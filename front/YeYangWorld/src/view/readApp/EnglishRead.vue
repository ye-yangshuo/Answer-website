<template>
    <div>
      <h1>English Read</h1>
      <div v-html="english" class="article-content"></div>
        

    </div>
  </template>
  
  <script setup>
  import { ref, inject ,onBeforeMount} from 'vue';
  import { useRoute } from 'vue-router';
  const axios = inject('axios');
  const route = useRoute();
  const article_id = route.params.articleid;

  const english = ref();
  const chinese = ref([]);


  async function getarticle(){
    const response = await axios.post('/read/get_article_detail/', {article_id: article_id})
    const data = response.data.article;
    english.value = data.english;
    chinese.value = data.chinese;
    console.log(english.value);
    console.log(chinese.value);
    console.log(response.data.article);
  }
  
  onBeforeMount(getarticle)

  </script>
  
  <style scoped>
  /* 样式内容 */
  </style>
  