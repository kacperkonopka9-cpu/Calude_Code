/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'inov-yellow': '#F5C344', // Inov brand primary
        'inov-navy': '#2C3E50',   // Inov brand secondary
      },
    },
  },
  plugins: [],
}
