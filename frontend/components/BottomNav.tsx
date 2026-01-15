"use client";

import { FaHome, FaSearch, FaPlay, FaUser } from "react-icons/fa";
import { motion } from "framer-motion";

export default function BottomNav() {
  const items = [
    { icon: <FaHome size={22} />, label: "Home" },
    { icon: <FaSearch size={22} />, label: "Search" },
    { icon: <FaPlay size={22} />, label: "Reels" },
    { icon: <FaUser size={22} />, label: "Profile" },
  ];

  return (
    <div className="fixed bottom-0 w-full border-t bg-white border-gray-300 flex justify-around py-2">
      {items.map((item, i) => (
        <motion.button key={i} whileTap={{ scale: 0.8 }}>
          {item.icon}
        </motion.button>
      ))}
    </div>
  );
}

