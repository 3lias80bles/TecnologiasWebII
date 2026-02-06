import PagesLayout from "../components/layouts/PagesLayout";
export default function Acerca() {
    return (
        <PagesLayout>
            <div className="max-w-3xl mx-auto p-8">
                <h2 className="text-2xl font-bold mb-4 text-center">
                    Acerca
                </h2>
                <p className="text-center">
                    Aplicación de vacantes desarrollada en Tecnologías Web II
                </p>
            </div>
        </PagesLayout>

    );
}
