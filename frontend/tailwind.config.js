/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['NanumSquare_acB', 'sans-serif'],
      },
      colors: {
        primary: '#EBECFA',
        secondary: '#1E215B',
        tertiay: 'A6A7B5',
      }
    },
  },
  plugins: [],
};
