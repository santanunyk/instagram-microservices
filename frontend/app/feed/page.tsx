"use client";

import { useEffect, useState } from "react";
import { api } from "@/lib/api";
import PostCard from "@/components/PostCard";
import Navbar from "@/components/Navbar";

export default function FeedPage() {
  const [posts, setPosts] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/feed")
      .then((res) => setPosts(res.data))
      .finally(() => setLoading(false));
  }, []);

  if (loading)
    return (
      <div className="w-full h-screen flex items-center justify-center">
        <p className="text-gray-500 text-lg">Loading your feed…</p>
      </div>
    );

  return (
    <>
      <Navbar />
      <div className="max-w-xl mx-auto mt-6 space-y-4">
        {posts.length === 0 ? (
          <p className="text-center text-gray-500 mt-10">No posts found.</p>
        ) : (
          posts.map((p) => <PostCard key={p.id} post={p} />)
        )}
      </div>
    </>
  );
}

