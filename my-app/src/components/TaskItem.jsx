export default function TaskItem({ task, toggleTask, deleteTask }) {
    return (
        <li style={{ marginBottom: "10px" }}>
            <span
                style={{
                    textDecoration: task.completed ? "line-through" : "none",
                    marginRight: "15px"
                }}
            >
                {task.text}
            </span>

            <button onClick={() => toggleTask(task.id)}>
                {task.completed ? "Desmarcar" : "Completar"}
            </button>

            <button
                onClick={() => deleteTask(task.id)}
                style={{ marginLeft: "10px", color: "red" }}
            >
                Eliminar
            </button>
        </li>
    );
}
export default function TaskItem({ task, toggleTask, deleteTask }) {
    return (
        <li style={{ marginBottom: "10px" }}>
            <span
                style={{
                    textDecoration: task.completed ? "line-through" : "none",
                    marginRight: "15px"
                }}
            >
                {task.text}
            </span>

            <button onClick={() => toggleTask(task.id)}>
                {task.completed ? "Desmarcar" : "Completar"}
            </button>

            <button
                onClick={() => deleteTask(task.id)}
                style={{ marginLeft: "10px", color: "red" }}
            >
                Eliminar
            </button>
        </li>
    );
}
