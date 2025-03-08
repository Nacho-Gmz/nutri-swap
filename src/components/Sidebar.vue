<script setup>
import { ref } from "vue";
import { useTheme } from "vuetify";

const theme = useTheme();

function toggleTheme() {
  theme.global.name.value = theme.global.current.value.dark ? "light" : "dark";
}

const items = ref([
  { title: "Inicio", icon: "home", route: "/" },
  { title: "Intercambio", icon: "sync", route: "/swapper" },
  { title: "Acerca de", icon: "info", route: "/about" },
]);
</script>

<template>
  <v-navigation-drawer permanent :width="200">
    <v-list>
      <v-list-item prepend-avatar="/logo.png" title="NutriSwap"></v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list density="compact" nav>
      <v-list-item
        v-for="item in items"
        :prepend-icon="item.icon"
        :key="item.title"
        :to="item.route"
        :title="item.title"
        active-class="router-link-exact-active"
        class="button"
        color="primary"
        rounded="xl"
      >
      </v-list-item>
    </v-list>
    <template #append>
      <v-list density="compact" nav>
        <v-list-item
          prepend-icon="person"
          to="/login"
          title="Iniciar sesión"
          color="primary"
          rounded="xl"
        >
        </v-list-item>
        <v-list-item
          prepend-icon="contrast"
          @click="toggleTheme"
          title="Cambiar tema"
          color="primary"
          rounded="xl"
        >
        </v-list-item>
      </v-list>
    </template>
  </v-navigation-drawer>
</template>
