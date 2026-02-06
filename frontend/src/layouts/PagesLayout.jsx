import Navbar from "../Navbar"; {/* Se importa el componentes */ }
import Footer from "../Footer";

{/* componente que envuelve las páginas*/ }
export default function PagesLayout({ children}) {
    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow">
                {children}
            </main>
            <Footer />
        </div>

    );
}