import { Link } from "react-router-dom";//ñse importa Link para la navegacion entre paginas
import Footer from "../components/Footer";
import Navbar from "../components/Navbar";

export default function MisVacantes() {
    return (
        <div className="max-w-6xl mx-auto px-4 py-8">
            <div className="border rounded-xl shadow overflow-hidden">
                <div className="bg-blue-600 text-white px-6 py-4">
                    <h3 className="text-lg font-semibold">
                        Bienvenido
                    </h3>
                </div>

                <div className="p-6 bg-white space-y-4">
                    <div>
                        <p className="font-bold">Username</p>
                        <p className="text-gray-600">elias</p>
                    </div>

                    <div>
                        <p className="font-bold">Email</p>
                        <p className="text-gray-600">roblessergioelias@gmail.com</p>
                    </div>

                    <div>
                        <p className="font-bold">Perfil</p>
                        <p className="text-gray-600">Admin</p>
                    </div>

                    <div>
                        <p className="font-bold">Estatus</p>
                        <p className="text-gray-600">estatus</p>
                    </div>
                </div>
            </div>

        </div>
    );
}
