import Vue from 'vue'
import store from "@/store"
import App from './App.vue'

Vue.config.productionTip = false

import Antd from "ant-design-vue"
import "ant-design-vue/dist/antd.css"
Vue.use(Antd)

import Contextmenu from 'vue-contextmenujs'
Vue.use(Contextmenu)

new Vue({
  render: h => h(App),
  store
}).$mount('#app')
