import api from '@/services/api'

export default {
  fetchOrders() {
    return api
      .get('order/')
      .then((response) => response)
      .catch((err) => err)
  },
  retrieveOrder(orderID) {
    return api
      .get(`order/${orderID}`)
      .then((response) => response)
      .catch((err) => err)
  },
}
