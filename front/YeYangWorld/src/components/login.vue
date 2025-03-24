<template>
  <div class="background">
  </div>

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
  import { ref,inject} from 'vue'

  const axios = inject('axios')
  
  const username = ref('')
  const password = ref('')



  const login = () => {
    axios.post('/user/login_verify/', {
      username: username.value,
      password: password.value
    }).then(response => {
      console.log(response.data)
      if (response.data.code === 200) {
        alert('登录成功')
      } else {
        alert('用户名或密码错误')
      }
    }).catch(error => {
      console.log(error)
    })
  }
  

  
  
  
  </script>





<style>
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
    background-color: #b7e8e8;  
}

</style>
