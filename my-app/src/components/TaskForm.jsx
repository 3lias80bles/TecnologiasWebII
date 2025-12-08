import { useState } from "react";

export default function TaskForm({ addTask }) {
    const [text, setText] = useState("");
    const [date, setDate] = useState("");
    const [taskTime, setTaskTime] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();

        addTask(text, date);
        setText("");
        setDate("");
        setTaskTime("");
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Escribe una tarea"
                value={text}
                onChange={(e) => setText(e.target.value)}
                style={{ width: "300px", marginRight: "10px" }}
            />
            <input
                type="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
            />
            <input
                type="time"
                value={taskTime}
                onChange={(e) => setTaskTime(e.target.value)}
            />

            <button>Agregar</button>
        </form>
    );
}
