import Vue from 'vue'
import Vuex from 'vuex'
import Auth from './auth'
import CartModule from './modules/CartModule'
import OrderModule from './modules/OrderModule'
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
    cart: CartModule,
    orders: OrderModule,
  },
  plugins,
})
