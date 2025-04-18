import { createApp } from 'vue'
import App from './App.vue'
import './style.css'

import router from "./router/index";
import axiosInstance from './utils/GlobalAxios';
import ElementPlus from 'element-plus';
import "element-plus/theme-chalk/index.css";
import * as icons from '@element-plus/icons-vue';
import SvgIcon from './components/SvgIcon.vue';
import './assets/icon/iconfont.js';

//创建app
const app = createApp(App)

//全局挂载axios
app.provide('axios', axiosInstance)

//挂载路由
app.use(router)

//全局挂载element-plus
app.use(ElementPlus)
Object.keys(icons).forEach(key => {
    app.component(key, icons[key])
  });

//全局挂载svg-icon
app.component('SvgIcon', SvgIcon)

//挂载app
app.mount('#app')