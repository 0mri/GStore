import axios from 'axios'

const UserModule = {
  namespaced: true,
  state: {
    user: JSON.parse(localStorage.getItem('user') || '{}'), // makes sure the user is logged in even after
  },
  mutations: {
    SET_USER(state, payload) {
      localStorage.setItem('user', JSON.stringify(payload))
      state.user = payload
    },
    DEL_USER(state) {
      state.user = null
      localStorage.removeItem('user')
    },
  },
  actions: {
    // run the below action to get a new access token on expiration
    getUser(context) {
      return new Promise((resolve, reject) => {
        axios
          .get('auth/users/me/')
          .then(({ data }) => {
            context.commit('SET_USER', data)
            resolve(data)
          })
          .catch((err) => {
            reject(err)
          })
      })
    },
    setUser(context, user) {
      context.commit('SET_USER', user)
    },
    deleteUser(context) {
      context.commit('DEL_USER')
    },
  },
}

export default UserModule
