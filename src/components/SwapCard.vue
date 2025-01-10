<script setup>
import { ref } from 'vue';

const alimento = []

const desserts = [
    {
        name: 'Calorías',
        calories: 159,
    },
    {
        name: 'Carbohidratos',
        calories: 237,
    },
    {
        name: 'Proteína',
        calories: 262,
    },
    {
        name: 'Lípidos',
        calories: 305,
    },
]

</script>

<template>
    <v-card variant="tonal">
        <v-card-item>
            <v-card-title primary-title>
                <!-- {{ alimento.name }} -->
                Manzana
            </v-card-title>
        </v-card-item>
        <v-card-text>
            <v-table>
                <thead>
                    <tr>
                        <th class="text-left">

                        </th>
                        <th class="text-left">
                            <b>Cantidad</b>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in desserts" :key="item.name">
                        <td>{{ item.name }}</td>
                        <td>{{ item.calories }}</td>
                    </tr>
                </tbody>
            </v-table>
            <br>

        </v-card-text>
    </v-card>
</template>