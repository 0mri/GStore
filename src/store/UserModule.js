import userService from '@/services/userService'
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
    SET_PROFILE_IMAGE(state, image) {
      state.user.profile_image = image
      localStorage.setItem('user', JSON.stringify(state.user))
    },
  },
  actions: {
    // run the below action to get a new access token on expiration
    // getUser(context) {
    //   return new Promise((resolve, reject) => {
    //     axios
    //       .get('auth/users/me/')
    //       .then(({ data }) => {
    //         context.commit('SET_USER', data)
    //         resolve(data)
    //       })
    //       .catch((err) => {
    //         reject(err)
    //       })
    //   })
    // },
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
    setUser(context, user) {
      context.commit('SET_USER', user)
    },
    deleteUser(context) {
      context.commit('DEL_USER')
    },
  },
}

export default UserModule
