import { createApp } from 'vue'
import App from './App.vue'
import './style.css'

import axios from 'axios'
import router from "./router/index";

//创建app
const app = createApp(App)

//设置全局的axios
axios.defaults.baseURL = 'http://localhost:8080'
app.config.globalProperties.$axios = axios

//挂载路由
app.use(router)



//挂载app
app.mount('#app')