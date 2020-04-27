import Vue from 'vue'
import Vuex from 'vuex'
import Auth from './auth'
import CartModule from './CartModule'
import Orders from './cart/orders'
import UserModule from './UserModule'
// import { axiosBase } from '../api/axios-Base'
Vue.use(Vuex)

const localStoragePlugin = (store) => {
  store.subscribe((mutation, { cart }) => {
    window.localStorage.setItem(`vue-shopping-cart`, JSON.stringify(cart.items))
  })
}
const plugins = [localStoragePlugin]

export default new Vuex.Store({
  modules: {
    auth: Auth,
    User: UserModule,
    cart: CartModule,
    orders: Orders,
  },
  plugins,
})
