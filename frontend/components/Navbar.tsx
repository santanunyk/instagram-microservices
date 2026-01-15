import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full bg-white shadow p-4 flex justify-between">
      <Link href="/feed" className="font-bold text-lg">
        InstaClone
      </Link>

      <div className="space-x-4">
        <Link href="/upload" className="text-blue-500">Upload</Link>
        <Link href="/profile" className="text-blue-500">Profile</Link>
      </div>
    </nav>
  );
}

