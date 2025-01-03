<script setup>
import SwapBar from '@/components/SwapBar.vue';

</script>

<template>
    <main class="swapper-page">
        <h1>Intercambio</h1>
        <SwapBar></SwapBar>
    </main>
</template>

<style scoped>
.swapper-page {
    display: grid;
    align-items: center;
    justify-items: center;

    color: var(--dark);

    width: 100vw;
}
</style>