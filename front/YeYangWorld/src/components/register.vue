<template>

<div class="background">
</div>

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
    </div>
    <button class="button" @click = "register">注册</button>
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

const sendcode = () => {
    axios.post('/sendcode/', {
        email : email.value
    }).then(res => {
        console.log(res)
    })
}
const register = () => {
    if(username.value.length > 6){
        username_ok.value = true
        return
    }
    if(password.value != password2.value){
        password2_ok.value = true
        return
    }

    axios.post('/register_verify/', {
        username: username.value,
        password: password.value,
        email: email.value,
        code: code.value,
        phone: phone.value
    }).then(res => {
        if(res.data.code == 200){
            alert('注册成功')
            window.location.href = '/login'
        }else{
            alert('注册失败')
        }
    })
}


</script>





<style scoped>

.background {  
    width: 100%;
    height: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;

    background-image: url("../public/background_img.jpeg");

    /* 背景图垂直、水平均居中 */
    background-position: center center;
    /* 背景图不平铺 */
    background-repeat: no-repeat;
    /* 当内容高度大于图片高度时，背景图像的位置相对于viewport固定 */
    background-attachment: fixed;
    /* 让背景图基于容器大小伸缩 */
    background-size: cover;
    /* 设置背景颜色，背景图加载过程中会显示背景色 */
    background-color: #464646;
}



</style>