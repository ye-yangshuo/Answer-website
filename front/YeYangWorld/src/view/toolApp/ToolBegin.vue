<template>
    
    <navigate></navigate>

    <div class="toolbegin">
        <router-link class="tool_crawl" to="/toolbegin/crawl">
            <p>网页爬虫</p>
            <p>可以爬取网页内容并转化为markdown格式</p>
        </router-link>
        <router-link class="tool_crawl" to="/toolbegin/markdown">
            <p>markdown编辑器</p>
            <p>实时预览markdown</p>
        </router-link>
        <router-link class="tool_crawl" to="/toolbegin/crawl">
            <p>网页爬虫</p>
            <p>可以爬取网页内容并转化为markdown格式</p>
        </router-link>
        <router-link class="tool_crawl" to="/toolbegin/crawl">
            <p>网页爬虫</p>
            <p>可以爬取网页内容并转化为markdown格式</p>
        </router-link>

    </div>
</template>

<script setup>

</script>

<style scoped>
.toolbegin {
  /* 容器宽度设置为1200px，高度自适应 */
  width: 1200px;
  height:900px;
  background-color: #ffffff;

  /* 使用grid布局 */
  display: grid;
  grid-template-columns: 1fr 1fr; /* 两列，每列占比1fr */
  grid-gap: 20px; /* 设置网格之间的间隔 */
  justify-items: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  padding: 20px; /* 内边距 */
  box-sizing: border-box; /* 包含padding和border在内的总宽高 */
}

.toolbegin>a {
    /* 设置工具项的样式 */
    width: 400px;
    height: 200px;
    background-color: #d8bdbd; /* 背景颜色 */
    border-radius: 10px; /* 圆角边框 */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 阴影效果 */
    color: #000000;
    text-decoration: none; /* 去掉链接下划线 */
    display: flex; /* 使用flex布局 */
    flex-direction: column; /* 垂直排列内容 */
    justify-content: center; /* 垂直居中内容 */
    align-items: center; /* 水平居中内容 */

}




</style>
