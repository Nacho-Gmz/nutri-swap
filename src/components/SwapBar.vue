<script setup>
import { ref, onMounted } from 'vue';

const items = ref([]);

const fetchFoodNames = async () => {
    try {
        const response = await fetch('http://localhost:5000/nombrealimentos'); // Adjust if hosted elsewhere
        const data = await response.json();
        items.value = data.map(item => item.Alimento); // Extract food names
    } catch (error) {
        console.error('Error fetching food names:', error);
    }
};

onMounted(fetchFoodNames);
</script>

<template>
    <v-container class="pa-6 pa-md-12 mt-16" fluid>
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
