<template>
  <navigate></navigate>


    <threelayout1>
      <template v-slot:left>
        <div class="left">
          <el-menu class="left_menu" default-active="/readbegin/englisharticle" router>
            <el-sub-menu index="English">
              <template #title>
                <span>英语</span>
              </template>
              <el-menu-item index="/readbegin/englisharticle">英语文章</el-menu-item>
              <el-menu-item index="/readbegin/englishbook">英语书籍</el-menu-item>
            </el-sub-menu>
            <el-sub-menu index="Chinese">
              <template #title>中文</template>
              <el-menu-item index="/readbegin/chinesearticle">中文文章</el-menu-item>
              <el-menu-item index="/readbegin/chinesebook">中文书籍</el-menu-item>
            </el-sub-menu>
          </el-menu>
        </div>
      </template>

      <template v-slot:main>
        <router-view></router-view>
      </template>

      <template v-slot:right>
        <div class="right">
          <router-link class="upload" to="/toolbegin/markdown">上传书籍</router-link>
          <el-menu class="right_menu" router >
            <el-menu-item index="/readbegin/history">历史记录</el-menu-item>
            <el-menu-item index="/readbegin/collect">收藏</el-menu-item>
          </el-menu>
        </div>
      </template>
    </threelayout1>


</template>


<script setup>
import threelayout1 from '/src/components/threelayout1.vue'





</script>

<style scoped>





/*左侧菜单栏*/
.left_menu {
  width: 100%;
  height: 500px;
  background-color: #ffffff;
}

/*右侧菜单栏*/
.upload {
  display: block;
  width: 100%;
  height: 40px;
  color: #000000;
  font-weight: bold;
  font-size: 20px;
  text-align: center;

  margin-bottom: 30px;
}

.right_menu {
  margin-bottom: 10%;
}
</style>