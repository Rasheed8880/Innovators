import { useState } from 'react';
import axios from 'axios';

export default function InputSection({ setResult }) {
  const [inputType, setInputType] = useState("text");
  const [input, setInput] = useState("");

  const handleCheck = async () => {
    const res = await axios.post("http://localhost:5000/api/check", {
      input_type: inputType,
      input,
    });
    setResult(res.data);
  };

  return (
    <div className="p-4 flex flex-col gap-4">
      <select
        onChange={(e) => setInputType(e.target.value)}
        className="p-2 border rounded"
      >
        <option value="text">Text</option>
        <option value="link">URL</option>
        <option value="image">Image URL</option>
      </select>
      <textarea
        placeholder="Paste your text, URL, or image link here"
        rows={4}
        className="border p-2 rounded"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button
        onClick={handleCheck}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Check Info
      </button>
    </div>
  );
}
