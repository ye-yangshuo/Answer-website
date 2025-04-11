<template>
    <div class="answer">

        <navigate></navigate>

        <div class="container">
            <div class="left">
                <div class="left_top">题型</div>
                <div class="left_table">
                    <div class='table_item item1' @click="">常识判断</div>
                </div>
            </div>

            <div class="main">

            </div>

            <div class="right">
                <div class="right_table">
                    <div class="right_history">历史记录</div>
                    <div class="right_collection">收藏</div>
                    <div class="right_note">笔记</div>
                </div>
            </div>
        </div>
    </div>

</template>


<script setup>

import navigate from '../components/navigate.vue'


</script>

<style scoped>
.answer {
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

.left_top {
    position: absolute;
    top: 5%;
    left: 22%;
    width: 60%;
    height: 10%;
    font-size: 3vh;
    color: #000000;
}

.left_table {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: absolute;
    top: 15%;
    left: 5%;
    width: 95%;
    height: 100%;
    overflow-y: auto;
}

.table_item {
    color: #000000;
}

.item1 {
    width: 100%;
    height: 5%;
    font-size: 3vh;
    position: absolute;
    top: 5%;
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

.right_table {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: absolute;
    top: 2%;
    left: 5%;

    width: 90%;
    height: 30%;

    overflow-y: auto;

    background-color: #d6d0d0;
}

.right_history {
    position: absolute;
    top: 7%;
    left: 22%;

    width: 60%;
    height: 25%;

    font-size: 3vh;
    color: #000000;

}

.right_collection {
    position: absolute;
    top: 35%;
    left: 22%;

    width: 60%;
    height: 25%;

    font-size: 3vh;
    color: #000000;
}

.right_note {
    position: absolute;
    top: 65%;
    left: 22%;

    width: 60%;
    height: 25%;

    font-size: 3vh;
    color: #000000;
}
</style>