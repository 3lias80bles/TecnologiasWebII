export default function Pagination() {
    return (
        <div className="flex justify-center mt-8 space-x-2">
            <button className="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300">
                Anterior
            </button>
            <button className="px-4 py-2 bg-blue-600 text-white rounded">
                1
            </button>
            <button className="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300">
                2
            </button>
            <button className="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300">
                Siguiente
            </button>
        </div>
    );
}
