var path = require("path");
var BundleTracker = require("webpack-bundle-tracker");
("use strict");

const { VueLoaderPlugin } = require("vue-loader");

const { CleanWebpackPlugin } = require("clean-webpack-plugin");

module.exports = {
  mode: "development",
  entry: {
    app: "./terra_mars/frontend/js/app.js"
  },
  output: {
    path: path.resolve("./terra_mars/frontend/static/bundles/"),
    filename: "[name]-[hash].js"
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: "vue-loader"
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"]
      },
      {
        test: /\.scss$/,
        use: ["style-loader", "css-loader", "sass-loader"]
      },
    ],
  },
  plugins: [
    new VueLoaderPlugin(),
    new BundleTracker({ filename: "./terra_mars/webpack-stats.json" }),
    new CleanWebpackPlugin(),
  ]
};
