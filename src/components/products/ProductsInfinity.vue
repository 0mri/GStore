<template>
  <div>
    <div class="columns is-gapless is-centered">
      <div class="column is-6">
        <search
          @loading="loading = true"
          @finishLoad="loading = false"
          @search="(data) => Search(data)"
          @OpenSideBar="
            $parent.$refs.sidebar.open = !$parent.$refs.sidebar.open
          "
          @clearSearch="serachResults = null"
        />
        <b-button
          @click="$parent.$refs.sidebar.open = !$parent.$refs.sidebar.open"
          type="is-primary"
          size="is-medium"
          class="cat-btn is-hidden-desktop"
        >
          <b-icon pack="fas" icon="bars"> </b-icon>
        </b-button>
      </div>
    </div>

    <product-list class="" ref="list" :products="serachResults || products">
    </product-list>
    <infinite-loading spinner="waveDots" @infinite="infiniteHandler">
    </infinite-loading>
    <b-loading :active.sync="loading" />
  </div>
</template>
<script>
import axios from 'axios'
import Search from '@/components/Search'
import ProductList from '@/components/Cart/ProductsList'
import productService from '@/services/productService'

export default {
  watch: {
    $route() {
      this.loading = true
      // this.loadNewContent()
    },
  },
  components: {
    ProductList,
    Search,
  },
  computed: {
    calcOffset() {
      return this.perPage * (this.page - 1)
    },
  },
  data() {
    return {
      products: [],
      loading: false,
      serachResults: null,
      perPage: 8,
      page: 1,
    }
  },
  created() {
    // console.log('2')
  },

  methods: {
    infiniteHandler($state) {
      productService
        .fetchProducts(
          this.calcOffset,
          this.perPage,
          this.$route.params.category
        )
        .then(({ data }) => {
          if (data.results.length) {
            this.page += 1
            this.products.push(...data.results)
            $state.loaded()
          } else {
            $state.complete()
          }
        })
    },
    loadNewContent() {
      productService
        .fetchProducts(
          this.calcOffset,
          this.perPage,
          this.$route.params.category
        )
        .then(({ data }) => {
          this.total = parseInt(data.count)
          this.products = data.results || data.product
        })
        .finally(() => {
          this.loading = false
        })
    },
  },
}
</script>

<style lang="scss" scoped>
.cat-btn {
  border-radius: 50000px !important;
  position: fixed;
  z-index: 40;
  right: 2.5rem;
  bottom: 3rem;
  box-shadow: 0 0 8px 3px #bbbbbb;
}
</style>
