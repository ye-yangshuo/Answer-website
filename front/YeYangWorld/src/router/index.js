import {createRouter, createWebHistory} from 'vue-router'

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

export default router

