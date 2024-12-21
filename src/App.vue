<script setup>
import Sidebar from './components/Sidebar.vue'
</script>

<template>
    <div class="app">
        <Sidebar />
        <RouterView />
    </div>
</template>

<style>
:root {
    --light: #fffffe;
    --light-alt: #abd1c6;
    --dark: #001e1d;
    --dark-alt: #0f3433;

    --primary: #abd1c6;
    --secondary: #004643;

    --grey: #757575;
    --sidebar-width: 300px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'DM Sans', sans-serif;
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