<template>
    <el-container class="container">
      <el-header class="header">Header</el-header>
      <el-aside width="200px">Aside</el-aside>
      <el-main>Main</el-main>
      <el-footer>Footer</el-footer>

    </el-container>
    

<el-button class='button' type="primary">主要按钮</el-button>

</template>


<script setup>
</script>


<style scoped>
.container{
  width: 100%;
  height: 100%;
  background-color: #f5f5f5;
}
.header{
  background-color: #409EFF;
}
.button{
  margin-top: 20px;
  margin-left: 20px;
}

</style>