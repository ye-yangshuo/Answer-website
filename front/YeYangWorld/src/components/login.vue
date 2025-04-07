<template>

  <div class="login">
    <p class="login_title">登录</p>
    <input type="text" placeholder="邮箱" class="login_email" v-model = "email">
    <input type="password" placeholder="密码" class="login_password" v-model = "password">
    <button class="login_button" @click = "login">登录</button>
    <div class="login_message" v-if="error">{{error}}</div>
    <div class="go_register" @click = "goregister">没有账号？去注册</div>
    <div class="get_password" @click = "getpassword">忘记密码？</div>
  </div>
  </template>
  
  
<script setup>

  import { ref,inject} from 'vue'
  const axios = inject('axios')

  const email = ref('')
  const password = ref('')
  const error = ref(null)
  
  async function login()
  {
    const response = await axios.post('/user/login_verify/',{
      email: email.value, password: password.value
    })
    console.log(response.data)
    if(response.data.status == 'success')
    {
      alert('登录成功')
      sessionStorage.setItem('accessToken',response.data.token) 
      console.log(sessionStorage.getItem('accessToken'))
      error.value = null
    }
    else
    {
      error.value = response.data.message
    }
  }

  const isregister = ref(true)
  const ispassword = ref(false)
  const emit = defineEmits(['isregister', 'ispassword'])
  function goregister()
  {
    emit('isregister', isregister)
  }
  function getpassword () 
  {
    window.location.href = '/getpassword'
  }
  </script>





<style>

.login {
  
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

.login_title {    
    /* 字体设置 */
    font-size: 40px;
    font-weight: bold;
    color: #2e3335;
    margin-bottom: 5%;
}

.login_email, .login_password{
    /* 长宽设置 */
    width: 300px;
    height: 40px;

    /* 边框设置 */
    border: 1px solid #e0ecec;
    border-radius: 20px;

    /* 间隔设置 */
    margin: 15px;
    
    /*背景设置*/
    background-color: #d8f0f0;

    /* 字体设置 */
    font-size: 20px;    
    font-weight: bold;
    color: #1b2222;
}

.login_button {
    /* 长宽设置 */
    width: 80px;
    height: 50px;

    /* 间隔设置 */
    margin : 8%;

    /* 颜色设置 */
    background-color: #26f0f0;  

    /* 字体设置 */
    color :#000000; 
    font-size :  17px;
}

.login_message{
    /* 位置设置 */
    position: absolute;
    top: 55%;
    left: 27%;
    transform: translate(-50%, -50%);

    /* 字体设置 */
    font-size: 15px;    
    font-weight: bold;
    color: #ff0000;
}

.go_register {

  /*长宽设置*/
  width : 100px;
  height: 50px;
  /*位置设置*/
  position: absolute;
  top: 80%;
  left: 15%;
  transform: translate(-50%, -50%);

  /*间隔设置*/
  margin : 7%;
  /*字体设置*/
  font-size: 15px;    
  font-weight: bold;
  color: #4ccaca;
}

.get_password{
  /*长宽设置*/
  width : 80px;
  height: 50px;
  /*位置设置*/
  position: absolute;
  top: 80%;
  left: 70%;
  transform: translate(-50%, -50%);
  /*间隔设置*/
  margin : 7%;
  /*字体设置*/
  font-size: 15px;    
  font-weight: bold;
  color: #4ccaca;
}

</style>
