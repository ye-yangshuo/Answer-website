
<template>

    <header class="header">
        <navigate></navigate>
        <div class="nav">
            <router-link class="return" to="/toolbegin">返回</router-link>
            <div class="name">markdown编辑器</div>
            <el-button class="upload" @click="upload">上传</el-button>
        </div>
    </header>
    <input class="title" placeholder="请输入标题" v-model="title"></input>
    <div id="vditor"></div>
  </template>



<script setup>
import separate from '/src/utils/Separate.js'

import Vditor from 'vditor'
import 'vditor/dist/index.css';

import { ref, onMounted ,inject} from 'vue';
const axios = inject('axios')

const vditor = ref()

function creatVditor() {
    vditor.value = new Vditor('vditor',{
    width: '1225px',
    height: '900px',
  })
}
onMounted(creatVditor)

const title = ref('')
const cover = ref('')
const content = ref('')
const category_id = ref(null)
const chinese = ref('')
const english = ref('')

async function upload(){
    content.value = vditor.value.getHTML()
    console.log(content.value)
    const [chinesetext,englishtext] = separate(content.value)
    chinese.value = chinesetext
    english.value = englishtext
    
    const response = await axios.post('/read/upload_article/',{
        title: title.value,
        cover: cover.value,
        category_id: category_id.value,
        chinese: chinese.value,
        english: english.value,
    })
    console.log(response.data)

}

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
    justify-content: space-between;
    font-size: 25px;
    color: #f12222;

}
.title{
    width: 1225px;
    height: 50px;
    font-size: 30px;
    color: #000000;
    font-weight: bold;

}


</style>