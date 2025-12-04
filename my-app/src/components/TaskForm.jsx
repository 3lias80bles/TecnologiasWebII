import { useState } from "react";

export default function TaskForm({ addTask }) {
    const [text, setText] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        addTask(text);
        setText(""); // limpiar input
    };

    return (
        <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
            <input
                type="text"
                placeholder="Escribe una tarea..."
                value={text}
                onChange={(e) => setText(e.target.value)}
                style={{ width: "300px", marginRight: "10px" }}
            />

            <button>Agregar</button>
        </form>
    );
}
