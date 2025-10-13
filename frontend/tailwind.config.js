/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        "lunno-primary": "#5C6AC4",
        "lunno-secondary": "#A5B4FC",
        "lunno-ink": "#1E293B",
        "lunno-surface": "#F8FAFC",
        "lunno-lilac": "#E0E7FF"
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui"]
      }
    }
  },
  plugins: [],
};
