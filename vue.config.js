const IS_PRODUCTION = process.env.NODE_ENV === 'production'


module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  publicPath: IS_PRODUCTION ? 'https://g-store-app.herokuapp.com/' : '/',
  // publicPath: 'http://localhost:8000/',
  // For Production, replace set baseUrl to CDN
  // And set the CDN origin to `yourdomain.com/static`
  // Whitenoise will serve once to CDN which will then cache
  // and distribute
  css: {
    loaderOptions: {
      sass: {
        prependData: '@import "@/assets/scss/app.scss";',
      },
    },
  },
  devServer: {
    proxy: {
      '/api*': {
        // Forward frontend dev server request for /api to django dev server
        target: 'http://localhost:8000/',
      },
    },
  },
}
