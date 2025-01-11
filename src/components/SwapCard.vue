<script setup>
defineProps({
    name: String,
    nutrients: Array,
    reference: {
        type: Array,
        default: () => [],
    },
});

import { computed } from 'vue';

const referenceMap = computed(() => {
    return reference.reduce((map, item) => {
        map[item.name] = item.amount;
        return map;
    }, {});
});

</script>

<template>
    <v-card variant="tonal">
        <v-card-text>
            <v-table>
                <thead>
                    <tr>
                        <th class="text-left">
                            {{ name }}
                        </th>
                        <th class="text-left">
                            <b>Cantidad</b>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(nutrient, index) in nutrients" :key="index" :class="{
                        'text-red-500': nutrient.amount < (referenceMap[nutrient.name] || 0),
                        'text-green-500': nutrient.amount > (referenceMap[nutrient.name] || 0),
                    }">
                        <td>{{ nutrient.name }}</td>
                        <td>{{ nutrient.amount }}</td>
                    </tr>
                </tbody>
            </v-table>
            <br>

        </v-card-text>
    </v-card>
</template>

<style lang="css" scoped>
.text-red-500 {
    color: red;
}

.text-green-500 {
    color: green;
}
</style>