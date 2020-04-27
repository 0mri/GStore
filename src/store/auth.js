// import { axiosBase } from '../api/axios-Base'
import store from './'

import axios from 'axios'
const Auth = {
  namespaced: true,
  state: {
    accessToken: localStorage.getItem('access_token') || null, // makes sure the user is logged in even after
    // refreshing the page
    refreshToken: localStorage.getItem('refresh_token') || null,
    // user: localStorage.getItem('user') || null
  },
  getters: {
    loggedIn(state) {
      return state.accessToken !== null
    },
    accessToken(state) {
      return state.accessToken
    },
  },
  mutations: {
    updateLocalStorage(state, { access, refresh }) {
      localStorage.setItem('access_token', access)
      localStorage.setItem('refresh_token', refresh)
      state.accessToken = access
      state.refreshToken = refresh
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + access
    },
    updateAccess(state, access) {
      state.accessToken = access
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + access
    },
    destroyToken(state) {
      state.accessToken = null
      state.refreshToken = null
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      axios.defaults.headers.common['Authorization'] = ''
    },
  },
  actions: {
    // run the below action to get a new access token on expiration
    refreshToken(context) {
      return new Promise((resolve, reject) => {
        axios
          .post('/auth/jwt/refresh/', {
            refresh: context.state.refreshToken,
          })
          .then((response) => {
            context.commit('updateAccess', response.data.access)
            resolve(response)
          })
          .catch((err) => {
            reject(err)
          })
      })
    },
    registerUser(context, data) {
      return new Promise((resolve, reject) => {
        axios
          .post('api/auth/users/', {
            username: data.username,
            password: data.password,
          })
          .then((response) => resolve(response))
          .catch((error) => reject(error))
      })
    },
    logoutUser(context) {
      if (context.getters.loggedIn) {
        return new Promise((resolve) => {
          context.commit('destroyToken')
          store.dispatch('User/deleteUser')
          resolve()
          // axiosBase
          //   .post('/auth/jwt/logout/')
          //   .then(() => {
          //     localStorage.removeItem('access_token')
          //     localStorage.removeItem('refresh_token')
          //     context.commit('destroyToken')
          //   })
          //   .catch(err => {
          //     localStorage.removeItem('access_token')
          //     localStorage.removeItem('refresh_token')
          //     context.commit('destroyToken')
          //     resolve(err)
          //   })
        })
      }
    },
    loginUser(context, credentials) {
      return new Promise((resolve, reject) => {
        axios
          .post('api/auth/jwt/create', credentials)
          .then(({ data }) => {
            context.commit('updateLocalStorage', {
              access: data.access,
              refresh: data.refresh,
            }) // store the access and refresh token in localstorage
            resolve()
            store.dispatch('User/setUser', data.user)
          })
          .catch((err) => {
            reject(err)
          })
      })
    },
  },
}

export default Auth
