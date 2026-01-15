"use client";

import { useEffect, useState } from "react";
import { api } from "@/lib/api";

export default function PostDetail({ params }: any) {
  const { id } = params;

  const [post, setPost] = useState<any>(null);
  const [comments, setComments] = useState([]);

  useEffect(() => {
    api.get(`/posts/${id}`).then((res) => setPost(res.data));
    api.get(`/comments/${id}`).then((res) => setComments(res.data));
  }, []);

  if (!post) return <p className="mt-20 text-center">Loading…</p>;

  return (
    <div className="max-w-xl mx-auto mt-10">
      <h2 className="font-bold text-lg">{post.username}</h2>

      <img
        src={`http://localhost:8003${post.media_url}`}
        className="rounded mt-4"
      />

      <p className="mt-3">
        <strong>{post.username}</strong> {post.caption}
      </p>

      <h3 className="mt-6 font-bold">Comments</h3>

      {comments.map((c: any) => (
        <div key={c.id} className="border-b py-2">
          <strong>{c.username}</strong>: {c.text}
        </div>
      ))}
    </div>
  );
}

