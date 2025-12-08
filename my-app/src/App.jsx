import { useState } from "react";
import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";

export default function App() {
  const [tasks, setTasks] = useState([]);

  const addTask = (text, date, TaskTime) => {
    // Validación
    if (!text.trim()) {
      alert("La tarea no puede estar vacía.");
      return;
    }
    if (text.trim().split(" ").length < 3) {
      alert("La tarea debe tener al menos 3 palabras.");
      return;
    }
    if (text.length > 150) {
      alert("La tarea no puede superar los 150 caracteres.");
      return;
    }

    const newTask = {
      id: Date.now(),
      text,
      date,
      TaskTime,
      completed: false
    };

    setTasks([...tasks, newTask]);
  };

  const toggleTask = (id) => {
    setTasks(tasks.map(t =>
      t.id === id ? { ...t, completed: !t.completed } : t
    ));
  };

  const deleteTask = (id) => {
    setTasks(tasks.filter(t => t.id !== id));
  };
  const pendingCount = tasks.filter(task => !task.completed).length;
  const completedCount = tasks.filter(task => task.completed).length;


  return (
    <div >


      <h1>Gestor de Tareas</h1>
      <TaskForm addTask={addTask} />

      <h2>Pendientes</h2>
      <p><strong>Tareas pendientes:</strong> {pendingCount}</p>
      <TaskList
        tasks={tasks.filter(t => !t.completed)}
        toggleTask={toggleTask}
        deleteTask={deleteTask}

      />
      <h2>Completadas</h2>
      <p><strong>Tareas completadas:</strong> {completedCount}</p>
      <TaskList
        tasks={tasks.filter(t => t.completed)}
        toggleTask={toggleTask}
        deleteTask={deleteTask}
      />
    </div>
  );
}
