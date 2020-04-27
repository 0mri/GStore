<template>
  <div>
    <b-loading :active.sync="loading"></b-loading>
    <section class="section">
      <div v-show="!loading" class="columns is-centered">
        <SideBar ref="sidebar" :categories="categories" />
        <!-- <div class="column is-2-widescreen"> -->
        <!-- </div> -->
        <div class="container">
          <Products />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import SideBar from '@/components/products/CategoriesSideBar'
import Products from '@/components/products/Products'
import categoryService from '@/services/categoryService'
import axios from 'axios'
export default {
  components: {
    SideBar,
    Products,
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
    // axios
    //   .get('/api/category/')
    //   .then(({ data }) => {
    //     this.categories = data
    //   })
    //   .finally(() => {
    //     this.loading = false
    //   })
  },
  mounted() {},
}
</script>

<style>
.is-fixed {
  position: fixed;
}
</style>
