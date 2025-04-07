<template>
<div class="register">
    <p class="title">注册</p>
    <div class="input">
        <input type="text" placeholder="用户名" v-model = 'username' >
        <input type="password" placeholder="密码" v-model = 'password'>
        <input type="password" placeholder="确认密码" v-model = 'password2'>
        <input type="text" placeholder="邮箱" v-model = 'email'>
        <input type="text" placeholder="验证码" v-model = 'code'>
        <input type="text" placeholder="手机号" v-model = 'phone'>
    </div>
    <button class = 'sendcode' @click = 'sendcode'>发送验证码</button>
    <button class="register_button" @click = "register">注册</button>
    <div class='isregister' @click = "gologin">返回登录</div>

    <div class = "warning">
        <div class='warn1' v-show = "warn[0]">存在未填信息</div>
        <div class='warn2' v-show  = "warn[1]">用户姓名不得大于6个字符</div>
        <div class='warn3' v-show = "warn[2]">密码不一致</div>
    </div>

</div>

</template>

<script setup>

import { ref,inject} from 'vue'
const axios = inject('axios')

const username = ref('')
const password = ref('')
const password2 = ref('')
const email = ref('')
const code = ref('')
const phone = ref('')
const warn = ref([false,false,false,false])

async function sendcode()
{
    const response = await axios.post('/user/send_code/', {email : email.value})
    console.log(response)
}


async function register()
{   
    if (username.value.length < 1 || password.value.length < 1 || code.value.length < 1 || phone.value.length < 1){
        warn.value[0] = true
        console.log(warn[0])
        return
    }
    else{
        warn.value[0] = false
    }
    if(username.value.length > 6){
        warn.value[1] = true
        return
    }
    else{
        warn.value[1] = false
    }
    if(password.value != password2.value ){
        warn.value[2] = true
        return
    }
    else{
        warn.value[2] = false
    }
    response = await axios.post('/user/register_verify/', {
        username: username.value,
        password: password.value,
        email: email.value,
        code: code.value,
        phone: phone.value
    })
    console.log(response)

}

const isregister = ref(false)
const emit = defineEmits(['isregister'])
function gologin()
{
    emit('isregister',isregister)
}


</script>





<style scoped>
.register
{
    /*长宽设置 */
  width: 400px;
  height: 480px;

  /*居中设置*/
  position: absolute;
  top: 50%;
  left: 48%;
  transform: translate(-50%, -50%);

  /*背景设置*/
  border-radius: 10px;  
  box-shadow: 
  10px 10px 10px #3a4141,
  -10px -10px 10px #3a4141;


}
.title{
    text-align: center;
    margin-top: 2%;
    margin-bottom: 5%;
    font-size: 30px;
}

.input {
  width: 100%; /* 使输入框宽度自适应 */
  margin-bottom: 5%;
}

.input input {
  width: 80%; /* 输入框占满整个输入区域 */
  padding: 2%;
  margin-bottom: 3%; /* 输入框之间的间距 */
}

.email{
    width: 10%;
    padding: 10%;
}
.sendcode{
    width:20%;
    height:10%;
    font-size: 5%;
}
.register_button{
    width:15%;
    height:10%;
    font-size: 5%;

}


.warning {
  width: 100%; /* 警告信息宽度自适应 */
  margin-top: 10px;
}

.warn1, .warn2, .warn3 {
  padding: 10px;
  background-color: #ffcccc; /* 警告信息的背景颜色 */
  color: red; /* 警告信息的文字颜色 */
  margin-top: 5px; /* 警告信息之间的间距 */
  box-sizing: border-box;
}


</style>