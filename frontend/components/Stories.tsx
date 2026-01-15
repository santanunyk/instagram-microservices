"use client";

import { motion } from "framer-motion";

const users = [
  { name: "emma", img: "https://randomuser.me/api/portraits/women/60.jpg" },
  { name: "lisa", img: "https://randomuser.me/api/portraits/women/44.jpg" },
  { name: "john", img: "https://randomuser.me/api/portraits/men/32.jpg" },
  { name: "mark", img: "https://randomuser.me/api/portraits/men/65.jpg" },
  { name: "sara", img: "https://randomuser.me/api/portraits/women/23.jpg" },
  { name: "alex", img: "https://randomuser.me/api/portraits/men/72.jpg" },
];

export default function Stories() {
  return (
    <div className="flex space-x-4 p-3 overflow-x-auto scrollbar-hide bg-white border-b border-gray-300">
      {users.map((user, i) => (
        <motion.div
          key={i}
          whileTap={{ scale: 0.85 }}
          className="flex flex-col items-center"
        >
          {/* Story ring */}
          <div className="w-16 h-16 rounded-full p-[2px] bg-gradient-to-tr from-yellow-500 via-pink-500 to-purple-600">
            <img
              src={user.img}
              className="w-full h-full rounded-full border-2 border-white object-cover"
            />
          </div>
          <p className="text-xs mt-1">{user.name}</p>
        </motion.div>
      ))}
    </div>
  );
}

