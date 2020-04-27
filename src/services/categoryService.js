import api from '@/services/api'

export default {
  fetchCategories() {
    return api.get(`category/`).then((response) => response)
  },
}
