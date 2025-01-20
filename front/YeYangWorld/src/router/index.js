import {createRouter, createWebHistory} from 'vue-router'
import LoginRegister from '../view/LoginRegister.vue'


const routes = [
    {
        path : '/login',
        //TODO不知道view可不可以
        view : LoginRegister
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router

