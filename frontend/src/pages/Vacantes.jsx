import VacanteCard from "../components/VacanteCard";
import Pagination from "../components/Pagination";

export default function Vacantes() {
    //arreglo de vacantes de ejemplo
    const vacantes = [
        { id: 1, titulo: "Frontend React", empresa: "Tech MX" },
        { id: 2, titulo: "Backend Node", empresa: "Code SA" },
        { id: 3, titulo: "Fullstack Developer", empresa: "Dev Corp" },
    ];

    return (
        <div className="p-8">
            <h1 className="text-2xl font-bold mb-6">
                Vacantes Disponibles
            </h1>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {vacantes.map(v => (
                    <VacanteCard key={v.id} vacante={v} />
                ))}
            </div>

            <Pagination />
        </div>
    );
}
