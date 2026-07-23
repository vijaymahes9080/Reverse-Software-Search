import type { NextConfig } from "next";

const isProd = process.env.NODE_ENV === 'production';

const nextConfig: NextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
  basePath: isProd ? '/Reverse-Software-Search' : '',
  assetPrefix: isProd ? '/Reverse-Software-Search/' : '',
  typescript: {
    ignoreBuildErrors: false,
  },
};

export default nextConfig;
