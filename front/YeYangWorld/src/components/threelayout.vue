<template>
    <div class="threelayout">

        <div class="header">
            <slot name="header"></slot>
        </div>
        
        <div class="container">
            <div class="left">
                <slot name="left"></slot>
            </div>

            <div class="main">
                <slot name="main"></slot>
            </div>

            <div class="right">
                <slot name="right"></slot>
            </div>
        </div>

    </div>

</template>


<script setup>

import navigate from '../components/navigate.vue'


</script>

<style scoped>
.threelayout {
    width: 100%;
    height: 100vh;
    position: absolute;
    top: 0;
    left: 0;
}

.container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    position: absolute;
    top: 10%;
    left: 0%;
    background-color: #F5F7FA;
}

/*主要内容*/
.main {
    position: fixed;
    left: 15%;
    right: 15%;
    height: 100%;
    background-color: #F5F7FA;
    overflow-y: auto;
}

/*左侧栏*/
.left {
    position: fixed;
    left: 0%;
    width: 15%;
    height: 90%;
    background-color: #F5F7FA;
}

/*右侧栏 */
.right {
    position: fixed;
    right: 0%;
    width: 15%;
    height: 90%;
    background-color: #F5F7FA;
    overflow-y: auto;
}



</style>