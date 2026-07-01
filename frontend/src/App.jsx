import { useState } from "react";
import api from "./services/api";
import ReactMarkdown from "react-markdown";

function App() {
  // Analysis States
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);

  // Comparison States
  const [company1, setCompany1] = useState("");
  const [company2, setCompany2] = useState("");
  const [comparison, setComparison] = useState(null);

  const [loading, setLoading] = useState(false);

  // Analyze Single Company
  const analyzeStock = async () => {
    if (!query.trim()) return;

    try {
      setLoading(true);
      setResult(null);

      const response = await api.post("/full-analysis", {
        query,
      });

      setResult(response.data);
    } catch (error) {
      console.log(error);
      alert("Failed to analyze stock.");
    } finally {
      setLoading(false);
    }
  };

  // Compare Two Companies
  const compareStocks = async () => {
    if (!company1 || !company2) return;

    try {
      setLoading(true);
      setComparison(null);

      const response = await api.post("/compare", {
        company_1: company1,
        company_2: company2,
      });

      setComparison(response.data);
    } catch (error) {
      console.log(error);
      alert("Comparison failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      {/* Header */}
      <h1 className="text-4xl font-bold text-center mb-10">
        Financial Multi-Agent Analyst
      </h1>

      {/* Analyze Section */}
      <div className="bg-white p-6 rounded shadow mb-8">
        <h2 className="text-2xl font-bold mb-4">
          Analyze Company
        </h2>

        <div className="flex gap-4">
          <input
            className="border p-3 rounded w-full"
            placeholder="Analyze NVIDIA for long-term investment"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />

          <button
            className="bg-blue-500 text-white px-6 rounded"
            onClick={analyzeStock}
          >
            Analyze
          </button>
        </div>
      </div>

      {/* Compare Section */}
      <div className="bg-white p-6 rounded shadow mb-8">
        <h2 className="text-2xl font-bold mb-4">
          Compare Companies
        </h2>

        <div className="flex gap-4">
          <input
            className="border p-3 rounded w-full"
            placeholder="Company 1 (e.g. NVIDIA)"
            value={company1}
            onChange={(e) => setCompany1(e.target.value)}
          />

          <input
            className="border p-3 rounded w-full"
            placeholder="Company 2 (e.g. AMD)"
            value={company2}
            onChange={(e) => setCompany2(e.target.value)}
          />

          <button
            className="bg-green-500 text-white px-6 rounded"
            onClick={compareStocks}
          >
            Compare
          </button>
        </div>
      </div>

      {/* Loading */}
      {loading && (
        <div className="text-center text-2xl font-semibold">
          Running AI Agents...
        </div>
      )}

      {/* Comparison Result */}
      {comparison && (
        <div className="bg-white p-6 rounded shadow mb-8">
          <h2 className="text-2xl font-bold mb-4">
            Comparison Result
          </h2>

          <pre className="overflow-x-auto">
            {JSON.stringify(comparison, null, 2)}
          </pre>
        </div>
      )}

      {/* Analysis Result */}
      {result && (
        <div className="space-y-6">
          {/* Market Data */}
          <div className="bg-white p-6 rounded shadow">
            <h2 className="text-2xl font-bold mb-4">
              Market Data
            </h2>

            <pre className="overflow-x-auto">
              {JSON.stringify(result.market_data, null, 2)}
            </pre>
          </div>

          {/* News */}
          <div className="bg-white p-6 rounded shadow">
            <h2 className="text-2xl font-bold mb-4">
              Latest News
            </h2>

            <pre className="overflow-x-auto">
              {JSON.stringify(result.news_data, null, 2)}
            </pre>
          </div>

          {/* SEC Analysis */}
          <div className="bg-white p-6 rounded shadow">
            <h2 className="text-2xl font-bold mb-4">
              SEC Analysis
            </h2>

            <ReactMarkdown>
              {result.sec_analysis}
            </ReactMarkdown>
          </div>

          {/* Bull Thesis */}
          <div className="bg-green-100 p-6 rounded shadow">
            <h2 className="text-2xl font-bold mb-4">
              Bull Thesis 🐂
            </h2>

            <ReactMarkdown>
              {result.bull_case}
            </ReactMarkdown>
          </div>

          {/* Bear Thesis */}
          <div className="bg-red-100 p-6 rounded shadow">
            <h2 className="text-2xl font-bold mb-4">
              Bear Thesis 🐻
            </h2>

            <ReactMarkdown>
              {result.bear_case}
            </ReactMarkdown>
          </div>

          {/* Final Recommendation */}
          <div className="bg-blue-100 p-6 rounded shadow">
            <h2 className="text-2xl font-bold mb-4">
              Final Recommendation ⚖️
            </h2>

            <pre className="overflow-x-auto">
              {JSON.stringify(
                result.final_recommendation,
                null,
                2
              )}
            </pre>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;