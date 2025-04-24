
<template>

    <header class="header">
        <navigate></navigate>
        <div class="nav">
            <router-link class="return" to="/toolbegin">返回</router-link>
            <div class="title">markdown编辑器</div>
        </div>
    </header>
    <div id="vditor" ></div>
  </template>


<script setup>
import navigate from '/src/components/navigate.vue';

import Vditor from 'vditor'
import 'vditor/dist/index.css';

import { ref, onMounted } from 'vue';

const vditor = ref()

function creatVditor() {
    vditor.value = new Vditor('vditor',{
    height: '1250px',
    width: '900px',
  })
}

onMounted(creatVditor)

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
</style>