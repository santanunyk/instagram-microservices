"use client";

import { useState } from "react";
import { api } from "@/lib/api";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const router = useRouter();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function login() {
    const res = await api.post("/auth/login", { email, password });
    localStorage.setItem("token", res.data.token);
    router.push("/feed");
  }

  return (
    <div className="max-w-sm mx-auto mt-20 space-y-4">
      <input
        className="border w-full p-2"
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        type="password"
        className="border w-full p-2"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />

      <button
        onClick={login}
        className="bg-blue-500 text-white p-2 rounded w-full"
      >
        Login
      </button>
    </div>
  );
}

