<template>

  <div class="login">
    <p class="login_title">登录</p>
    <div class="login_form" >
      <input type="text" placeholder="用户名" class="login_username" v-model = "username">
      <input type="password" placeholder="密码" class="login_password" v-model = "password">
      <button class="login_button" @click = "login">登录</button>
      <div class="go_register" @click = "goregister">没有账号？去注册</div>
      <div class="get_password" @click = "getpassword">忘记密码？</div>
    </div>

  </div>
  </template>
  
  
<script setup>

  import { ref,inject} from 'vue'

  const axios = inject('axios')
  
  const username = ref('')
  const password = ref('')

  const isregister = ref(true)
  const ispassword = ref(false)
  const emit = defineEmits(['isregister', 'ispassword'])


  const login = () => {
    axios.post('/user/login_verify/', {
      username: username.value,
      password: password.value
    }).then(response => {
      console.log(response.data)
      if (response.data.code === 200) {
        alert('登录成功')
      } 
      else {
        alert('用户名或密码错误')
      }
    }).catch(error => {
      console.log(error)
    })
  }
  
  const goregister = () => {
   emit('isregister', isregister)
  }

  const getpassword = () => {
    window.location.href = '/getpassword'
  }

  
  
  
  </script>





<style>

.login {
  
  /*长宽设置 */
  width: 400px;
  height: 500px;

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
}


.login_form {
    /* 长宽设置 */
    width: 400px;
    height: 300px;

    /* 居中设置 */
    position: absolute;
    top: 54%;
    left: 50%;
    transform: translate(-50%, -50%);
}


.login_username, .login_password{
    /* 长宽设置 */
    width: 300px;
    height: 40px;

    /* 边框设置 */
    border: 1px solid #e0ecec;
    border-radius: 20px;

    /* 间隔设置 */
    margin: 20px;
    
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
    margin : 7%;

    /* 颜色设置 */
    background-color: #26f0f0;  

    /* 字体设置 */
    color :#000000; 
    font-size :  17px;
}

.go_register {

  /*长宽设置*/
  width : 100px;
  height: 50px;
  /*位置设置*/
  position: absolute;
  top: 90%;
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
  top: 90%;
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
