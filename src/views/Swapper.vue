<script setup>
import SwapBar from "@/components/SwapBar.vue";
import SwapSection from "@/components/SwapSection.vue";
</script>

<template>
  <v-main class="swapper-page">
    <SwapBar></SwapBar>
    <SwapSection></SwapSection>
  </v-main>
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
