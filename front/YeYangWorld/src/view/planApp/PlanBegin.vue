<template>
    <navigate class="navigate"></navigate>
    <div class="planbegin">
        <div class="left">
            <Calendar  class='calendar' expanded transparent borderless  title-position="left" />
        </div>
        <div class="right">

        </div>
        </div>
</template>

<script setup>
import { Calendar } from 'v-calendar';
import 'v-calendar/style.css';

</script>

<style scoped>
.navigate{
    margin-bottom: 0;
}
.planbegin{
width:1200px;
height:900px;
background-color: #ffffff;
display:flex;
flex-direction: row;
}
.left{
    width:35%;
    height:100%;
    border-right: #383636 solid 1px;
}
.calendar{

}

</style>