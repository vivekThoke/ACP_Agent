import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://127.0.0.1:8000/process-claim", formData);
    setResponse(res.data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Insurance Claims Agent</h2>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>

      {response && (
        <div style={{ marginTop: "20px" }}>
          <h3>Structured Output</h3>

          <div>
            <p><b>Policy Number:</b> {response.extractedFields.policy_number || "N/A"}</p>
            <p><b>Name:</b> {response.extractedFields.policyholder_name || "N/A"}</p>
            <p><b>Date:</b> {response.extractedFields.incident_date || "N/A"}</p>
            <p><b>Damage:</b> {response.extractedFields.estimated_damage || "N/A"}</p>
          </div>

          <h3>Route</h3>
          <p>{response.recommendedRoute}</p>

          <h3>Reasoning</h3>
          <p>{response.reasoning}</p>

          <h3>Raw JSON</h3>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;