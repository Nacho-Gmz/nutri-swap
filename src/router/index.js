import { createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: Home
        },
        {
            path: '/swapper',
            component: () => import('../views/Swapper.vue')
        },
        {
            path: '/about',
            component: () => import('../views/About.vue')
        },
        {
            path: '/login',
            component: () => import('../views/Login.vue')
        },
        {
            path: '/register',
            component: () => import('../views/Register.vue')
        },
    ]
})

export default router