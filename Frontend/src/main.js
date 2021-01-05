import Vue from 'vue'
import store from "@/store"
import App from './App.vue'
import router from '@/router'
//导入字体图标
import '@/assets/fonts/iconfont.css'
// 导入全局样式表
import '@/assets/css/global.css'
// 导入element ui
import ElementUI, { Message } from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
Vue.prototype.$message = Message;

Vue.config.productionTip = false

import axios from "axios"
Vue.prototype.$axios = axios

import Antd from "ant-design-vue"
import "ant-design-vue/dist/antd.css"
Vue.use(Antd)

import Contextmenu from 'vue-contextmenujs'
Vue.use(Contextmenu)

new Vue({
    render: h => h(App),
    store,
    router
}).$mount('#app')