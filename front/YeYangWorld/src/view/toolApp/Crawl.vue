<template>
    <header class="header">
        <navigate></navigate>
        <div class="nav">
            <router-link class="return" to="/toolbegin">返回</router-link>
            <div class="title">网页爬虫</div>
        </div>
    </header>
    <div class="body">
        <div class="left_main">
            <input type="text" placeholder="请输入网址" class="input_url" v-model="url" /></input>
            <button class="crawl_button" @click="crawl">爬取</button>
        </div>
        <div class="right_main">
            <textarea class="result">{{ requestData }}</textarea>
        </div>
    </div>
    <div class="footer">
        <div class="footer-text">© 2023 YeYangWorld. All rights reserved.</div>
    </div>
</template>

<script setup>
import axios from 'axios';

import { ref } from 'vue';
let url = ref('');
const requestData = ref(''); // 用于存储请求返回的数据


async function crawl() {
    const newurl = ref('');
    newurl.value = `https://r.jina.ai/${url.value}`;
    console.log(url.value)
    const config = {
        method: 'GET',
        url: newurl.value,
    };
    try {
        const response = await axios(config);
        console.log('statusCode:', response.status);
        requestData.value = response.data;
        console.log(requestData.value);
        return response.data; // 请求完成后，返回响应数据

    } catch (error) {
        console.error(error);
        throw error; // 捕获错误并抛出
    }

};




</script>

<style scoped>
.header {
    width: 100%;
    display: flex;
    flex-direction: column;
}

.nav {
    width: 100%;
    display: flex;
    flex-direction: row;
    background-color: #f7efef;

    font-size: 25px;
    color: #f12222;
}

.nav .return {
    margin-right: 40%;
}

.body {
    width: 1250px;
    height: 900px;
    display: flex;
    flex-direction: row;
    background-color: #f7efef;
}

.body .left_main {
    width: 50%;
    height: 80%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.body .left_main .input_url {
    width: 400px;
    height: 100px;
    font-size: 20px;
}

.body .left_main .crawl_button {
    background-color: #F6F7F8;
    margin-top: 100px;
    width: 100px;
    height: 50px;
    font-size: 20px;
    color: #f90000;
}

.body .right_main {
    width: 50%;
    height: 80%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.body .right_main .result {
    width: 300px;
    height: 300px;
    font-size: 20px;
}
</style>