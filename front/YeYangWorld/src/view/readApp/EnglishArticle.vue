<template>
    <div v-for="item in items" :key="item.id" class="item">
        {{ item.text }}
    </div>
    <div v-if="isLoading" class="loading">Loading...</div>

</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const items = ref([]);
const isLoading = ref(false);
const mainContainer = ref(null);

// 模拟加载更多数据的函数
const loadMoreItems = () => {
    isLoading.value = true;
    // 模拟异步数据加载
    setTimeout(() => {
        const moreItems = Array.from({ length: 20 }, (_, index) => ({
            id: items.value.length + index,
            text: `Item ${items.value.length + index}`
        }));
        items.value.push(...moreItems);
        isLoading.value = false;
    }, 1000);
};

// 检查是否需要加载更多数据
const checkScroll = () => {
    const { scrollTop, clientHeight, scrollHeight } = document.documentElement;
    if (scrollTop + clientHeight >= scrollHeight - 10) { // 10 是一个阈值，可以根据需要调整
        loadMoreItems();
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
loadMoreItems();
</script>

<style scoped>
.item {
    background-color: #ffffff;
    color: #000000;
}
</style>