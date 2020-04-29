<template>
  <div>
    <b-loading :active.sync="loading"></b-loading>
    <section class="section">
      <div v-show="!loading" class="columns is-centered">
        <SideBar ref="sidebar" :categories="categories" />
        <div class="container">
          <ProductsInfinity v-if="$route.query.infinity" />
          <Products v-else />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import SideBar from '@/components/products/CategoriesSideBar'
import Products from '@/components/products/Products'
import ProductsInfinity from '@/components/products/ProductsInfinity'
import categoryService from '@/services/categoryService'
import axios from 'axios'
export default {
  components: {
    SideBar,
    Products,
    ProductsInfinity,
  },
  data() {
    return {
      categories: [],
      loading: true,
    }
  },
  created() {
    categoryService
      .fetchCategories()
      .then(({ data }) => {
        this.categories = data
      })
      .finally(() => {
        this.loading = false
      })
  },
  mounted() {},
}
</script>

<style></style>
