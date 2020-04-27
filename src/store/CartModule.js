import _ from 'lodash'
import paymentService from '@/services/paymentService'
const CartModule = {
  namespaced: true,
  state: {
    items: JSON.parse(localStorage.getItem(`vue-shopping-cart`) || '[]'),
  },
  getters: {
    sumItems(state) {
      return _.sumBy(state.items, (p) => {
        return p.quantity * p.product_price
      }).toFixed(2)
    },
  },
  mutations: {
    ADD_TO_CART: (state, product) => {
      const record = state.items.find((p) => p.id === product.id)
      if (!record) {
        state.items.push({
          ...product,
          quantity: product.product_quantity,
        })
      } else {
        record.quantity += product.product_quantity
      }
    },
    REMOVE_FROM_CART: (state, product) => {
      state.items = state.items.filter((p) => p.id !== product.id)
    },
    EMPTY_CART: (state) => {
      localStorage.removeItem(`vue-shopping-cart`)
      state.items = []
    },
    // ORDER_CART: (state, cart) => {
    //   console.log(cart);

    // }
  },
  actions: {
    addToCart(context, product) {
      context.commit('ADD_TO_CART', product)
    },
    removeFromCart(context, product) {
      context.commit('REMOVE_FROM_CART', product)
    },
    CheckOutCart(context, nonce) {
      // console.log(context.state.items);
      return new Promise((resolve, reject) => {
        paymentService
          .makePayment(nonce, context.state.items)
          .then((response) => {
            resolve(response)
            response.data.status == 'success'
              ? context.commit('EMPTY_CART')
              : null
          })
          .catch((error) => {
            reject(error)
          })
      })
    },
  },
}

export default CartModule
