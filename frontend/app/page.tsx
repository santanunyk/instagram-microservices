import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-50">
      <h1 className="text-4xl font-bold mb-6">Welcome to Instagram Clone</h1>

      <div className="flex gap-4">
        <Link
          href="/login"
          className="px-6 py-2 bg-blue-500 text-white rounded-lg shadow"
        >
          Login
        </Link>

        <Link
          href="/register"
          className="px-6 py-2 bg-green-500 text-white rounded-lg shadow"
        >
          Sign Up
        </Link>
      </div>
    </div>
  );
}

