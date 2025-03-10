<template>
  <v-card class="pa-4 rounded-xl" elevation="4">
    <v-card-title class="font-weight-bold text-primary text-wrap">{{
      titleText
    }}</v-card-title>
    <v-card-text class="text-justify">{{ descriptionText }}</v-card-text>
    <v-card-actions v-if="buttonText">
      <v-btn
        class="rounded-xl"
        color="primary"
        variant="elevated"
        @click="$emit('click')"
        >{{ buttonText }}</v-btn
      >
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    titleText: String,
    subtitleText: String,
    descriptionText: String,
    buttonText: String,
  },
};
</script>
