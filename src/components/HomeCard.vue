<template>
  <v-container class="fill-height" fluid>
    <v-responsive
      class="mx-auto text-center d-flex align-center justify-center"
      max-width="600"
      style="height: 100vh"
    >
      <p class="font-weight-bold text-sm-h2 text-h4 mt-2">
        {{ titleText }}
      </p>
      <p class="font-weight-medium text-primary">
        {{ subtitleText }}
      </p>
      <p class="mt-4 text-body-1 text-medium-emphasis">
        {{ descriptionText }}
      </p>
      <br />
      <v-btn
        v-if="showButton"
        rounded
        class="text-none"
        color="primary"
        size="x-large"
        :text="buttonText"
        variant="flat"
        :to="buttonLink"
      />
    </v-responsive>
  </v-container>
</template>

<script>
export default {
  props: {
    titleText: {
      type: String,
      default: "",
    },
    subtitleText: {
      type: String,
      default: "",
    },
    descriptionText: {
      type: String,
      default: "",
    },
    buttonText: {
      type: String,
      default: "",
    },
    buttonLink: {
      type: String,
      default: "/",
    },
    showButton: {
      type: Boolean,
      default: false,
    },
  },
};
</script>
