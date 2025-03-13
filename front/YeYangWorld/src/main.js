import { createApp } from 'vue'
import App from './App.vue'
import './style.css'

import axios from 'axios'
import router from "./router/index";
import axiosInstance from './utils/GlobalAxios';

//创建app
const app = createApp(App)

//全局挂载axios
app.provide('axios', axiosInstance)

//挂载路由
app.use(router)

//挂载app
app.mount('#app')