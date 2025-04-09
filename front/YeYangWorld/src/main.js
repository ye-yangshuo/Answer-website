import { createApp } from 'vue'
import App from './App.vue'
import './style.css'

import router from "./router/index";
import axiosInstance from './utils/GlobalAxios';
import ElementPlus from 'element-plus';

//创建app
const app = createApp(App)

//全局挂载axios
app.provide('axios', axiosInstance)

//挂载路由
app.use(router)
app.use(ElementPlus)

//挂载app
app.mount('#app')