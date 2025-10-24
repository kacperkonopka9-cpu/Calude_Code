/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'inov-yellow': '#F5C344',
        'inov-navy': '#2C3E50',
      },
    },
  },
  plugins: [],
}
