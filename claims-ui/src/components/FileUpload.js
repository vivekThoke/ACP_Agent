import React, { useState } from "react";

function FileUpload({ onFileSelect, onUpload, loading }) {
  const [dragActive, setDragActive] = useState(false);
  const [fileName, setFileName] = useState("");

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();

    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    const file = e.dataTransfer.files[0];
    if (file) {
      onFileSelect(file);
      setFileName(file.name);
    }
  };

  const handleChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      onFileSelect(file);
      setFileName(file.name);
    }
  };

  return (
    <div className="card">
      <h3>Upload Claim Document</h3>

      <div
        className={`upload-box ${dragActive ? "active" : ""}`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
      >
        <input type="file" onChange={handleChange} />

        <div className="upload-content">
          <p className="upload-icon">📄</p>
          <p>
            Drag & drop your file here, or <span>browse</span>
          </p>
          {fileName && <p className="file-name">{fileName}</p>}
        </div>
      </div>

      <button onClick={onUpload} disabled={loading}>
        {loading ? "Processing..." : "Upload & Process"}
      </button>
    </div>
  );
}

export default FileUpload;