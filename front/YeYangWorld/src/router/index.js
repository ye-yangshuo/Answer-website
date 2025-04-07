import {createRouter, createWebHistory} from 'vue-router'

import axiosInstance from '../utils/GlobalAxios';

import LoginRegister from '../view/LoginRegister.vue'
import Home from '../view/Home.vue'




const routes = [
    {
        path : '/',
        component : LoginRegister
    },

    {
        path : '/home',
        component : Home
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

const axios = axiosInstance
router.beforeEach(async function(to, from, next) {
    const response = await axios.post('/user/user_verify/')
    // 判断是否登录
    if (response.data.result == null && to.path != '/')
    {
        next('/')
    }
    else
    {
        next()
    }
})


export default router

