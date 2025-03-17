import {createRouter, createWebHistory} from 'vue-router'
import Introduce from '../view/introduce.vue'
import LoginRegister from '../view/LoginRegister.vue'
import Home from '../view/Home.vue'



const routes = [
    {
        path : '/',
        component : Introduce
    },

    {
        path : '/login',
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

