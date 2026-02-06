import axios from "axios";

import {
    getAccessToken,   // Obtiene el access token del storage
    getRefreshToken,  // Obtiene el refresh token del storage
    setTokens,        // Guarda nuevos tokens
    clearTokens,      // Elimina tokens (logout)
} from "../utils/token";

// Creamos una instancia de axios con configuración base
const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL, // URL base de la API desde variables de entorno
    headers: {
        "Content-Type": "application/json", // Todas las peticiones serán JSON
    },
});

/* ============================
   INTERCEPTOR DE REQUEST
   Agrega el access token a cada petición
   ============================ */
api.interceptors.request.use((config) => {
    // Obtenemos el access token
    const token = getAccessToken();

    // Si existe, lo agregamos al header Authorization
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }

    // Retornamos la configuración modificada
    return config;
});

/* ============================
   VARIABLES PARA CONTROLAR EL REFRESH TOKEN
   ============================ */

// Indica si ya se está refrescando el token
let isRefreshing = false;

// Cola de peticiones que fallaron mientras el token se refresca
let failedQueue = [];

// Procesa la cola una vez que el refresh termina
const processQueue = (error, token = null) => {
    failedQueue.forEach((prom) => {
        if (error) {
            // Si falló el refresh, se rechazan todas
            prom.reject(error);
        } else {
            // Si fue exitoso, se resuelven con el nuevo token
            prom.resolve(token);
        }
    });

    // Limpiamos la cola
    failedQueue = [];
};

/* ============================
   INTERCEPTOR DE RESPONSE
   Maneja expiración del access token (401)
   ============================ */
api.interceptors.response.use(
    // Si la respuesta es exitosa, se retorna tal cual
    (response) => response,

    // Manejo de errores
    async (error) => {
        const originalRequest = error.config;

        // Si el error es 401 (no autorizado)
        // y la petición aún no ha sido reintentada
        if (
            error.response?.status === 401 &&
            !originalRequest._retry
        ) {
            // Si ya hay un refresh en proceso,
            // se pone la petición en cola
            if (isRefreshing) {
                return new Promise((resolve, reject) => {
                    failedQueue.push({
                        resolve: (token) => {
                            // Se actualiza el token en el header
                            originalRequest.headers.Authorization =
                                "Bearer " + token;

                            // Se reintenta la petición
                            resolve(api(originalRequest));
                        },
                        reject,
                    });
                });
            }

            // Marcamos la petición como reintentada
            originalRequest._retry = true;
            isRefreshing = true;

            try {
                // Obtenemos el refresh token
                const refreshToken = getRefreshToken();

                // Llamamos al endpoint para refrescar el access token
                const res = await axios.post(
                    `${import.meta.env.VITE_API_URL}/auth/refresh`,
                    {},
                    {
                        headers: {
                            Authorization: `Bearer ${refreshToken}`,
                        },
                    }
                );

                // Guardamos el nuevo access token
                setTokens({ access_token: res.data.access_token });

                // Resolvemos todas las peticiones en cola
                processQueue(null, res.data.access_token);

                // Actualizamos el token en la petición original
                originalRequest.headers.Authorization =
                    "Bearer " + res.data.access_token;

                // Reintentamos la petición original
                return api(originalRequest);
            } catch (err) {
                // Si falla el refresh:
                // rechazamos todas las peticiones en cola
                processQueue(err, null);

                // Eliminamos tokens (logout)
                clearTokens();

                // Redirigimos al login
                window.location.href = "/login";

                return Promise.reject(err);
            } finally {
                // Indicamos que ya terminó el refresh
                isRefreshing = false;
            }
        }

        // Cualquier otro error se rechaza normalmente
        return Promise.reject(error);
    }
);

// Exportamos la instancia configurada
export default api;