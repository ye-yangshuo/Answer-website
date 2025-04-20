<template>
    <div class="ReadBegin">
        <threelayout>
            <template v-slot:header><navigate></navigate></template>
            <template v-slot:left></template>
            <template v-slot:right></template>
            <template v-slot:main></template>
        </threelayout>
    </div>
</template>

<script setup>
import threelayout from '/src/components/threelayout.vue'
import navigate from '/src/components/navigate.vue'
</script>

<style scoped>
.ReadBegin {
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;

}
</style>