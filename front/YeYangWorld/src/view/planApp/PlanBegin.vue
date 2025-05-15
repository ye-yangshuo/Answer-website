<template>
    <navigate class="navigate"></navigate>
    <div class="planbegin">
        <div class="left">
            <Calendar @dayclick='handleselect' ref="calendar" :attributes="attributes" expanded transparent borderless
                title-position="left">
                <template #footer>
                    <div class="w-full px-4 pb-3">
                        <button
                            class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold w-full px-3 py-1 rounded-md"
                            @click="moveToday">
                            Today
                        </button>
                    </div>
                </template>
            </Calendar>
        </div>


        <div class="right">

            <div class="right_top">
                <div class="now_days">连续完成天数</div>
                <div class="history_days">历史连续完成天数</div>
            </div>


            <div class="right_create">
                <div class="now_time">{{ selectedTime }}</div>
                <input type="text" class="input" placeholder="请输入计划">
                <button class="button">创建计划</button>
            </div>


            <div class="right_complete">

                <div class="incompleted">
                    <div class='title'>正在完成</div>
                    <div class="content"></div>
                </div>

                <div class="completed">
                    <div class='title'>已完成</div>
                    <div class="content"></div>
                </div>

            </div>


        </div>
    </div>
</template>


<script setup>
import { Calendar } from 'v-calendar';
import 'v-calendar/style.css';
import { ref } from 'vue';

const nowDate = ref(new Date());
const selectedDate = ref(new Date());
const calendar = ref(null);
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



/*右侧*/
.right {
    width: 65%;
    height: 100%;
    background-color: #ffffff;
}

/*顶部 */
.right_top {
    height: 40px;
    display: flex;
    flex-direction: row;
    border-bottom: #4a4949 solid 1px;
    align-items: center;
    color: #383636;
    font-size: 20px;
}

.now_days {
    width: 50%;
    margin-left: 20px;
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
    flex-direction: row;
    color: #383636;
    border-top: #383636 solid 1px;
}

.incompleted {
    width: 50%;
    border-right: #383636 solid 1px;
}

.completed {
    width: 50%;
}

.title {
    border-bottom: #383636 solid 1px;
}
</style>