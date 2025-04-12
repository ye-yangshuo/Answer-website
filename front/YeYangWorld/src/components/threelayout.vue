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
    background-color: #c9c3c3;
}

/*主要内容*/
.main {
    position: fixed;
    left: 12%;
    right: 18%;
    height: 100%;
    background-color: #f9f1f1;
    overflow-y: auto;
}

/*左侧栏*/
.left {
    position: fixed;
    left: 0%;
    width: 12%;
    height: 90%;
    background-color: #f9f1f1;
}

/*右侧栏 */
.right {
    position: fixed;
    right: 0%;
    width: 18%;
    height: 90%;
    background-color: #f9f1f1;
    overflow-y: auto;
}



</style>