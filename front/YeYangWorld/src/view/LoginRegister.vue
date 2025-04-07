<template>
    <div class="background">
    </div>

    <login @isregister="receive" @islogin=" receiver" v-show="!is"></login>
    <register @isregister="receive" v-show = 'is' ></register>
</template>


<script setup>
import login from '../components/login.vue';
import register from '../components/register.vue';

import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();

const is = ref(false);
const receive = (isregister) => {
    is.value = isregister.value;
}
const receiver = () => {
    router.push('/home');
}


</script>






<style scoped>

.background {  
    width: 100%;
    height: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;

    background-image: url("../public/background_img.jpeg");

    /* 背景图垂直、水平均居中 */
    background-position: center center;
    /* 背景图不平铺 */
    background-repeat: no-repeat;
    /* 当内容高度大于图片高度时，背景图像的位置相对于viewport固定 */
    background-attachment: fixed;
    /* 让背景图基于容器大小伸缩 */
    background-size: cover;
    /* 设置背景颜色，背景图加载过程中会显示背景色 */
    background-color: #464646;
}


</style>