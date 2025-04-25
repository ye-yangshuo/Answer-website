<template>
    <navigate></navigate>

  <div class="readbegin">
    <div class="left">a</div>
    <div class="main">b</div>
  </div>

</template>

<script setup>


</script>

<style scoped>
.readbegin {
    background-color: #E4E2E2;
    width: 1200px;
    height: 900px;
    display: flex;
    flex-direction: row;
}
.left{
    position: sticky;
    top:70px;
    width:120px;
    height: 500px;
    background-color: #ffffff;
}
.main{
    width:100%;
    height: 900px;
    background-color: #ffffff;
    margin-left :  10px;

}



</style>