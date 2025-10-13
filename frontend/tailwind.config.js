/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        lunno: {
          primary: "#5C6AC4",
          secondary: "#A5B4FC",
          ink: "#1E293B",
          surface: "#F8FAFC",
          lilac: "#E0E7FF"
        }
      },
      boxShadow: {
        soft: "0 8px 24px -12px rgba(15, 23, 42, 0.12)"
      },
      borderRadius: {
        xl2: "1rem"
      }
    }
  },
  plugins: []
}
