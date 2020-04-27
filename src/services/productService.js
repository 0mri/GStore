import api from '@/services/api'

export default {
  fetchProducts(offset, limit, category) {
    return api
      .get(`product/?offset=${offset}&limit=${limit}&category=${category}`)
      .then((response) => response)
  },
  fetchProduct(slug) {
    return api.get(`product/${slug}/`).then((response) => response)
  },
  searchProducts(key, limit) {
    return api
      .get(`product?search=${key}&limit=${limit}`)
      .then((response) => response)
  },
  commentProduct(comment) {
    return api.post(`comment/`, comment).then((response) => response)
  },
}
