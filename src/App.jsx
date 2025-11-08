import { useState } from "react";

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [input, setInput] = useState("");

  const addTask = () => {
    if (!input.trim()) return;
    setTasks([...tasks, { id: Date.now(), text: input, completed: false }]);
    setInput("");
  };

  const toggleTask = (id) => {
    setTasks(tasks.map((t) =>
      t.id === id ? { ...t, completed: !t.completed } : t
    ));
  };

  const removeTask = (id) => {
    setTasks(tasks.filter((t) => t.id !== id));
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center py-10">
      <h1 className="text-4xl font-bold mb-6">Todo List</h1>

      <div className="flex mb-6">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Add a new task..."
          className="px-4 py-2 rounded-l-lg text-black"
        />
        <button
          onClick={addTask}
          className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-r-lg"
        >
          Add
        </button>
      </div>

      <ul className="w-full max-w-md space-y-3">
        {tasks.map((t) => (
          <li
            key={t.id}
            className={`flex justify-between items-center p-3 rounded-lg ${
              t.completed ? "bg-green-700" : "bg-gray-700"
            }`}
          >
            <span
              onClick={() => toggleTask(t.id)}
              className={`cursor-pointer ${
                t.completed ? "line-through text-gray-300" : ""
              }`}
            >
              {t.text}
            </span>
            <button
              onClick={() => removeTask(t.id)}
              className="text-red-400 hover:text-red-500"
            >
              ✕
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
