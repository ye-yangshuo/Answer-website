<template>
  <header class="navigate">
    <router-link to="/readbegin" class="back">返回</router-link>
    <a class="logo" href='http://localhost:5173/home'></a>
  </header>

  <div class="english_read">
    <div class="content">
      <div v-for="item in content" :key="item">
        <span v-html="item.english"></span>
        <span v-html="item.chinese" v-if="ischinese"></span>
      </div>
    </div>
  </div>

  <div class="tools">
    <el-button @click="ischinese = !ischinese">{{ ischinese ? '隐藏中文' : '显示中文' }}</el-button>
  </div>

</template>

<script setup>
import { ref, inject, onBeforeMount } from 'vue';
import { useRoute } from 'vue-router';
import separate from '../../utils/Separate';
const axios = inject('axios');
const route = useRoute();
const article_id = route.params.articleid;

const contentstring = ref('');
const content = ref([]);
const ischinese = ref(false);
async function getarticle() {
  const response = await axios.post('/read/get_article_detail/', { article_id: article_id })
  const data = response.data.article;
  contentstring.value = data.content;
  console.log(contentstring.value);
  content.value = separate(contentstring.value);
  console.log(content.value);
}
onBeforeMount(getarticle)


</script>

<style scoped>
.navigate {
  position: sticky;
  top: 0;
  left: 0;
  width: 100%;
  height: 45px;
  display: flex;
  flex-direction: row;
  background-color: #ffffff;
  z-index: 1000;
  border-bottom: #29313a solid 1px;
}

.back {
  display: block;
  width: 100px;
  height: 45px;
}

.logo {
  width: 100px;
  height: 45px;
  position: absolute;
  left: 45%;
  background-image: url('/src/assets/userApp/image.png');
  background-size: 60%;
  background-repeat: no-repeat;
  background-position: center;
}



.english_read {
  width: 700px;
  background-color: #ffffff;
  color: #29313a;
  font-size: 20px;
  display: flex;
  flex-direction: column;
}

.tools {
  position: sticky;
  width: 100%;
  bottom:0%;
  height: 45px;
  display: flex;
  flex-direction: row;
  background-color: #ffffff;
  z-index: 1000;
  border-bottom: #29313a solid 1px;
}

.content {
  display: flex;
  flex-direction: column;

}
</style>