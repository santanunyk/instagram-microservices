"use client";

import { useState } from "react";
import { api } from "@/lib/api";

export default function RegisterPage() {
  const [username, setUser] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function register() {
    await api.post("/auth/register", { username, email, password });
    alert("Registered! Please login.");
  }

  return (
    <div className="max-w-sm mx-auto mt-20 space-y-4">
      <input className="border p-2 w-full" placeholder="Username" onChange={(e)=>setUser(e.target.value)} />
      <input className="border p-2 w-full" placeholder="Email" onChange={(e)=>setEmail(e.target.value)} />
      <input className="border p-2 w-full" placeholder="Password" type="password" onChange={(e)=>setPassword(e.target.value)} />

      <button className="bg-green-600 text-white p-2 rounded w-full" onClick={register}>
        Register
      </button>
    </div>
  );
}

