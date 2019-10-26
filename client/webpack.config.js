const path = require("path");

module.exports = {
  entry: {
    index: "./src/index.js"
  },
  output: {
    filename: "bundle.js",
    path: path.join(__dirname, "../static/js")
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', "@babel/preset-react"]
          }
        }
      },
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
    ]
  }
}