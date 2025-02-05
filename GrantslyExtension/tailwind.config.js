/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html', // Adjust this if you have an `index.html` file
    './src/**/*.{vue,js,ts,jsx,tsx}', // Adjust this if your project uses Vue, JS, or TS files
  ],
  theme: {
    extend: {},
    fontFamily: {
      sans: ['Montserrat', 'Arial', 'sans-serif'], // Set Montserrat as default sans font
    },
  },
  plugins: [], // You can add plugins if you need them
}
