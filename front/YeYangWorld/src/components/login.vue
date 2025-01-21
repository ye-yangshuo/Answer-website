


<template>

  <div class="login">

    <p class="login_title">登录</p>

    <div class="login_form" >
      <input type="text" placeholder="用户名" class="login_username" v-model = "username">
      <input type="password" placeholder="密码" class="login_password" v-model = "password">
      <button class="login_button" @click = "login">登录</button>
    </div>

    

  </div>


</template>


<script setup>
import { ref } from 'vue'

const username = ref('')
const password = ref('')

//TODO 脚本编写
const login = () => {$axios.post('/api/login', {username: username.value, password: password.value}
    ).then(response => alert(response.data))}



</script>



<style scoped>

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
    
}


</style>