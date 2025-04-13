import './assets/main.css'
import './assets/Tailwind/tailwind.css';
import './assets/Scss/style.scss';

// Animate
import 'animate.css';

// Font Awesome
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
// Add Free Icons Styles To SVG Core
library.add(fas, far, fab);

// Axios  استيراد
import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:8000";


import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())

// eslint-disable-next-line vue/multi-word-component-names
app.component("fa", FontAwesomeIcon);

// Axios
app.use(router, axios);

app.mount('#app')
