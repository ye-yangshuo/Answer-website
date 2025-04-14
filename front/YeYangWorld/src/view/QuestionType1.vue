<template>
    <div class="questiontype1">

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

                    <div class="main_collection">收藏</div>

                    <div class="main_question">{{question}}</div>

                    <div class="main_options">
                        <div class="optionA" >
                            <div class="optionA_title">A</div>
                            <div class="optionA_content">{{options[0]}}</div>
                        </div>
                        <div class="optionB">
                            <div class="optionB_title">B</div>
                            <div class="optionB_content">{{options[1]}}</div>
                        </div>
                        <div class="optionC">
                            <div class="optionC_title">C</div>
                            <div class="optionC_content">{{options[2]}}</div>
                        </div>
                        <div class="optionD">
                            <div class="optionD_title">D</div>
                            <div class="optionD_content">{{options[3]}}</div>
                        </div>
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

import { ref } from 'vue'
const question = ref('属于国家一类保护动物的是？')
const options = ref(['熊猫','大熊猫','熊猫熊','熊猫猫'])
const analysis = ref('属于国家一类保护动物的是？')

</script>

<style scoped>
.questiontype1 {
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
    height:75%;
    background-color: #ffffff;

    display: flex;
    flex-direction: column;
    gap:7%;
    overflow-y :auto;
}
.main_title{
    position:relative;
    top:4%;
    left:2%;

    width:10%;
    height:7%;
    margin-bottom: 2%;

    font-size: 3vh;
    text-align: center;
    background-color: #000000;
}
.main_collection{
    position: absolute;
    top:4%;
    right:6%;

    color: #000000;
    font-size: 20px;
}
.main_question{
    position:relative;
    left:7%;
    width:87%;

    color: #000000;
    font-size: 20px;
    text-align: left;
}
.main_options{
    position:relative;
    left:7%;
    width:80%;

    font-size: 20px;
    color:#000000;
    text-align: left;

    display: flex;
    flex-direction:column;
}
.optionA, .optionB, .optionC, .optionD{
    margin-bottom: 3%;
    display: flex;
    flex-direction: row;
}
.optionA_title, .optionB_title, .optionC_title, .optionD_title{
    border:1px solid #000000;
    border-radius: 50%;
    width:5%;
    text-align: center;
    margin-right: 2%;
}
.main_analysis{
    position:relative;
    left:7%;
    width:80%;

    font-size: 20px;
    color:#000000;
    text-align: left;
}




.main_button{
    position:absolute;
    top:79%;
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
    left:30%;

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
    top: 2%;
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