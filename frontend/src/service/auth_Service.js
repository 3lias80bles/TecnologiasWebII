import api from "../api/axios";
import { setTokens, clearTokens } from "../utils/token";
//api es una estancia de axios configurada para comunicarse con el backend

export const login = async (nombre_usuario, password) => {
  const res = await api.post("/auth/login", { nombre_usuario, password });
  setTokens(res.data.tokens);
};

export const logout = () => {
  clearTokens();
};

