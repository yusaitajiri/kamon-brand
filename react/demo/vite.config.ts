import react from "@vitejs/plugin-react";
import { resolve } from "node:path";
import { defineConfig } from "vite";

// The demo pages use the kit's source, not dist, so a change shows without a build.
export default defineConfig({
  plugins: [react()],
  resolve: { alias: { "@yusai/kamon-react": resolve(import.meta.dirname, "../src/index.ts") } },
  server: { port: 5199, strictPort: true },
  build: {
    rollupOptions: {
      input: Object.fromEntries(
        ["index", "elements", "sample", "dashboard"].map((page) => [page, resolve(import.meta.dirname, `${page}.html`)]),
      ),
    },
  },
});
