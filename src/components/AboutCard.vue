<script setup>
const items = [
  {
    title: "Luis Ignacio Gómez Aldrete",
    subtitle: "Diseño / Web",
    text: "luis.gomez5882@alumnos.udg.mx",
    avatar: "https://vuetifyjs.b-cdn.net/images/john-smirk.png",
  },
  {
    title: "Dayal Gutiérrez Villalobos",
    subtitle: "Backend / Base de datos",
    text: "dayal.gutierrez5863@alumnos.udg.mx",
    avatar: "https://vuetifyjs.b-cdn.net/images/john-smirk.png",
  },
  {
    title: "Emanuel Michel Lopez Franco",
    subtitle: "Asesor",
    text: "michel.lopez@academicos.udg.mx",
    avatar: "https://vuetifyjs.b-cdn.net/images/john-smirk.png",
  },
];
</script>

<template>
  <v-container class="pa-6 pa-md-12" fluid>
    <v-row>
      <v-col cols="12" lg="4" md="12">
        <p class="text-h5 font-weight-bold text-sm-h4">Conoce al equipo</p>

        <p class="mt-4 text-body-1 text-medium-emphasis">
          Este es el equipo responsable del proyecto modular NutriSwap para la
          carrera de INCO.
        </p>
      </v-col>

      <v-col cols="12" lg="8" md="12">
        <v-row justify="center">
          <v-col v-for="(item, i) in items" :key="i" cols="12" sm="6">
            <v-card
              class="px-0"
              :subtitle="item.subtitle"
              :title="item.title"
              :text="item.text"
            >
              <template #prepend>
                <v-avatar
                  color="surface-light"
                  :image="item.avatar"
                  :size="48"
                />
              </template>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>
