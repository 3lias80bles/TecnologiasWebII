import { Link } from "react-router-dom";

export default function VacanteCard({ vacante }) {
    return (
        <div className="bg-white p-6 rounded-xl shadow hover:shadow-xl transition">
            <h2 className="text-xl font-bold mb-2">{vacante.titulo}</h2>
            <p className="text-gray-500 mb-4">{vacante.empresa}</p>

            <Link
                to={`/vacantes/${vacante.id}`}
                className="text-blue-600 font-semibold"
            >
                Ver detalle →
            </Link>
        </div>
    );
}
