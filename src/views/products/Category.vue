<template>
  <div>
    <section class="section">
      <div v-if="!loading" class="columns is-centered">
        <SideBar ref="sidebar" :categories="categories" />
        <div class="container">
          <ProductsInfinity v-if="$route.query.infinity == 'true'" />
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
      loading: false,
    }
  },
  created() {
    categoryService.fetchCategories().then(({ data }) => {
      this.categories = data
    })
  },
  mounted() {},
}
</script>

<style></style>
