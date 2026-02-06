import { Link } from "react-router-dom";

export default function Navbar() {
    //props
    return (
        <nav className="bg-gray-600 text-white px-6 py-4 flex justify-between items-center">
            <Link to="/" className="text-xl font-bold">
                VacantesApp
            </Link>

            <div className="space-x-4">
                <Link to="/home" className="hover:underline">
                    Inicio
                </Link  >
                <Link to="/mis-vacantes" className="hover:underline">
                    Administración
                </Link>
                <Link to="/acerca" className="hover:underline">
                    Acerca
                </Link>
                <Link to="/" className="bg-white text-blue-600 px-3 py-1 rounded">
                    Cerrar Sesión
                </Link>
            </div>
        </nav>
    );
}
