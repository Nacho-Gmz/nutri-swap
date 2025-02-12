import 'vuetify/styles'
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { createVuetify } from 'vuetify'

const vuetify = createVuetify({
    components,
    directives,
    theme: {
        defaultTheme: 'light',
        themes: {
            light: {
                dark: false,
                colors: {
                primary: '#47b84d', 
                secondary: '#93e197',
                background: '#f9fbf9',
                surface: '#f9fbf9',
                text: '#070907',
                },
            },
            dark: {
                dark: true,
                colors: {
                primary: '#47b84d',
                secondary: '#1e6c22',
                background: '#040604',
                surface: '#040604',
                text: '#f6f8f6',
                },
            },
        },
    },
})

export default vuetify
