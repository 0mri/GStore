import api from '@/services/api'

export default {
  makePayment(nonce, products) {
    return new Promise((resolve, reject) => {
      api
        .post('payment/checkout/', {
          payment_method_nonce: nonce,
          products: products,
        })
        .then((response) => resolve(response))
        .catch((error) => reject(error))
    })
  },
  retrieveNonce() {
    return new Promise((resolve, reject) => {
      api
        .get('payment/checkout/new')
        .then((response) => resolve(response))
        .catch((error) => reject(error))
    })
  },
}
