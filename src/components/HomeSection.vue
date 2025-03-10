<template>
  <v-container fluid class="home-section">
    <v-row align="center" justify="center" class="section-content">
      <!-- Image Column -->
      <v-col cols="12" md="6" order-md="1" :order="imagePosition">
        <v-img
          :src="image"
          height="300px"
          contain
          class="section-image"
        ></v-img>
      </v-col>

      <!-- Cards Column -->
      <v-col cols="12" md="6">
        <h2 class="section-title">{{ title }}</h2>
        <slot />
        <!-- Place `InfoCard` components inside here -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    title: String,
    image: String,
    reverse: Boolean, // Controls whether the image appears on the right or left
  },
  computed: {
    imagePosition() {
      return this.reverse ? "2" : "1"; // Ensures image is positioned correctly
    },
  },
};
</script>

<style scoped>
.home-section {
  padding: 50px 0;
}
.section-title {
  text-align: left;
  margin-bottom: 20px;
}
.section-image {
  width: 100%;
  object-fit: contain;
}
</style>
