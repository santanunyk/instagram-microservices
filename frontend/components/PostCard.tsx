import Link from "next/link";

export default function PostCard({ post }: any) {
  return (
    <div className="border rounded p-4 shadow bg-white">
      <h2 className="font-semibold mb-2">{post.username}</h2>

      <img
        src={`http://localhost:8003${post.media_url}`}
        className="rounded"
      />

      <p className="mt-2">
        <strong>{post.username}</strong> {post.caption}
      </p>

      <Link
        href={`/post/${post.id}`}
        className="text-blue-600 mt-2 inline-block"
      >
        View Comments →
      </Link>
    </div>
  );
}

