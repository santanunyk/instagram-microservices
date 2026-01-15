/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    turbo: false,              // 🚫 disable turbopack
  },

  webpack(config) {
    config.resolve.alias['@'] = __dirname;   // ✅ your alias
    return config;
  }
};

module.exports = nextConfig;

