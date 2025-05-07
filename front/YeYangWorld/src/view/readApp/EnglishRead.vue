<template>

  <header class="navigate">

    <router-link to="/readbegin" class="back">返回</router-link>


    <a class="logo" href='http://localhost:5173/home'></a>


    <div class="collect" @click="iscollect = !iscollect">
      <el-icon :size="28" v-show="!iscollect">
        <star />
      </el-icon>
      <el-icon :size="28" v-show="iscollect">
        <StarFilled />
      </el-icon>
    </div>

  </header>



  <div class="english_read">

    <div class="title">
      <span v-html="title"></span>
    </div>


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

//获取文章
const title = ref('');
const contentstring = ref('');
const content = ref([]);
async function getarticle() {
  const response = await axios.post('/read/get_article_detail/', { article_id: article_id })
  const data = response.data.article;
  contentstring.value = data.content;
  title.value = data.title;
  title.value = title.value.split('(')[1].split(')')[0];
  console.log(contentstring.value);
  content.value = separate(contentstring.value);
  console.log(content.value);
}
onBeforeMount(getarticle)

//显示中文
const ischinese = ref(false);

//收藏
const iscollect = ref(false);

</script>




<style scoped>
/*导航栏 */
.navigate {
  position: sticky;
  top: 0;
  width: 100%;
  height: 45px;
  z-index: 1000;
  background-color: #E4E2E2;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  border-bottom: #000000 solid 1px;
}
  /*返回键*/
  .back {
    display: block;
    width: 100px;
    height: 45px;
  }
  /*网站标志*/
  .logo {
    width: 100px;
    height: 45px;
    background-image: url('/src/assets/userApp/image.png');
    background-size: 60%;
    background-repeat: no-repeat;
    background-position: center;
  }
  /*收藏键*/
  .collect {
    width: 30px;
    margin-right: 5%;
    color: #000000;
    text-align: center;
  }



/*主页面*/
.english_read {
  width: 700px;
  background-color: #E4E2E2;
  color: #29313a;
  font-size: 20px;
  display: flex;
  flex-direction: column;
}
  /*标题*/
  .title {
    font-weight: bold;
    font-size: 30px;
    margin-top: 60px;
    margin-bottom: 30px;
    text-align: center;
  }
  /*内容展示部分*/
  .content {
    display: flex;
    flex-direction: column;
  }



/*工具栏*/ 
.tools {
  position: sticky;
  width: 100%;
  bottom: 0%;
  height: 45px;
  display: flex;
  flex-direction: row;
  background-color: #E4E2E2;
  z-index: 1000;
  border-top: #000000 solid 1px;
}
</style>