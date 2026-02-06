import { Navigate, Outlet } from "react-router-dom";
import { getAccessToken } from "../utils/token";

export default function ProtectedRoute() {
    const token = getAccessToken();

    return token ? <Outlet /> : <Navigate to="/login" replace />;
}