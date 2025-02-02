<script setup lang="ts">
import { ref } from 'vue';
import SwapCard from './SwapCard.vue';

// Example nutrient data
const firstCardData = ref({
    name: 'Opción 1',
    nutrients: [
        { name: 'Proteína', amount: 20 },
        { name: 'Carbohidratos', amount: 50 },
        { name: 'Grasas', amount: 10 }
    ]
});

const swapCards = ref([
    {
        name: 'Opción 2',
        nutrients: [
            { name: 'Proteína', amount: 25 },
            { name: 'Carbohidratos', amount: 40 },
            { name: 'Grasas', amount: 9 }
        ]
    },
    {
        name: 'Opción 3',
        nutrients: [
            { name: 'Proteína', amount: 28 },
            { name: 'Carbohidratos', amount: 45 },
            { name: 'Grasas', amount: 18 }
        ]
    },
    {
        name: 'Opción 4',
        nutrients: [
            { name: 'Proteína', amount: 22 },
            { name: 'Carbohidratos', amount: 38 },
            { name: 'Grasas', amount: 12 }
        ]
    },
    {
        name: 'Opción 5',
        nutrients: [
            { name: 'Proteína', amount: 35 },
            { name: 'Carbohidratos', amount: 42 },
            { name: 'Grasas', amount: 20 }
        ]
    }
]);

const currentIndex = ref(0);

const cycleSwapCard = () => {
    currentIndex.value = (currentIndex.value + 1) % swapCards.value.length;
};
</script>

<template>
    <v-container class="pa-6 pa-md-12 my-16" fluid>
        <v-row>
            <v-col>
                <SwapCard :name="firstCardData.name" :nutrients="firstCardData.nutrients" />
            </v-col>
            <v-col>
                <SwapCard :name="swapCards[currentIndex].name" :nutrients="swapCards[currentIndex].nutrients"
                    :reference="firstCardData.nutrients" />
            </v-col>
        </v-row>
        <v-btn @click="cycleSwapCard">Swap Card</v-btn>
    </v-container>
</template>
