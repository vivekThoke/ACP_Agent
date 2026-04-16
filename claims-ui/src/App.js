import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import ResultCard from "./components/ResultCard";
import Loader from "./components/Loader";
import ErrorMessage from "./components/ErrorMessage";
import { processClaim } from "./services/api";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a file");
      return;
    }

    setLoading(true);
    setError("");
    setResponse(null);

    try {
      const formData = new FormData();
      formData.append("file", file);

      const res = await processClaim(formData);
      setResponse(res.data);
    } catch (err) {
      setError("Failed to process claim. Check backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h2>Insurance Claims AI</h2>

      <FileUpload
        onFileSelect={setFile}
        onUpload={handleUpload}
        loading={loading}
      />

      {loading && <Loader />}
      {error && <ErrorMessage message={error} />}
      {response && <ResultCard data={response} />}
    </div>
  );
}

export default App;