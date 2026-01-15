"use client";

import { useState } from "react";
import { api } from "@/lib/api";
import Link from "next/link";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function handleLogin(e: any) {
    e.preventDefault();
    setError("");

    try {
      const res = await api.post("/auth/login", { email, password });

      localStorage.setItem("token", res.data.token);
      window.location.href = "/feed"; // redirect to feed
    } catch (err: any) {
      setError(err?.response?.data?.message || "Invalid login");
    }
  }

  return (
    <div className="flex h-screen items-center justify-center bg-gray-50">
      <div className="w-[350px] p-8 bg-white border rounded-xl shadow-sm">

        <h1 className="text-3xl font-bold text-center mb-6 font-sans">
          Instagram
        </h1>

        <form onSubmit={handleLogin} className="flex flex-col gap-3">
          <input
            className="border p-2 rounded bg-gray-100"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
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
            Log In
          </button>
        </form>

        <p className="text-center text-sm mt-4">
          Don't have an account?{" "}
          <Link href="/register" className="text-blue-600 font-semibold">
            Sign up
          </Link>
        </p>
      </div>
    </div>
  );
}

