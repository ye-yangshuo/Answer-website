<template>
    <div class="answer">

        <threelayout>
            <template v-slot:header><navigate></navigate></template>

            <template v-slot:left>
                <div class="left_top">题型</div>
                <div class="left_table">
                    <router-link class='table_item item1' to="/questiontype1">常识判断</router-link>
                </div>
            </template>

            <template v-slot:main>

                <div class="question_table">
                    <div class="main_title">常识判断</div>
                    <div class="main_question">{{question}}属于国家一类保护动物的是？</div>
                    <div class="main_answer">
                        <div class="answer_item" v-for="(item,index) in answer" :key="index">122{{item}}</div>
                    </div>
                    <div class="main_analysis">解析：{{analysis}}</div>
                </div>

                <div class="main_button">
                    <button class="button1">上一题</button>
                    <button class="button2">下一题</button>
                </div>

            </template>

            <template v-slot:right>
                <div class="right_table">
                    <div class="right_history">历史记录</div>
                    <div class="right_collection">收藏</div>
                    <div class="right_note">笔记</div>
                </div>
            </template>

        </threelayout>

    </div>
</template>


<script setup>

import threelayout from '../components/threelayout.vue'
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



/*主要内容*/
.question_table{
    position:absolute;
    top:2%;
    left:0%;

    width:95%;
    height:70%;
    background-color: #ffffff;

    display: flex;
    flex-direction: column;
    justify-content: space-between;

    overflow-y :auto;
}
.main_title{
    position:absolute;
    top:4%;
    left:2%;
    font-size: 3vh;
    background-color: #000000;
}
.main_question{
    position:absolute;
    top:15%;
    left:10%;
    background-color: #000000;

    font-size: 2vw;
}



.main_button{
    position:absolute;
    top:75%;
    left:8%;
    width:80%;
    height:9%;  
}
.button1 {  
    position: absolute;
    left:0%;

    width:10%;
    height:100%;
    background-color: #c4bbbb;

    color:#000000;
    font-size: 2vh;
}
.button2 {
    position: absolute;
    right:0%;

    width:10%;
    height:100%;
    background-color: #c4bbbb;

    color:#000000;
    font-size: 2vh;
}

/*左侧栏*/


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


.right_table {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: absolute;
    top: 2%;


    width: 90%;
    height: 30%;

    overflow-y: auto;

    background-color: #ffffff;
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