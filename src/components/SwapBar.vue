<script setup>
import { ref } from 'vue';

const items = ref(["Manzana", "Naranja", "Pera", "Piña", "Fresa",]);

</script>

<template>
    <v-container class="pa-6 pa-md-12 my-16" fluid>
        <v-responsive class="mx-auto text-center" max-width="600">
            <p class="font-weight-bold text-sm-h2 text-h4 mt-2'">
                Intercambio
            </p>
            <br>
            <v-combobox auto-select-first="exact" rounded label="Alimento" variant="outlined"
                :items="items"></v-combobox>
            <br>
            <v-btn rounded class="text-none" color="primary" size="x-large" text="Busca alternativas" variant="flat" />
        </v-responsive>
    </v-container>
</template>