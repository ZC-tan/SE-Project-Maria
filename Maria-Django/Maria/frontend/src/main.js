import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import './assets/login.css'
import './assets/global.css'

// import VueQuillEditor from '../node_modules/vue-quill-editor'
//
// // require styles
// import '../node_modules/quill/dist/quill.core.css'
// import '../node_modules/quill/dist/quill.snow.css'
// import '../node_modules/quill/dist/quill.bubble.css'
//
// Vue.use(VueQuillEditor, /* { default global options } */)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
