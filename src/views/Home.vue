<script setup>
import HomeCard from '@/components/HomeCard.vue';
</script>

<template>
    <v-main class="home-page">
        <HomeCard></HomeCard>
    </v-main>
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