import api from '@/services/api'

export default {
  fetchOrders() {
    return api.get('order/').then((response) => response)
  },
  retrieveOrder(orderID) {
    return api.get(`order/${orderID}`).then((response) => response)
  },
}
