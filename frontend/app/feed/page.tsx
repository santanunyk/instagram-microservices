import Stories from "@/components/Stories";
import PostCard from "@/components/PostCard";
import BottomNav from "@/components/BottomNav";

export default function FeedPage() {
  return (
    <div className="pb-20">
      {/* STORIES */}
      <Stories />

      {/* POSTS */}
      <div className="space-y-6 pt-4">
        <PostCard />
        <PostCard />
        <PostCard />
        <PostCard />
      </div>

      {/* BOTTOM NAV */}
      <BottomNav />
    </div>
  );
}

