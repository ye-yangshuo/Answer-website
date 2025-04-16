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

                    <div class="main_collect" @click="collect">收藏</div>

                    <div class="main_question" >{{now_question}}</div>

                    <div class="main_options">
                        <div class="optionA" >
                            <div class="optionA_title">A</div>
                            <div class="optionA_content">{{now_options[0]}}</div>
                        </div>
                        <div class="optionB">
                            <div class="optionB_title">B</div>
                            <div class="optionB_content">{{now_options[1]}}</div>
                        </div>
                        <div class="optionC">
                            <div class="optionC_title">C</div>
                            <div class="optionC_content">{{now_options[2]}}</div>
                        </div>
                        <div class="optionD">
                            <div class="optionD_title">D</div>
                            <div class="optionD_content">{{now_options[3]}}</div>
                        </div>
                    </div>

                    <div class="main_analysis">解析：{{now_explanation}}</div>

                </div>

                <div class="main_bottom">
                    <button class="main_button" @click="next_question">下一题</button>
                    <input class="main_note" type="txet" placeholder="笔记" v-model="now_note"></input>
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

import { onBeforeMount, ref ,inject} from 'vue'
const axios = inject('axios')

const now_question = ref('')
const now_options = ref([])
const now_explanation = ref('')
const now_answer = ref('')
const now_note = ref('')

const next_question = ref('')
const next_options = ref([])
const next_explanation = ref('')
const next_answer = ref('')


async function getproblem(){
    const response = await axios.get('/dati/get_problem/')
    const data = response.data
    const now_problem = data.now_problem
    const next_problem = data.next_problem

    
    now_question.value = now_problem.question
    now_options.value = [now_problem.option_a, now_problem.option_b, now_problem.option_c, now_problem.option_d]
    now_answer.value = now_problem.answer
    now_explanation.value = now_problem.explanation
    console.log(now_answer.value)

    next_question.value = next_problem.question
    next_options.value = [next_problem.option_a, next_problem.option_b, next_problem.option_c, next_problem.option_d]
    next_answer.value = next_problem.answer
    next_explanation.value = next_problem.explanation

}
onBeforeMount(getproblem)

async function submitnote(){
    const response = await axios.post('/dati/submit_note/', {
        note: now_note.value
    })
    const data = response.data
    console.log(data)
}

async function submitanswer() {
    const response = await axios.post('/dati/submit_answer/', {
        answer: now_answer.value
    })
    const data = response.data
    console.log(data)

}
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
.main_collect{
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
    left:5%;

    width:9%;
    height:9%;  

    background-color: #8da9f1;
    color:#000000;
    font-size: 2vh;
    text-align: center;
}
.main_note{
    position:absolute;
    top:80%;
    left:22%;

    width:70%;
    height:7%;

    background-color: #ffffff;
    color:#000000;
    font-size: 4vh;
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