import {createRouter, createWebHashHistory, RouteRecordRaw} from "vue-router";
import Home from "../views/home.vue";

const routes:RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/correction'
    }, {
        path: "/",
        name: "Home",
        component: Home,
        children: [
            {
                path: "/correction",
                name: "correction",
                meta: {
                    title: '纠错',
                    permiss: '1'
                },
                component: () => import ( /* webpackChunkName: "correction" */ "../views/correction.vue")
            }
        ]
    }, 
    {
        path: '/403',
        name: '403',
        meta: {
            title: '没有权限'
        },
        component: () => import (/* webpackChunkName: "403" */ '../views/403.vue')
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | Demo`;
    next()
});

export default router;