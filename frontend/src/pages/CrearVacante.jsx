import PagesLayout from "../components/layouts/PagesLayout";

export default function CrearVacante() {
    return (
        <PagesLayout>
            <div className="max-w-xl mx-auto p-8 bg-white mt-10 rounded-xl shadow">
                <h2 className="text-2xl font-bold mb-6">
                    Crear Vacante
                </h2>

                <input className="w-full mb-4 p-2 border rounded" placeholder="Título" />
                <input className="w-full mb-4 p-2 border rounded" placeholder="Empresa" />
                <textarea className="w-full mb-4 p-2 border rounded" placeholder="Descripción"></textarea>

                <button className="bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700 transition">
                    Guardar Vacante
                </button>
            </div>
        </PagesLayout>
    );
}
//crear componentes para botones y formularios y buscadores