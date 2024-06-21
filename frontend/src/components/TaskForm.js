import React, { useState } from "react";

const TaskForm = ({ addTask }) => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [deadline, setDeadline] = useState("");
  const [priority, setPriority] = useState("Low");
  const [label, setLabel] = useState("Development");

  const handleSubmit = (e) => {
    e.preventDefault();
    addTask({ title, description, deadline, priority, label });
    setTitle("");
    setDescription("");
    setDeadline("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
      />
      <textarea
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        required
      ></textarea>
      <input
        type="date"
        value={deadline}
        onChange={(e) => setDeadline(e.target.value)}
        required
      />
      <select value={priority} onChange={(e) => setPriority(e.target.value)}>
        <option value="Low">Low</option>
        <option value="Medium">Medium</option>
        <option value="High">High</option>
      </select>
      <select value={label} onChange={(e) => setLabel(e.target.value)}>
        <option value="Development">Development</option>
        <option value="Design">Design</option>
        <option value="Content">Content</option>
      </select>
      <button type="submit">Add Task</button>
    </form>
  );
};

export default TaskForm;
