import React, { useState } from "react";
import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);

  const addTask = (task) => {
    setTasks([...tasks, task]);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Task Manager</h1>
      </header>
      <TaskForm addTask={addTask} />
      <TaskList tasks={tasks} />
    </div>
  );
}

export default App;
