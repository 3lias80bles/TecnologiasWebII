import api from "../api/axios";

export const obtenerUltimasTres = () => api.get("/vacantes/ultimas")

export const crearVacante = (data) =>
    api.post("/vacantes", data);