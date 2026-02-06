import { useParams } from "react-router-dom";

export default function DetalleVacante() {
    const { id } = useParams();

    return (
        <div className="max-w-3xl mx-auto p-8 bg-white mt-10 rounded-xl shadow">
            <h2 className="text-2xl font-bold mb-4">
                Vacante #{id}
            </h2>
            <p className="mb-4">
                Descripción detallada de la vacante seleccionada.
            </p>
            <button className="bg-blue-600 text-white px-6 py-2 rounded">
                Postularme
            </button>
        </div>
    );
}
