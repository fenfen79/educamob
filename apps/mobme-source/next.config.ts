import type { NextConfig } from "next";

const isProd = process.env.NODE_ENV === "production";

const nextConfig: NextConfig = {
  compress: false,
  ...(isProd ? { output: "export", basePath: "/apps/mobme" } : {
    async rewrites() {
      return [
        {
          source: "/api/:path*",
          destination: "http://127.0.0.1:8000/api/:path*",
        },
      ];
    },
  }),
  allowedDevOrigins: [
    'subjective-hobby-handling-specials.trycloudflare.com',
    '*.trycloudflare.com',
    '192.168.1.12',
    'localhost',
    '127.0.0.1',
  ],
};

export default nextConfig;
