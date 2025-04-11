import { useState } from 'react';
import Navbar from './components/Navbar';
import InputSection from './components/InputSection';
import ResultCard from './components/ResultCard';

function App() {
  const [result, setResult] = useState(null);
  return (
    <div className="min-h-screen bg-blue-50 font-sans">
      <Navbar />
      <div className="max-w-2xl mx-auto mt-8">
        <InputSection setResult={setResult} />
        <ResultCard result={result} />
      </div>
    </div>
  );
}

export default App;