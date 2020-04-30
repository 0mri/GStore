<template>
  <div>
    <!-- <div class="columns is-gapless is-centered">
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
    </div> -->
    <products-list :mobileLayOut="12" :products="list" />
    <infinite-loading @infinite="infiniteHandler">
      <vue-simple-spinner slot="spinner"></vue-simple-spinner>
    </infinite-loading>
    <!-- <b-loading :active.sync="loading" /> -->
  </div>
</template>
<script>
import axios from 'axios'
import Search from '@/components/Search'
import ProductsList from '@/components/Cart/ProductsList'
import productService from '@/services/productService'

export default {
  watch: {
    // $route() {
    //   this.loading = false
    //   // this.loadNewContent()
    // },
  },
  components: {
    ProductsList,
    Search,
  },
  computed: {
    calcOffset() {
      return this.perPage * (this.page - 1)
    },
  },
  data() {
    return {
      list: [],
      // loading: false,
      perPage: 16,
      page: 1,
    }
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
            this.list.push(...data.results)
            $state.loaded()
          } else {
            $state.complete()
          }
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
