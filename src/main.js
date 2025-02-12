import { createApp } from 'vue'

// Vuetify
import vuetify from './plugins/vuetify'
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

// Components
import App from './App.vue'

import router from './router'

createApp(App)
.use(router)
.use(vuetify)
.mount('#app');
