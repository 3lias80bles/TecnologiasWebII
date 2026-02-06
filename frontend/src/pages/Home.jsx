import PagesLayout from "../components/layouts/PagesLayout";
import { Link } from "react-router-dom";

export default function Home() {
    return (
        <PagesLayout>
            <section className="bg-blue-600 text-white py-20 text-center">
                <h1 className="text-4xl font-bold mb-4">
                    Encuentra tu trabajo ideal
                </h1>
                <p className="mb-6">
                    Bienvenido a VacantesApp, aquí podrás encontrar ofertas de empleos que sean adecuados a tu perfil...
                </p>

                <Link
                    to="/vacantes"
                    className="bg-white text-blue-600 px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition"
                >
                    Ver Mas Ofertas
                </Link>
            </section>
            {/* Ofertas recientes */}
            <section className="max-w-6xl mx-auto px-4 py-16">
                <h2 className="text-2xl font-bold mb-8 text-center">
                    Ofertas recientes
                </h2>


                <div className="grid gap-6 md:grid-cols-3">
                    {/* Oferta 1 */}
                    <div className="bg-white p-6 rounded-xl shadow hover:shadow-lg transition">
                        <h3 className="font-semibold text-lg mb-2">
                            Desarrollador Frontend
                        </h3>
                        <p className="text-gray-600 mb-4">
                            Empresa tecnológica busca desarrollador con experiencia en React.
                        </p>
                        <Link
                            to="/vacantes"
                            className="text-blue-600 font-semibold hover:underline"
                        >
                            Ver detalles →
                        </Link>
                    </div>
                    {/* Oferta 2 */}
                    <div className="bg-white p-6 rounded-xl shadow hover:shadow-lg transition">
                        <h3 className="font-semibold text-lg mb-2">
                            Analista de Sistemas
                        </h3>
                        <p className="text-gray-600 mb-4">
                            Se requiere analista para soporte y documentación de sistemas.
                        </p>
                        <Link
                            to="/vacantes"
                            className="text-blue-600 font-semibold hover:underline"
                        >
                            Ver detalles →
                        </Link>
                    </div>
                    {/* Oferta 3 */}
                    <div className="bg-white p-6 rounded-xl shadow hover:shadow-lg transition">
                        <h3 className="font-semibold text-lg mb-2">
                            Diseñador UI/UX
                        </h3>
                        <p className="text-gray-600 mb-4">
                            Diseño de interfaces modernas y experiencia de usuario.
                        </p>
                        <Link
                            to="/vacantes"
                            className="text-blue-600 font-semibold hover:underline"
                        >
                            Ver detalles →
                        </Link>
                    </div>
                </div>
            </section>
        </PagesLayout>

    );
}
