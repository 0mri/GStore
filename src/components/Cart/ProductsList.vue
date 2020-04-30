<template>
  <div>
    <div class="columns is-gapless is-multiline is-mobile">
      <div
        :class="`column is-3-desktop is-${mobileLayOut}-mobile`"
        v-for="product in products"
        :key="product.id"
      >
        <product class="tile" :product="product" />
      </div>
      <!-- <b-loading :is-full-page="false" :active="loading" /> -->
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import Product from './Product'

export default {
  name: 'product-list',
  props: {
    mobileLayOut: Number,
    products: Array,
    loading: Boolean,
  },
  computed: {
    // mobileLayOut() {
    //   return
    // },
  },
  created() {},
  components: {
    Product,
  },
  methods: {},
}
</script>

<style scoped></style>
