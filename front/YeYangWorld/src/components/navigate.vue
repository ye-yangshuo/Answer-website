<template>
  <div class = "top_navigation">
    <a class="logo" href = 'http://localhost:5173/home'> 
    </a>
    <div class="nav-container">
      <router-link class='nav-item home' to="/home">首页</router-link> 
      <router-link class='nav-item answer' to="/datibegin/questiontype1">答题</router-link>
      <router-link class='nav-item read' to="/readbegin">阅读</router-link>
      <router-link class='nav-item plan' to="/blogbegin">博客</router-link>
      <router-link class="nav-item tools" to="/toolbegin">工具</router-link>
      <router-link class="nav-item plan" to="/planbegin">计划</router-link>
    </div>
    <router-link class='my' to="/my"></router-link>
    </div>
  </template>


<script setup>
</script>


<style scoped>
.top_navigation{
    position: sticky;
    top: 0;
    left: 0;
    width: 100%;
    height: 60px;
    background-color: #ffffff;
    z-index: 1000;
    margin-bottom: 20px;

}
.logo{
  width: 8%;
  height: 100%;
  position: absolute;
  left:2%;

  background-image: url('/src/assets/userApp/image.png');
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
  width: 60%; 
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
  background-image: url('/src/assets/userApp/personal.png');
  background-repeat: no-repeat;
  background-size: 40%;
  background-position: center;
}

</style>
