<script setup>
import { computed } from 'vue';

const props = defineProps({
    name: String,
    nutrients: Array,
    reference: {
        type: Array,
        default: () => [],
    },
});

const referenceMap = computed(() => {
    return props.reference.length > 0 ? props.reference.reduce((map, item) => {
        map[item.name] = item.amount;
        return map;
    }, {}) : null;
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
                        'text-red-500': referenceMap && nutrient.amount < (referenceMap[nutrient.name] || 0),
                        'text-green-500': referenceMap && nutrient.amount > (referenceMap[nutrient.name] || 0),
                    }">
                        <td>{{ nutrient.name }}</td>
                        <td>
                            <span v-if="referenceMap && nutrient.amount > (referenceMap[nutrient.name] || 0)"
                                class="text-green-500">
                                <span class="material-symbols">arrow_up</span>
                            </span>
                            <span v-if="referenceMap && nutrient.amount < (referenceMap[nutrient.name] || 0)"
                                class="text-red-500">
                                <span class="material-symbols">arrow_down</span>
                            </span>
                            {{ nutrient.amount }}
                        </td>
                    </tr>
                </tbody>
            </v-table>
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
