<template>
    <navigate class="navigate"></navigate>
    <div class="planbegin">
        <div class="left">
            <Calendar @dayclick='handleselect' ref="calendar" :attributes="attributes" expanded transparent borderless
                title-position="left">
                <template #footer>
                    <div class="w-full px-4 pb-3">
                        <button
                            class="bg-indigo-600 hover:bg-indigo-700 `text-white font-bold w-full px-3 py-1 rounded-md"
                            @click="moveToday">
                            Today
                        </button>
                    </div>
                </template>
            </Calendar>

            <div class="left_bottom">
                <div class="conpleted_days">已完成天数</div>
                <div class="now_days">连续完成天数</div>
                <div class="history_days">历史连续完成天数</div>
            </div>

        </div>


        <div class="right">

            <div class="now_time">{{ selectedTime }}</div>


            <div class="right_create">
                <input class="input" type="text" placeholder="请输入计划" v-model="planContent"></input>
                <button class="create" @click="createplan">创建计划</button>
                <button class="commit" @click="commit">提交</button>
            </div>


            <div class="right_complete">

                <div class="incompleted" v-if="showIncompleted">
                    <div class='title' >正在完成</div>

                    <div class="plan" v-for="(incom, incom_index) in incompleted[selectedTime]" :key="incom.id">
                        <div class="content">{{ incom.content }}</div>
                        <button class="delete" @click="deleteplan(incom_index)">删除</button>
                        <button class="complete" @click="completeplan(incom, incom_index)">完成</button>
                    </div>

                </div>


                <div class="completed" v-if="showCompleted">
                    <div class='title' >已完成</div>

                    <div class="plan" v-for="(com, com_index) in completed[selectedTime]" :key="com.id">
                        <div class="content">{{ com.content }}</div>
                        <button class="back" @click="backplan(com, com_index)">回退</button>
                    </div>

                </div>



            </div>
        </div>
    </div>
</template>


<script setup>
import { ref, inject, watch } from 'vue';
const axios = inject('axios');

import { Calendar } from 'v-calendar';
import 'v-calendar/style.css';
import { v4 as uuidv4 } from 'uuid';

const calendar = ref(null);
const nowDate = ref(new Date());
const selectedDate = ref(new Date());
const selectedTime = ref(getTodayDate());
const attributes = ref([
    { key: 'today', highlight: { fillMode: 'solid' }, dates: nowDate.value },
])

//获取特定格式的现在日期
function getTodayDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}
//移动到今天,并显示今天
function moveToday() {
    calendar.value.move(nowDate.value);
    selectedTime.value = getTodayDate();
    attributes.value[1] = {};
}
//选择日期,并显示日期
function handleselect(value) {
    // console.log(value)
    selectedDate.value = new Date(value.id)
    attributes.value[1] = { key: 'selected', highlight: { fillMode: 'outline' }, dates: selectedDate.value }
    selectedTime.value = value.id
}

const planContent = ref('')
const incompleted = ref({})
const completed = ref({})
const id = ref(0)
function createplan() {
    if (incompleted.value[selectedTime.value] == undefined) {
        incompleted.value[selectedTime.value] = []
    }
    id.value = uuidv4()
    incompleted.value[selectedTime.value].push({ id: id.value, content: planContent.value })
    planContent.value = ''
    // console.log(incompleted.value)
}
function deleteplan(incom_index) {
    incompleted.value[selectedTime.value].splice(incom_index, 1)
    //console.log(incompleted.value)
}
function completeplan(incom, incom_index) {
    if (completed.value[selectedTime.value] == undefined) {
        completed.value[selectedTime.value] = []
    }
    completed.value[selectedTime.value].push(incom)
    incompleted.value[selectedTime.value].splice(incom_index, 1)
    // console.log(incom, icom_index,incompleted.value[selectedTime.value],completed.value[selectedTime.value])
}
function backplan(com, com_index) {
    if (incompleted.value[selectedTime.value] == undefined) {
        incompleted.value[selectedTime.value] = []
    }
    incompleted.value[selectedTime.value].push(com)
    completed.value[selectedTime.value].splice(com_index, 1)
    // console.log(com, com_index,incompleted.value[selectedTime.value],completed.value[selectedTime.value])
}

let completed_content = []
async function commit() {

    for (const com of completed.value[selectedTime.value]) {
        completed_content.push(com.content)
    }
    //将数组转换为字符串且换行
    const contentString = completed_content.join('\n');
    // console.log(contentString)

    const response = await axios.post('/plan/commit_plan/', {
        plan_content: contentString
    })
    console.log(response)
}

const showIncompleted = ref(true)
const showCompleted = ref(true)

watch(selectedTime,function(newVal, oldVal){
    if (newVal< getTodayDate()) {
        showCompleted.value = true
        showIncompleted.value = false

    }
    else if (newVal == getTodayDate())  {
        showCompleted.value = true
        showIncompleted.value = true
    }
    else {
        showCompleted.value = false
        showIncompleted.value = true
    }

}
)

</script>



<style scoped>
.navigate {
    margin-bottom: 0;
}

/*主页面 */
.planbegin {
    width: 1200px;
    height: 700px;
    background-color: #ffffff;
    display: flex;
    flex-direction: row;
}



/*左侧*/
.left {
    width: 35%;
    height: 100%;
    border-right: #383636 solid 1px;
}

.left_bottom {
    height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;
    border-top: #4a4949 solid 1px;
    color: #383636;
    font-size: 20px;
}


/*右侧*/
.right {
    width: 65%;
    height: 100%;
    background-color: #ffffff;
}

.now_time {
    border-bottom: #383636 solid 1px;
    height: 45px;
    color: #000000;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}

/*创建*/
.right_create {
    height: 60px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    color: #383636;
    margin-top: 15px;
    align-items: center;

}

/*完成与未完成 */
.right_complete {
    margin-top: 15px;
    height: 570px;
    display: flex;
    flex-direction: column;
    color: #383636;
}

.incompleted {
    min-height: 50%;
    border-top: #383636 solid 1px;
    overflow-y: auto;
}

.completed {
    min-height: 50%;
    border-top: #383636 solid 1px;
    overflow-y: auto;
}

.title {
    border-bottom: #383636 solid 1px;
}

.plan {
    display: flex;
    flex-direction: row;
    min-height: 40px;
    border-bottom: #383636 solid 1px;
}
</style>