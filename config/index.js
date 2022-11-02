'use strict'

const path = require('path')

module.exports = {
  dev: {
    // Paths
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',
    proxyTable: {
      '/api': {
        target: process.env.NODE_ENV == "development" ? "http://localhost:8080/" : "http://10.136.211.125:8080", // 本地
        // target: "http://10.136.211.125:8080" , // 后端ip
        changeOrigin: true, // 允许跨域 在本地会创建一个虚拟服务端，然后发送请求的数据，并同时接收请求的数据，这样服务端和服务端进行数据的交互就不会有跨域问题
        logLevel: 'debug',
        pathRewrite: { // 路径重写，
          '^/api': '/' // 路径会被代理成 http://。。。/api ，但是我们不需要/api这段字段，重写替换为空字符。
        }
      },
      '/': {
        // target: "http://localhost:8080/" , // 本地
        target: "http://10.136.211.125:8080", // 后端ip
        changeOrigin: true, // 允许跨域 在本地会创建一个虚拟服务端，然后发送请求的数据，并同时接收请求的数据，这样服务端和服务端进行数据的交互就不会有跨域问题
        logLevel: 'debug',
      }

    },

    // host: 'localhost', // 可以通过 process.env.HOST 进行重写
    port: 8080, // 可以通过 process.env.PORT 重写, 如被占用，会自动更换
    autoOpenBrowser: true, // 构建完成自动打开浏览器
    errorOverlay: true,
    notifyOnErrors: true,
    poll: false, // https://webpack.js.org/configuration/dev-server/#devserver-watchoptions-


    /**
     * Source Maps
     */

    // https://webpack.js.org/configuration/devtool/#development
    devtool: 'cheap-module-eval-source-map',

    // If you have problems debugging vue-files in devtools,
    // set this to false - it *may* help
    // https://vue-loader.vuejs.org/en/options.html#cachebusting
    cacheBusting: true,

    cssSourceMap: true
  },

  build: {
    // Template for index.html
    //打包到Hbuilder中与打包到cordova中需要做的配置
    index: path.resolve(__dirname, '../dist/index.html'),
    assetsRoot: path.resolve(__dirname, '../dist'),
    assetsSubDirectory: 'static',
    assetsPublicPath: './',

    /**
     * Source Maps
     */

    productionSourceMap: false,
    // https://webpack.js.org/configuration/devtool/#production
    devtool: '#source-map',

    // Gzip off by default as many popular static hosts such as
    // Surge or Netlify already gzip all static assets for you.
    // Before setting to `true`, make sure to:
    // npm install --save-dev compression-webpack-plugin
    productionGzip: false,
    productionGzipExtensions: ['js', 'css'],

    // Run the build command with an extra argument to
    // View the bundle analyzer report after build finishes:
    // `npm run build --report`
    // Set to `true` or `false` to always turn it on or off
    bundleAnalyzerReport: process.env.npm_config_report,
    fileExt: fileExt
  }
}