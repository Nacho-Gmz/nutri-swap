<script setup>
import Sidebar from "./components/Sidebar.vue";
</script>

<template>
  <v-app class="app">
    <Sidebar />
    <RouterView />
  </v-app>
</template>

<style>
:root {
  /* Light palette */
  --background-light: #abd1c6;
  --headline-light: #001e1d;
  --text-light: #0f3433;
  --component-bg-light: #004643;
  --component-text-light: #fffffe;

  /* Dark palette */
  --background: #004643;
  --headline: #fffffe;
  --text: #abd1c6;
  --component-bg: #e8e4e6;
  --component-text: #001e1d;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "DM Sans", sans-serif;
}

body {
  background: var(--primary);
}

button {
  cursor: pointer;
  appearance: none;
  border: none;
  outline: none;
  background: none;
}

.app {
  display: flex;
  flex: 1 1 0;
  /* padding: 2rem; */

  @media (max-width: 768px) {
    /* padding: 6rem; */
  }
}
</style>
