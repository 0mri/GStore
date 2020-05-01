import api from '@/services/api'
import userService from '@/services/userService'
const Auth = {
  namespaced: true,
  state: {
    accessToken: localStorage.getItem('access_token') || null, // makes sure the user is logged in even after
    // refreshing the page
    refreshToken: localStorage.getItem('refresh_token') || null,

    user: JSON.parse(localStorage.getItem('user') || '{}'), // makes sure the user is logged in even after
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
      api.defaults.headers.common['Authorization'] = 'Bearer ' + access
    },
    updateAccess(state, access) {
      state.accessToken = access
      api.defaults.headers.common['Authorization'] = 'Bearer ' + access
    },
    destroyToken(state) {
      state.accessToken = null
      state.refreshToken = null
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      api.defaults.headers.common['Authorization'] = ''
    },
    SET_USER(state, payload) {
      localStorage.setItem('user', JSON.stringify(payload))
      state.user = payload
    },
    DEL_USER(state) {
      state.user = null
      localStorage.removeItem('user')
    },
    SET_PROFILE_IMAGE(state, image) {
      state.user.profile_image = image
      localStorage.setItem('user', JSON.stringify(state.user))
    },
  },
  actions: {
    // run the below action to get a new access token on expiration
    refreshToken(context) {
      return new Promise((resolve, reject) => {
        api
          .post('auth/jwt/refresh/', {
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
        api
          .post('auth/users/', {
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
          context.commit('DEL_USER')
          resolve()
        })
      }
    },
    loginUser(context, credentials) {
      return new Promise((resolve, reject) => {
        api
          .post('auth/jwt/create', credentials)
          .then(({ data }) => {
            context.commit('updateLocalStorage', {
              access: data.access,
              refresh: data.refresh,
            }) // store the access and refresh token in localstorage
            resolve()
            context.commit('SET_USER', data.user)
          })
          .catch((err) => {
            reject(err)
          })
      })
    },
    async updateProfileImage(context, data) {
      return userService
        .putImage(
          data.imageFile,
          (uploadEvent) =>
            data.progress(
              Math.round((uploadEvent.loaded / uploadEvent.total) * 100) - 1
            ) //percentage loaded
        )
        .then((response) => {
          if (response.status == 200)
            context.commit('SET_PROFILE_IMAGE', response.data)
          return response
        })
        .catch((err) => err)
    },
  },
}

export default Auth
