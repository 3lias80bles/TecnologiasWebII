import { useEffect, useState } from "react";
import PagesLayout from "../components/layouts/PagesLayout";
import { Link } from "react-router-dom";
import { obtenerUltimasTres } from "../service/vacante_Service";

export default function Home() {
    const [vacantes, setVacantes] = useState([]);
    const [vacanteSeleccionada, setVacanteSeleccionada] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        obtenerUltimasTres()
            .then((res) => {
                // Blindaje total
                if (Array.isArray(res.data)) {
                    setVacantes(res.data);
                } else {
                    console.error("La API no devolvió un array:", res.data);
                    setVacantes([]);
                }
            })
            .catch((err) => {
                console.error("Error al cargar vacantes:", err);
                setVacantes([]);
            })
            .finally(() => setLoading(false));
    }, []);

    return (
        <PagesLayout>
            {/* HERO */}
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
                    Ver Más Ofertas
                </Link>
            </section>

            {/* OFERTAS RECIENTES */}
            <section className="max-w-6xl mx-auto px-4 py-16">
                <h2 className="text-2xl font-bold mb-8 text-center">
                    Ofertas recientes
                </h2>

                {loading && (
                    <p className="text-center text-gray-500">
                        Cargando vacantes...
                    </p>
                )}

                {!loading && vacantes.length === 0 && (
                    <p className="text-center text-gray-500">
                        No hay vacantes disponibles por el momento.
                    </p>
                )}

                <div className="grid gap-6 md:grid-cols-3">
                    {vacantes.map((v) => (
                        <div
                            key={v.id_vacante ?? v.id}
                            className="bg-white p-6 rounded-xl shadow hover:shadow-lg transition"
                        >
                            <h3 className="font-semibold text-lg mb-2">
                                {v.nombre_vacante}
                            </h3>

                            <p className="text-gray-600 mb-4">
                                {v.descripcion}
                            </p>

                            <button
                                onClick={() => setVacanteSeleccionada(v)}
                                className="text-blue-600 font-semibold hover:underline"
                            >
                                Ver detalles →
                            </button>
                        </div>
                    ))}
                </div>
            </section>

            {/* MODAL */}
            {vacanteSeleccionada && (
                <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
                    <div className="bg-white p-6 rounded-lg max-w-md w-full">
                        <h3 className="text-xl font-bold mb-2">
                            {vacanteSeleccionada.nombre_vacante}
                        </h3>

                        <p className="mb-4">
                            {vacanteSeleccionada.detalles}
                        </p>

                        <button
                            onClick={() => setVacanteSeleccionada(null)}
                            className="bg-blue-600 text-white px-4 py-2 rounded"
                        >
                            Cerrar
                        </button>
                    </div>
                </div>
            )}
        </PagesLayout>
    );
}
