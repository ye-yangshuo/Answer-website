import LoginRegister from '/src/view/userApp/LoginRegister.vue'
import Home from '/src/view/public/Home.vue'

export default [
    {   
        path: '/',
        component: LoginRegister,
        name: 'loginRegister',
    },
    {
        path: '/home',
        component: Home,
        name: 'home',
    }
]