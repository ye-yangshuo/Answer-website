<template>
<div class="page">
    <div class="left">
        <slot name="left"></slot>
    </div>

    <div class="main">
        <slot name="main"></slot>
    </div>

    <div class="right">
        <slot name="right"></slot>
    </div>

</div>

</template>

<style scoped>
/*页面布局*/
.page {
  background-color: #E4E2E2;
  width: 1200px;
  height: 900px;
  display: flex;
  flex-direction: row;
}

.left {
  position: sticky;
  top: 70px;
  width: 200px;
  height: 500px;
  background-color: #E4E2E2;

}

.main {
  width: 100%;
  height: 900px;
  background-color: #ffffff;
  margin-left: 20px;
  margin-right: 20px;

}

.right {
  width: 200px;
  height: 500px;
  right: 0;

  background-color: #E4E2E2;
}
</style>