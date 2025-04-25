import { createRouter, createWebHistory } from 'vue-router'

import axiosInstance from '../utils/GlobalAxios';



// 使用 import.meta.glob 动态导入所有模块化的路由文件
const modules = import.meta.glob('../router/modules/*.js');
console.log(modules)
// 初始化路由数组
let routes = [];

// 遍历模块并导入路由配置
for (const path in modules) {
  // 调用函数以动态导入模块
  const module = await modules[path]();
  // 将模块的默认导出（路由配置数组）合并到主路由数组
  routes.push(...module.default);
}

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes,
});

const axios = axiosInstance
router.beforeEach(async function (to, from, next) {
    const response = await axios.post('/user/user_verify/')
    // 判断是否登录
    if (response.data.result == null && to.path != '/') {
        next('/')
    }
    else {
        next()
    }
})


export default router

