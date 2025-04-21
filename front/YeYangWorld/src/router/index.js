import {createRouter, createWebHistory} from 'vue-router'

import axiosInstance from '../utils/GlobalAxios';

import LoginRegister from '../view/userApp/LoginRegister.vue'
import Home from '../view/public/Home.vue'
import QuestionType1 from '../view/datiApp/QuestionType1.vue'
import ReadBegin from '../view/readApp/ReadBegin.vue'


const routes = [
    {
        path : '/',
        component : LoginRegister
    },

    {
        path : '/home',
        component : Home
    },

    {
        path : '/questiontype1',
        component : QuestionType1,
    },

    {
        path : '/readbegin',
        component : ReadBegin,
    }
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

