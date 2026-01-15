"use client";

import { motion } from "framer-motion";
import { useState } from "react";
import { FaHeart, FaRegHeart, FaRegComment, FaBookmark, FaRegBookmark, FaShare } from "react-icons/fa";

export default function PostCard() {
  const [liked, setLiked] = useState(false);
  const [saved, setSaved] = useState(false);
  const [likes, setLikes] = useState(214);

  const toggleLike = () => {
    setLiked(!liked);
    setLikes(liked ? likes - 1 : likes + 1);
  };

  return (
    <div className="bg-white border border-gray-300 rounded-xl max-w-lg mx-auto mt-6 shadow-sm">

      {/* HEADER */}
      <div className="flex items-center px-4 py-3">
        <img
          src="https://randomuser.me/api/portraits/women/68.jpg"
          className="w-10 h-10 rounded-full"
          alt="Profile"
        />
        <div className="ml-3">
          <p className="font-semibold text-sm">emma_wilson</p>
          <p className="text-xs text-gray-500">UID: 887172</p>
        </div>
      </div>

      {/* POST IMAGE */}
      <div className="w-full bg-gray-100">
        <motion.img
          src="https://images.unsplash.com/photo-1519741497674-611481863552"
          alt="Post"
          className="w-full object-cover rounded-sm"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
        />
      </div>

      {/* ACTIONS */}
      <div className="flex items-center justify-between px-4 py-3">
        <div className="flex items-center space-x-4">

          {/* LIKE BUTTON */}
          <motion.button
            whileTap={{ scale: 0.7 }}
            onClick={toggleLike}
            className="text-2xl"
          >
            {liked ? (
              <FaHeart className="text-red-500" />
            ) : (
              <FaRegHeart className="text-gray-800" />
            )}
          </motion.button>

          {/* COMMENT */}
          <motion.button whileTap={{ scale: 0.7 }} className="text-2xl">
            <FaRegComment className="text-gray-800" />
          </motion.button>

          {/* SHARE */}
          <motion.button whileTap={{ scale: 0.7 }} className="text-2xl">
            <FaShare className="text-gray-800" />
          </motion.button>
        </div>

        {/* SAVE */}
        <motion.button whileTap={{ scale: 0.7 }} onClick={() => setSaved(!saved)}>
          {saved ? (
            <FaBookmark className="text-2xl text-gray-900" />
          ) : (
            <FaRegBookmark className="text-2xl text-gray-800" />
          )}
        </motion.button>
      </div>

      {/* LIKE COUNT */}
      <div className="px-4 -mt-2">
        <p className="font-semibold text-sm">{likes} likes</p>
      </div>

      {/* CAPTION */}
      <div className="px-4 py-2">
        <p className="text-sm">
          <span className="font-semibold">emma_wilson</span> Enjoying the sunny
          vibes 🌞✨ #travel #life
        </p>
      </div>

      {/* TIME */}
      <p className="text-xs text-gray-400 px-4 pb-4">2 hours ago</p>
    </div>
  );
}

