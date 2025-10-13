import axios from "axios";
export const api = axios.create({ baseURL: import.meta.env.VITE_API_URL || "http://localhost/api" });
export function setAuth(token?: string){ if(token) api.defaults.headers.common["Authorization"] = `Bearer ${token}`; else delete api.defaults.headers.common["Authorization"]; }
