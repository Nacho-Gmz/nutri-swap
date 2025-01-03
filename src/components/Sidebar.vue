<script setup>
import { ref } from 'vue';

const is_expanded = ref(false);

const ToggleMenu = () => {
    is_expanded.value = !is_expanded.value;
}

</script>

<template>
    <aside :class="[is_expanded ? 'is-expanded' : '']">
        <div class="logo">
            <img class="logo-img" src="../assets/images/logo.png" alt="">
            <span class="text">NutriSwap</span>
        </div>

        <div class="menu-toggle-wrap">
            <button class="menu-toggle" @click="ToggleMenu">
                <span class="material-icons">menu</span>
            </button>
        </div>
        <h3>Menu</h3>
        <div class="menu">
            <RouterLink class="button" to="/">
                <span class="material-icons">home</span>
                <span class="text">Inicio</span>
            </RouterLink>
            <RouterLink class="button" to="/swapper">
                <span class="material-icons">sync</span>
                <span class="text">Intercambio</span>
            </RouterLink>
            <RouterLink class="button" to="/about">
                <span class="material-icons">info</span>
                <span class="text">Acerca de</span>
            </RouterLink>
        </div>
    </aside>
</template>

<style scoped>
aside {
    display: flex;
    flex-direction: column;
    background-color: var(--secondary);
    color: var(--light);
    width: calc(2rem + 32px);
    overflow: hidden;
    min-height: 100vh;
    padding: 1rem;
    transition: 0.2s ease-in-out;
    position: fixed;
}

aside .logo {
    display: flex;
    margin-bottom: 0.7rem;
    align-items: center;
    position: relative;
    top: 0;
    transition: 0.2s ease-in-out;
}

aside .logo img {
    width: 2rem;
}

aside .logo .text {
    color: var(--light);
    font-size: 1rem;
}

aside .menu-toggle-wrap {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 0;
    position: relative;
    top: 0;
    transition: 0.2s ease-in-out;
}

aside .menu-toggle-wrap .menu-toggle {
    transition: 0.5s ease-in-out;
}

aside .menu-toggle-wrap .menu-toggle .material-icons {
    font-size: 2rem;
    color: var(--primary);
    transition: 0.5s ease-out;
}

aside .menu-toggle-wrap .menu-toggle:hover .material-icons {
    color: var(--light);
    transform: translateX(0.5rem);
}

aside h3,
aside .logo .text,
aside .button .text {
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
}

aside h3 {
    color: var(--light);
    font-size: 1rem;
    margin-bottom: 0;
    text-transform: uppercase;
}

aside .menu {
    margin: 0 -1rem;
}

aside .logo .text,
aside .menu .button {
    display: flex;
    align-items: center;
    text-decoration: none;
    transition: 0.5s ease-in-out;
    padding: 0.5rem 1rem;
}

aside .menu .button .material-icons {
    font-size: 2rem;
    color: var(--light-alt);
    transition: 0.5s ease-in-out;
}

aside .menu .button .text {
    color: var(--light-alt);
    transition: 0.2s ease-in-out;
    max-height: 32px;
}

aside .menu .button:hover {
    background-color: var(--dark-alt);
}

aside .menu .button:hover .material-icons,
aside .menu .button:hover .text {
    color: var(--light);
}

aside .menu .button.router-link-exact-active {
    background-color: var(--dark-alt);
    border-right: 5px solid var(--light);
}

aside .menu .button.router-link-exact-active .material-icons,
aside .menu .button.router-link-exact-active .text {
    color: var(--light);
}

aside.is-expanded {
    width: var(--sidebar-width);
}

aside.is-expanded .menu-toggle-wrap {
    top: -3rem;
}

aside.is-expanded .menu-toggle-wrap .menu-toggle {
    transform: rotate(-180deg);
}

aside.is-expanded h3,
aside.is-expanded .logo .text,
aside.is-expanded .button .text {
    opacity: 1;
}

aside.is-expanded .button .material-icons {
    margin-right: 1rem;
}

@media (max-width: 1024px) {
    aside {
        /* position: absolute; */
        z-index: 99;
    }
}
</style>