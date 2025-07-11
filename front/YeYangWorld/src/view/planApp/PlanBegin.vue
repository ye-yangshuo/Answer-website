<template>
    <navigate class="navigate"></navigate>
    <div class="planbegin">
        <div class="left">
            <Calendar @dayclick='handleSelect' ref="calendar" :attributes="attributes" expanded transparent borderless
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
                <button class="create" @click="createPlan">创建计划</button>
                <button class="commit" @click="commitPlan">提交</button>
            </div>


            <div class="right_complete">

                <div class="incompleted" v-if="showIncompleted">
                    <div class='title'>正在完成</div>

                    <div class="plan" v-for="(incom, incom_index) in incompleted[selectedTime]" :key="incom.id">
                        <div class="content">{{ incom.content }}</div>
                        <button class="delete" @click="deletePlan(incom_index)">删除</button>
                        <button class="complete" @click="completePlan(incom, incom_index)">完成</button>
                    </div>

                </div>


                <div class="completed" v-if="showCompleted">
                    <div class='title'>已完成</div>

                    <div class="plan" v-for="(com, com_index) in completed[selectedTime]" :key="com.id">
                        <div class="content">{{ com.content }}</div>
                        <button class="back" @click="backPlan(com, com_index)" v-if="showIncompleted">回退</button>
                    </div>

                </div>



            </div>
        </div>
    </div>
</template>


<script setup>
import { ref, inject, watch, onMounted } from 'vue';
const axios = inject('axios');

import { Calendar } from 'v-calendar';
import 'v-calendar/style.css';
import { v4 as uuidv4 } from 'uuid';
import { ElMessage } from 'element-plus';

/*
变量管理
calendar: 用于存储日历组件的引用，以便后续操作。

nowDate: 存储当前日期，用于高亮显示。

selectedDate: 存储用户选择的日期。

selectedTime: 存储用户选择的日期，字符串格式，用于显示和提交。

attributes: 用于配置日历组件，高亮显示今天和选中的日期。

planContent: 存储用户输入的计划内容。

incompleted: 存储所有未完成的计划，以日期为键，计划列表为值。

completed: 存储所有已完成的计划，以日期为键，计划列表为值。

id: 存储唯一ID，用于标识每个计划。

showIncompleted 和 showCompleted: 控制是否显示未完成和已完成的计划列表。
*/

const calendar = ref(null);
const nowDate = ref(new Date());
const selectedDate = ref(new Date());
const selectedTime = ref(getTodayDate());
const attributes = ref([
    { key: 'today', highlight: { fillMode: 'solid' }, dates: nowDate.value },
]);
const planContent = ref('');
//格式：{date: [{id: 1, content: '学习'}, {···}], ···}
const incompleted = ref({});
//格式：{date: [{id: 1, content: '学习'}, {···}], ···}
const completed = ref({});
const id = ref(0);
const showIncompleted = ref(true);
const showCompleted = ref(true);


/*
函数管理

getTodayDate: 获取当前日期，并格式化为字符串。

moveToday: 将日历移动到今天日期，并更新相关变量。

handleSelect: 处理用户选择日期的操作，更新选中日期和显示状态。

createPlan: 创建新计划，并进行输入验证。将计划添加到未完成计划列表中。

deletePlan: 删除未完成的计划。

completePlan: 将未完成的计划标记为已完成，并从未完成列表中移除。

backPlan: 将已完成的计划回退到未完成状态。

commitPlan: 提交已完成的计划到服务器，并进行输入验证。

loadPlan: 从服务器加载已完成的计划，并更新已完成计划列表。

onMounted(loadPlan): 组件挂载时加载计划。

watch(selectedTime): 监听选中日期的变化，并根据日期调整显示状态。
*/

function getTodayDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

function moveToday() {
    calendar.value.move(nowDate.value);
    attributes.value = [{ key: 'today', highlight: { fillMode: 'solid' }, dates: nowDate.value }];
    selectedTime.value = getTodayDate();
}

function handleSelect(value) {
    selectedDate.value = new Date(value.id);
    attributes.value = [{ key: 'selected', highlight: { fillMode: 'outline' }, dates: selectedDate.value }];
    selectedTime.value = value.id;
}

function createPlan() {
    //检查
    if (planContent.value === '') {
        ElMessage({
            message: '请输入计划内容',
            type: 'warning',
        });
        return;
    }
    if (selectedTime.value < getTodayDate()) {
        ElMessage({
            message: '不能添加过去日期的计划',
            type: 'warning',
        });
        return;
    }
    if (!incompleted.value[selectedTime.value]) {
        incompleted.value[selectedTime.value] = [];
    }

    //执行
    id.value = uuidv4();
    incompleted.value[selectedTime.value].push({ id: id.value, content: planContent.value });
    planContent.value = '';
}

function deletePlan(incomIndex) {
    incompleted.value[selectedTime.value].splice(incomIndex, 1);
}

function completePlan(incom, incomIndex) {
    //检查
    if (!completed.value[selectedTime.value]) {
        completed.value[selectedTime.value] = [];
    }
    //执行
    completed.value[selectedTime.value].push(incom);
    incompleted.value[selectedTime.value].splice(incomIndex, 1);
}

function backPlan(com, comIndex) {
    //检查
    if (!incompleted.value[selectedTime.value]) {
        incompleted.value[selectedTime.value] = [];
    }
    //执行
    incompleted.value[selectedTime.value].push(com);
    completed.value[selectedTime.value].splice(comIndex, 1);
}

async function commitPlan() {
    //检查
    if (selectedTime.value < getTodayDate()) {
        alert("不能提交过去日期的计划")
        return;
    }
    if (completed.value[selectedTime.value] == undefined) {
        ElMessage.warning("请完成计划")
    }
    //执行
    const completedContent = [];
    for (const com of completed.value[selectedTime.value]) {
        completedContent.push(com.content);
    }
    const contentString = completedContent.join('\n');
    const response = await axios.post('/plan/commit_plan/', {
        selectedTime: selectedTime.value,
        planContent: contentString,
    });
}

async function loadPlan() {
    const response = await axios.get('/plan/get_plan/');
    const plans = response.data.data;

    for (const plan of plans) {
        if (!completed.value[plan.create_time]) {
            completed.value[plan.create_time] = [];
        }
        const contentArr = plan.content.split('\n');
        for (const content of contentArr) {
            id.value = uuidv4();
            completed.value[plan.create_time].push({ id: id.value, content: content });
        }
    }
}
onMounted(loadPlan);

watch(selectedTime, (newVal, oldVal) => {
    if (newVal < getTodayDate()) {
        showCompleted.value = true;
        showIncompleted.value = false;
    } else {
        showCompleted.value = true;
        showIncompleted.value = true;
    }
});




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