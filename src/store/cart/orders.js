import orderService from '@/services/orderService'
const Orders = {
  namespaced: true,
  state: {
    // ordersList: JSON.parse(localStorage.getItem('orders') || [])
  },
  mutations: {
    // ADD_ORDERS: (state, orders) => {
    //   state.ordersList.push(...orders)
    // }
  },
  actions: {
    getAllOrders() {
      return new Promise((resolve) => {
        orderService.fetchOrders().then(({ data }) => {
          // context.commit('ADD_ORDERS', data)
          resolve(data)
        })
      })
    },
    getDetailOrder(context, id) {
      return new Promise((resolve, reject) => {
        orderService
          .retrieveOrder(id)
          .then(({ data }) => {
            // context.commit('ADD_ORDERS', data)
            resolve(data)
          })
          .catch((error) => {
            reject(error)
          })
      })
    },
  },
}

export default Orders
