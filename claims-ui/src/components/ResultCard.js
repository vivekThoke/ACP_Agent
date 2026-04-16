import React from "react";

function ResultCard({ data }) {
  const fields = data.extractedFields || {};

  return (
    <div className="card">
      <h3>Claim Summary</h3>

      <div className="grid">
        <p><b>Policy Number:</b> {fields.policy_number || "N/A"}</p>
        <p><b>Name:</b> {fields.policyholder_name || "N/A"}</p>
        <p><b>Date:</b> {fields.incident_date || "N/A"}</p>
        <p><b>Damage:</b> {fields.estimated_damage || "N/A"}</p>
      </div>

      <h4>Recommended Route</h4>
      <p>{data.recommendedRoute}</p>

      <h4>Reasoning</h4>
      <p>{data.reasoning}</p>

      <details>
        <summary>Raw JSON</summary>
        <pre>{JSON.stringify(data, null, 2)}</pre>
      </details>
    </div>
  );
}

export default ResultCard;