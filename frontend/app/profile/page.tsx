"use client";

export default function ProfilePage() {
  const email = "sunaofficials@gmail.com";

  return (
    <div className="max-w-xl mx-auto mt-20">
      <h1 className="text-xl font-bold">Profile</h1>
      <p>Email: {email}</p>
    </div>
  );
}

