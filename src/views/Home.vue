<script setup>
import HomeSection from "@/components/HomeSection.vue";
import HomeCard from "@/components/HomeCard.vue";
</script>

<template>
  <HomeSection title="NutriSwap" image="src\assets\images\placeholder.png">
    <HomeCard
      title-text="¡Intercambia, disfruta y come lo que te gusta!"
      description-text="Intercambiar un alimento por otro nunca había sido tan sencillo. En NutriSwap te damos las mejores opciones para que sigas disfrutando de tus comidas sin complicarte, eligiendo lo que más te guste sin perder nutrientes. Solo elige, intercambia y mantén el equilibrio en tu alimentación de forma sencilla y práctica."
      button-text="Empieza a intercambiar"
    ></HomeCard>
  </HomeSection>

  <HomeSection
    title="¿Qué es NutriSwap y cómo funciona?"
    image="src\assets\images\placeholder.png"
  >
    <HomeCard
      title-text="Te brindamos la alternativa más similar al alimento que quieres sustituir"
      description-text="Utilizamos datos del Sistema Mexicano de Alimentos
      Equivalentes (SMAE) para encontrar la mejor alternativa al alimento que
      elijas. Nuestro algoritmo analiza los macronutrientes de todos los
      alimentos dentro de la misma categoría y te proporciona varias opciones,
      permitiéndote intercambiar tu porción de la mejor manera."
    >
    </HomeCard>
  </HomeSection>

  <HomeSection title="¿Qué son las porciones y cómo se definen?">
    <HomeCard
      title-text="La clave para una alimentación equilibrada"
      description-text="Una porción es la cantidad específica de un alimento que se recomienda consumir. Su tamaño varía según el tipo de alimento y las necesidades nutricionales de cada persona."
    ></HomeCard>
  </HomeSection>

  <HomeSection title="¿Por qué es importante seguir las porciones?">
    <HomeCard
      title-text="El equilibrio entre nutrición y bienestar"
      description-text="Un seguimiento adecuado de las porciones te ayuda a
    consumir los nutrientes necesarios para tu cuerpo sin desequilibrar tu
    alimentación. Es clave para alcanzar objetivos como la pérdida de peso, el
    mantenimiento o aumento de masa muscular."
    ></HomeCard>
  </HomeSection>

  <HomeSection
    title=" ¿Por qué aprender a intercambiar porciones mejora tu alimentación?"
  >
    <HomeCard
      title-text="Flexibilidad sin perder el equilibrio nutricional"
      description-text="Conocer cómo intercambiar porciones te permite adaptar tu
  alimentación sin afectar tu ingesta de nutrientes. Esto facilita una dieta
  más variada, personalizada y experimental sin sacrificar el control
  nutricional."
    ></HomeCard>
  </HomeSection>
</template>
