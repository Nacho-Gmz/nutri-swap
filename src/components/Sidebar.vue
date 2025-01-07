<script setup>
import { ref } from 'vue';

const drawer = ref(true);
const rail = ref(true);

const items = ref([
    { title: "Inicio", icon: "home", route: "/" },
    { title: "Intercambio", icon: "sync", route: "/swapper" },
    { title: "Acerca de", icon: "info", route: "/about" },

])
</script>

<template>
    <v-navigation-drawer expand-on-hover rail>
        <v-list>
            <v-list-item prepend-avatar="/logo.png" title="NutriSwap"></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
            <v-list-item v-for="item in items" :key="item.title" :to="item.route" :title="item.title"
                active-class="router-link-exact-active" class="button" color="primary" rounded="xl">
                <template v-slot:prepend>
                    <span class="material-icons">{{ item.icon }}</span>
                </template>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
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