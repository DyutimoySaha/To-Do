import React from "react";

const Task = ({ task }) => {
  return (
    <div className={`task ${task.priority.toLowerCase()}`}>
      <h3>{task.title}</h3>
      <p>{task.description}</p>
      <p>Deadline: {task.deadline}</p>
      <p>Priority: {task.priority}</p>
      <p>Label: {task.label}</p>
    </div>
  );
};

export default Task;
