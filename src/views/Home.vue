<script setup>
import HomeCard from '@/components/HomeCard.vue';
</script>

<template>
    <v-main class="home-page">
        <HomeCard title-text="NutriSwap" subtitle-text="¡Intercambia, disfruta y come lo que te gusta!"
            description-text="Cambiar un alimento por otro nunca fue tan fácil. En NutriSwap te damos la mejor alternativa para que sigas disfrutando tus comidas sin complicaciones, eligiendo lo que prefieras sin perder valor nutricional (CAMBIAR REDACCION). Solo elige, intercambia y mantén el equilibrio en tu alimentación de forma sencilla y práctica."
            button-text="Empieza a intercambiar" button-link="/swapper" show-button="true" />
        <v-divider></v-divider>
        <HomeCard title-text="¿Qué es NutriSwap y cómo funciona?"
            subtitle-text="Te brindamos la alternativa más similar al alimento que quieres sustituir"
            description-text="Utilizamos datos del Sistema Mexicano de Alimentos Equivalentes (SMAE) para encontrar la mejor alternativa al alimento que elijas. Nuestro algoritmo analiza los macronutrientes de todos los alimentos dentro de la misma categoría y te proporciona varias opciones, permitiéndote intercambiar tu porción de la mejor manera." />
        <v-divider></v-divider>
        <HomeCard title-text="¿Qué son las porciones y cómo se definen?"
            subtitle-text="La clave para una alimentación equilibrada"
            description-text="Una porción es la cantidad específica de un alimento que se recomienda consumir. Su tamaño varía según el tipo de alimento y las necesidades nutricionales de cada persona." />
        <v-divider></v-divider>
        <HomeCard title-text="¿Por qué es importante seguir las porciones?"
            subtitle-text="El equilibrio entre nutrición y bienestar"
            description-text="Un seguimiento adecuado de las porciones te ayuda a consumir los nutrientes necesarios para tu cuerpo sin desequilibrar tu alimentación. Es clave para alcanzar objetivos como la pérdida de peso, el mantenimiento o aumento de masa muscular." />
        <v-divider></v-divider>
        <HomeCard title-text=" ¿Por qué aprender a intercambiar porciones mejora tu alimentación?"
            subtitle-text="Flexibilidad sin perder el equilibrio nutricional"
            description-text="Conocer cómo intercambiar porciones te permite adaptar tu alimentación sin afectar tu ingesta de nutrientes. Esto facilita una dieta más variada, personalizada y experimental sin sacrificar el control nutricional." />
    </v-main>
</template>

<style scoped>
.home-page {
    display: grid;
    align-items: center;
    justify-items: center;

    color: var(--dark);

    width: 100vw;
}
</style>