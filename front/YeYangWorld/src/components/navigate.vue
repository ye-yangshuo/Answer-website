<template>
  <div class = "top_navigation">
    <a class="logo" href = 'http://localhost:5173/home'> 
    </a>
    <div class="nav-container">
      <router-link class='nav-item home' to="/home">首页</router-link> 
      <router-link class='nav-item answer' to="/questiontype1">答题</router-link>
      <router-link class='nav-item read' to="/read">阅读</router-link>
      <router-link class='nav-item plan' to="/plan">计划</router-link>
    </div>
    <router-link class='my' to="/my"></router-link>
    </div>
  </template>


<script setup>
</script>


<style scoped>
.top_navigation{
  width: 100%;
  height: 10%;
  background-color: #ffffff;

  position: fixed;
  top: 0;
  left: 0;

  z-index: 9999;
}
.logo{
  width: 8%;
  height: 100%;
  position: absolute;
  left:2%;

  background-image: url('../public/image.png');
  background-size: 60%;
  background-repeat: no-repeat;
  background-position: center;
}

.nav-container {
  display: flex;
  justify-content: space-between; 
  align-items: center; 

  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); 
  width: 50%; 
}
.nav-item {
  font-size: 3vh;
  color: #000000;
  text-decoration: none;
}

.my {
  position:absolute;
  left:92%;
  width: 7%;
  height: 100%;
  background-image: url('../public/personal.png');
  background-repeat: no-repeat;
  background-size: 40%;
  background-position: center;
}

</style>
