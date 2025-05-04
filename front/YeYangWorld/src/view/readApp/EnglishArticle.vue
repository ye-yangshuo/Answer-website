<template>
    <div class="header">
    </div>
    <div v-for="item in items" :key="item.id" class="item" @click = 'englishread(item)'>
        <div class="item_content">
            <div class="english_title">{{ item.title.split('(')[1].split(')')[0] }} </div>
            <div class="chinese_title"> {{ item.title.split('(')[0] }}</div>
            <div class="item_footer">
                <div class="item_creator">{{ item.creator }}</div>
                <div class="item_watch">{{ item.watch_count }}</div>
                <div class="item_star">{{ item.star_count }}</div>
            </div>
        </div>
        <div class="item_image">
           
        </div>
    </div>
    <div v-if="isLoading" class="loading">Loading...</div>

</template>


<script setup>
import { ref, inject,onMounted, onUnmounted } from 'vue';
const axios = inject('axios');

const items = ref([]);
const isLoading = ref(false);
const count = ref(-1);

// 模拟加载更多数据的函数
async function loading() {
    if (isLoading.value) return; // 如果正在加载，则不执行
    isLoading.value = true;
    try {
        const response = await axios.post('/read/get_articl_list/', {count: count.value});
        const articlelist = response.data.article_list;
        count.value = response.data.count;
        console.log(articlelist);
        console.log(count.value);
        items.value.push(...articlelist); // 将新数据添加到现有数据中
        console.log(items.value);
    } catch (error) {
        console.error('Error loading data:', error);
    } finally {
        isLoading.value = false;
    }
}
// 检查是否需要加载更多数据
const checkScroll = () => {
    const { scrollTop, clientHeight, scrollHeight } = document.documentElement;
    if (scrollTop + clientHeight >= scrollHeight - 10) { // 10 是一个阈值，可以根据需要调整
        loading();
    }
};
// 添加和移除滚动事件监听器
onMounted(() => {
    window.addEventListener('scroll', checkScroll);
});
onUnmounted(() => {
    window.removeEventListener('scroll', checkScroll);
});
// 初始加载一些数据
loading();


//知识点：动态路由参数传递
import { useRouter } from 'vue-router';
const router = useRouter();
function englishread(item) {
    console.log(item.id);
    router.push({  name: 'englishread' , params:{articleid : item.id} }); // 传递参数到下一个页面
}   

</script>


<style scoped>
.header {
    height: 60px;
    background-color: #ffffff;
    border-bottom: 1px solid #E4E6EB;


}
.item {
    display: flex;
    flex-direction: row;
    height: 90px;
    background-color: #ffffff;
    border-bottom: #E4E6EB 2px solid;
    color: #000000;
}
.item_content {
    width: 80%;
    padding-left: 30px;
}
.english_title {
    font-size: 20px;
    font-weight: bold;
    color: #000000;
}
.chinese_title {
    font-size: 16px;
    color: #000000;
}
.item_footer{
    width:40%;
    display: flex;
    flex-direction: row;
    margin-top:10px;
}
.item_footer > div {
    margin-right: 50px;
    font-size: 14px;
    color: #000000;
}

.item_image {
    width: 14%;
    height: 87%;
    background-color: #E4E6EB;
    margin-top: 5px;
    margin-right: 25px;
}
</style>