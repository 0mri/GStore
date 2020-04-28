<template>
  <div>
    <div class="columns is-gapless is-multiline is-mobile">
      <div
        class="column is-3-desktop is-6-mobile"
        v-for="product in products"
        :key="product.id"
      >
        <product class="tile" :product="product" />
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import Product from './Product'
export default {
  name: 'product-list',
  props: {
    products: Array,
  },
  data() {
    return {
      isLoading: true,
      array: [1],
    }
  },
  created() {},
  components: {
    Product,
  },
  methods: {},
}
</script>

<style scoped></style>
