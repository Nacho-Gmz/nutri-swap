<script setup>
import HomeCard from '@/components/HomeCard.vue';


</script>

<template>
    <div class="home-page">
        <h1>NutriSwap</h1>
        <HomeCard></HomeCard>
    </div>
</template>

<style scoped>
.home-page {
    display: grid;
    align-items: center;
    justify-items: center;

    color: var(--dark);

    width: 100vw;
}
</style>