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
