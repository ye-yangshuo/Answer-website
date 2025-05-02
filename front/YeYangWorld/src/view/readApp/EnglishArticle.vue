<template>
    <div class="header">
    </div>
    <div v-for="item in items" :key="item.id" class="item">
        <div class="item_content">
            <div class="english_title"></div>
            <div class="chinese_title"></div>
            <div class="item_footer">
                <div class="item_author"></div>
                <div class="item_watch"></div>
                <div class="item_star"></div>
            </div>
        </div>
        <div class="item_image"></div>
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
        items.value.push(...response.data); // 将新数据添加到现有数据中
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
</style>