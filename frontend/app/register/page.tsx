"use client";

import { useState } from "react";
import { api } from "@/lib/api";
import Link from "next/link";

export default function RegisterPage() {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function handleRegister(e: any) {
    e.preventDefault();
    setError("");

    try {
      const res = await api.post("/auth/register", {
        email,
        username,
        password,
      });

      localStorage.setItem("token", res.data.token);
      window.location.href = "/feed";
    } catch (err: any) {
      setError(err?.response?.data?.message || "Registration failed");
    }
  }

  return (
    <div className="flex h-screen items-center justify-center bg-gray-50">
      <div className="w-[350px] p-8 bg-white border rounded-xl shadow-sm">

        <h1 className="text-3xl font-bold text-center mb-6 font-sans">
          Instagram
        </h1>

        <form onSubmit={handleRegister} className="flex flex-col gap-3">

          <input
            className="border p-2 rounded bg-gray-100"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            className="border p-2 rounded bg-gray-100"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <input
            type="password"
            className="border p-2 rounded bg-gray-100"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          {error && (
            <p className="text-red-500 text-sm text-center">{error}</p>
          )}

          <button className="bg-blue-500 text-white py-2 rounded font-semibold">
            Sign Up
          </button>
        </form>

        <p className="text-center text-sm mt-4">
          Already have an account?{" "}
          <Link href="/login" className="text-blue-600 font-semibold">
            Log In
          </Link>
        </p>

      </div>
    </div>
  );
}

