import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "../pages/Home";
import Vacantes from "../pages/Vacantes";
import DetalleVacante from "../pages/DetalleVacante";
import Login from "../pages/Login";
import CrearVacante from "../pages/CrearVacante";
import MisVacantes from "../pages/MisVacantes";
import Acerca from "../pages/Acerca";
import Mensaje from "../pages/Mensaje";

export default function AppRoute() {
    return (
        <BrowserRouter> {/* COmponenete de react router dom para biscar rutas*/}
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/vacantes" element={<Vacantes />} />
                <Route path="/vacantes/:id" element={<DetalleVacante />} />
                <Route path="/crear" element={<CrearVacante />} />
                <Route path="/mis-vacantes" element={<MisVacantes />} />
                <Route path="/acerca" element={<Acerca />} />
                <Route path="/mensaje" element={<Mensaje />} />
                <Route path="/" element={<Home />} />{/* Elemento que quiero redirigir */}

            </Routes>
        </BrowserRouter>
    );
}