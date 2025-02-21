<script setup>


</script>

<template>

    <div class="v-row align-center justify-center h-100">
        <div class="v-sheet bg-background flex-1-1 px-4" style="max-width: 420px;">
            <div class="v-responsive v-img mx-auto mb-4" style="max-width: 60px;">
                <div class="v-responsive__sizer" style="padding-bottom: 96.2891%;"></div><img
                    class="v-img__img v-img__img--contain" src="/logo.png" style="">
            </div>
            <div class="text-h5 text-center mb-8 font-weight-medium">Regístrate en NutriSwap</div>
            <div class="v-sheet border-opacity-25 border-thin rounded-xl overflow-hidden">
                <div
                    class="v-input v-input--horizontal v-input--center-affix v-input--density-compact v-locale--is-ltr v-text-field">
                    <div class="v-input__control">
                        <div
                            class="v-field v-field--center-affix v-field--flat v-field--no-label v-field--variant-solo rounded-lg v-locale--is-ltr">
                            <div class="v-field__field" data-no-activator=""><input placeholder="Nombre" size="1"
                                    type="text" id="input-125" aria-describedby="input-125-messages"
                                    class="v-field__input"></div>
                            <div class="v-field__outline"></div>
                        </div>
                    </div>
                </div>
                <hr class="v-divider" aria-orientation="horizontal" role="separator">
                <div
                    class="v-input v-input--horizontal v-input--center-affix v-input--density-compact v-locale--is-ltr v-text-field">
                    <div class="v-input__control">
                        <div
                            class="v-field v-field--center-affix v-field--flat v-field--no-label v-field--variant-solo rounded-lg v-locale--is-ltr">
                            <div class="v-field__field" data-no-activator=""><input placeholder="Correo" size="1"
                                    type="text" id="input-125" aria-describedby="input-125-messages"
                                    class="v-field__input"></div>
                            <div class="v-field__outline"></div>
                        </div>
                    </div>
                </div>
                <hr class="v-divider" aria-orientation="horizontal" role="separator">
                <div
                    class="v-input v-input--horizontal v-input--center-affix v-input--density-compact v-locale--is-ltr v-text-field">
                    <div class="v-input__control">
                        <div
                            class="v-field v-field--center-affix v-field--flat v-field--no-label v-field--variant-solo rounded-lg v-locale--is-ltr">
                            <div class="v-field__field" data-no-activator=""><input placeholder="Contraseña" size="1"
                                    type="password" id="input-125" aria-describedby="input-125-messages"
                                    class="v-field__input"></div>
                            <div class="v-field__outline"></div>
                        </div>
                    </div>
                </div>
                <hr class="v-divider" aria-orientation="horizontal" role="separator">
                <div
                    class="v-input v-input--horizontal v-input--center-affix v-input--density-compact v-locale--is-ltr v-text-field">
                    <div class="v-input__control">
                        <div
                            class="v-field v-field--center-affix v-field--flat v-field--no-label v-field--variant-solo rounded-lg v-locale--is-ltr">
                            <div class="v-field__field" data-no-activator=""><input placeholder="Confirma tu contraseña"
                                    size="1" type="password" id="input-125" aria-describedby="input-125-messages"
                                    class="v-field__input"></div>
                            <div class="v-field__outline"></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="py-4">
                <button type="button"
                    class="v-btn v-btn--block v-btn--flat bg-primary v-btn--density-default rounded-xl v-btn--size-default v-btn--variant-elevated text-none"><span
                        class="v-btn__overlay"></span><span class="v-btn__underlay"></span><span class="v-btn__content"
                        data-no-activator="">Regístrate</span></button>
            </div>
            <div class="text-center text-body-2"> ¿Ya tienes una cuenta? <RouterLink
                    class="text-decoration-none text-primary font-weight-medium" to="/login">Inicia sesión
                </RouterLink>
            </div>
        </div>
    </div>

</template>