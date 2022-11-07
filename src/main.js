import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';

import './assets/index.less'

import vueSeamlessScroll from 'vue-seamless-scroll' // 循环滚动


Vue.config.productionTip = false

//全局挂载所有接口名
import http from "./interfaces/http"
Vue.prototype.$http = http;

Vue.use(ElementUI)
Vue.use(vueSeamlessScroll)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
