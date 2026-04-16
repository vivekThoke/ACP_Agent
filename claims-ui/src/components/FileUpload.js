import React from "react";

function FileUpload({ onFileSelect, onUpload, loading }) {
  return (
    <div className="card">
      <h3>Upload Claim Document</h3>

      <input
        type="file"
        onChange={(e) => onFileSelect(e.target.files[0])}
      />

      <button onClick={onUpload} disabled={loading}>
        {loading ? "Processing..." : "Upload & Process"}
      </button>
    </div>
  );
}

export default FileUpload;