import api from '@/services/api'

export default {
  makePayment(nonce, products) {
    return api
      .post('payment/checkout/', {
        payment_method_nonce: nonce,
        products: products,
      })
      .then((response) => response)
      .catch((error) => error)
  },
}
