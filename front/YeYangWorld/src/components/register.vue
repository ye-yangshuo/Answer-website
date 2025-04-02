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
        <button class = 'sendcode' @click = 'sendcode'>发送验证码</button>
        <button class="button" @click = "register">注册</button>
        <div class='isregister' @click = "gologin">返回登录</div>
    </div>

    <div class = "warning">
        <p class='warn1' v-show = "username_ok">用户姓名不得大于6个字符</p>
        <p class='warn2' v-show  = "password2_ok">密码不一致</p>
        <p class='warn3' v-show = "code_ok">验证码错误</p>
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

const username_ok = ref(false)
const password2_ok = ref(false)
const code_ok = ref(false)

const isregister = ref(false)
const emit = defineEmits(['isregister'])

async function sendcode()
{
    const response = await axios.post('/user/send_code/', {email : email.value})
    console.log(response)
}



const register = () => {

    if(username.value.length > 6){
        username_ok.value = true
        return
    }
    else{
        username_ok.value = false
    }
    
    if(password.value != password2.value ){
        password2_ok.value = true
        return
    }
    else{
        password2_ok.value = false
    }

    axios.post('/user/register_verify/', {
        username: username.value,
        password: password.value,
        email: email.value,
        code: code.value,
        phone: phone.value
    }).then(res => {
        console.log(res)
    })
}

const gologin = () => {
    emit('isregister',isregister.value)
}


</script>





<style scoped>



</style>