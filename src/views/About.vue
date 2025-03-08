<script setup lang="ts">
import AboutCard from "@/components/AboutCard.vue";
</script>

<template>
  <v-main class="about-page">
    <AboutCard />
  </v-main>
</template>

<style scoped>
.about-page {
  display: grid;
  align-items: center;
  justify-items: center;
  margin-top: 10px;
  gap: 10px;

  color: var(--dark);

  width: 100%;
}
</style>
