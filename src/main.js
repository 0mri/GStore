import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Buefy from 'buefy'
import './assets/scss/app.scss'
import Default from './layouts/Default.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
// import VueSocialauth from 'vue-social-auth'
import VueScrollReveal from 'vue-scroll-reveal'

import api from '@/services/api'
// Using ScrollReveal's default configuration
Vue.use(VueScrollReveal, {
  class: 'v-scroll-reveal', // A CSS class applied to elements with the v-scroll-reveal directive; useful for animation overrides.
  duration: 800,
  scale: 1,
  distance: '10px',
  mobile: true,
  // cleanup: true,
  // offset: 0.8,
  // debug: true,
})

// import IdleVue from 'idle-vue'
// IDLE Vue
// const eventsHub = new Vue()
// Vue.use(IdleVue, {
//   eventEmitter: eventsHub,
//   idleTime: 5
// }) // sets up the idle time,i.e. time left to logout the user on no activity

// // Form Validation
// extend('required', {
//   ...required,
//   message: 'This field is required'
// })

// Buefy
Vue.use(Buefy)
Vue.use(VueAxios, axios)

// Vue.use(VueSocialauth, {
//   providers: {
//     google: {
//       clientId:
//         '865964894539-8oot0dnaufhc3v8gsfbebo43448798tl.apps.googleusercontent.com',
//       redirectUri: '/auth/google/callback', // Your client app URL
//     },
//   },
// })

Vue.config.productionTip = false

//Layouts
Vue.component('default-layout', Default)

router.beforeEach((to, from, next) => {
  // if any of the routes in ./router.js has a meta named 'requiresAuth: true'
  // then check if the user is logged in before routing to this path:
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!store.getters['auth/loggedIn']) next({ name: 'signin' })
    else next()
  }
  // else if any of the routes in ./router.js has a meta named 'requiresLogged: true'
  // then check if the user is logged in; if true continue to home page else continue routing to the destination path
  // this comes to play if the user is logged in and tries to access the login/register page
  else if (to.matched.some((record) => record.meta.requiresLogged)) {
    if (store.getters['auth/loggedIn'])
      next({
        name: 'products',
        params: {
          category: 'all',
        },
      })
    else next()
  } else next()
})

if (store.getters['auth/loggedIn'])
  api.defaults.headers.common['Authorization'] =
    'Bearer ' + store.getters['auth/accessToken']

api.interceptors.response.use(undefined, async (error) => {
  const originalRequest = error.config
  if (error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true
    return await store.dispatch('auth/refreshToken').then(() => {
      return api(originalRequest)
    })
    // .catch((err) => {
    //   store.dispatch('auth/logoutUser').then(() => {
    //     router.push('/login')
    //   })
    // })
  } else if (error.response.status == 401 && originalRequest._retry)
    store.dispatch('auth/logoutUser').then(() => {
      router.push('/login')
    })
  return Promise.reject(error)
})

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app')
