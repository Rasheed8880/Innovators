export default function ResultCard({ result }) {
    if (!result) return null;
  
    return (
      <div className="bg-white shadow p-4 rounded-md mt-4">
        <h2 className="text-xl font-bold mb-2">Verdict</h2>
        <p className="text-lg text-gray-800 mb-2">{result.verdict}</p>
        <div className="flex items-center gap-1 mb-2">
          {Array.from({ length: result.rating }).map((_, idx) => (
            <span key={idx}>⭐</span>
          ))}
          {Array.from({ length: 5 - result.rating }).map((_, idx) => (
            <span key={idx}>☆</span>
          ))}
        </div>
        <p className="text-sm text-gray-600 mb-2">{result.message}</p>
        {result.references.length > 0 && (
          <div>
            <p className="font-semibold">References:</p>
            <ul className="list-disc pl-6 text-blue-600">
              {result.references.map((link, idx) => (
                <li key={idx}>
                  <a href={link} target="_blank" rel="noopener noreferrer">
                    {link}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    );
  }