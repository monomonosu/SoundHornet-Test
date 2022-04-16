// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

module.exports = {
  assetsDir: 'static',
  publicPath: '/front/dist/',
  pages: {
    index: {
      entry: 'src/main.js', // 必須パラメータ
      title: 'ページタイトル',
    }
  }
}