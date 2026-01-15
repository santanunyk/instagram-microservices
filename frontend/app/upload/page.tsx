"use client";

import { useState } from "react";
import { api } from "@/lib/api";

export default function UploadPage() {
  const [caption, setCaption] = useState("");
  const [file, setFile] = useState<any>(null);

  const upload = async () => {
    const form = new FormData();
    form.append("caption", caption);
    form.append("file", file);

    await api.post("/posts/upload", form, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    alert("Uploaded successfully!");
  };

  return (
    <div className="max-w-xl mx-auto mt-10 space-y-4">
      <input
        type="text"
        className="border w-full p-2"
        placeholder="Caption..."
        onChange={(e) => setCaption(e.target.value)}
      />

      <input
        type="file"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />

      <button
        onClick={upload}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Upload
      </button>
    </div>
  );
}

