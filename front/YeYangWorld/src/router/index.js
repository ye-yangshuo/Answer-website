import {createRouter, createWebHistory} from 'vue-router'

import axiosInstance from '../utils/GlobalAxios';

import LoginRegister from '/src/view/userApp/LoginRegister.vue'
import Home from '/src/view/public/Home.vue'
import QuestionType1 from '/src/view/datiApp/QuestionType1.vue'
import ReadBegin from '/src/view/readApp/ReadBegin.vue'
import ToolBegin from '/src/view/toolApp/ToolBegin.vue';
import Crawl from '/src/view/toolApp/Crawl.vue';
import Markdown from '/src/view/toolApp/Markdown.vue';


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
    },
    {
        path : '/toolbegin',
        component : ToolBegin,
    },
    {
        path : '/toolApp/crawl',
        component : Crawl,
    },
    { 
        path : '/toolApp/markdown',
        component : Markdown,
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

