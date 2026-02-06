import { useNavigate } from "react-router-dom"; {/* Se importa el hook para navegar entre rutas*/ }

export default function Login() {
    const navigate = useNavigate();//
    const handlelogin = () => {
        navigate("/home")
    }
    return (
        <div className="max-w-md mx-auto mt-16 p-8 bg-white rounded-xl shadow">
            <h2 className="text-2xl font-bold mb-6">
                Iniciar Sesión
            </h2>

            <input
                className="w-full mb-4 p-2 border rounded"
                placeholder="Correo electrónico"
            />
            <input
                type="password"
                className="w-full mb-4 p-2 border rounded"
                placeholder="Contraseña"
            />
            <form onSubmit={handlelogin}>
                <button type="submit" className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition">
                    Entrar
                </button>
            </form>
        </div>
    );
}
