<template>
  <div>
    <b-loading :active.sync="loading" />
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
    <div class="columns is-gapless">
      <product-list
        class="column is-12"
        ref="list"
        :total="total"
        :products="serachResults || products"
      >
      </product-list>
    </div>
    <div>
      <section
        v-if="serachResults != null && serachResults.length == 0 && !loading"
        class="section"
      >
        <div class="content has-text-grey has-text-centered">
          <p>
            <b-icon icon="binoculars" size="is-large"> </b-icon>
          </p>
          <p>We couldnt find this product</p>
        </div>
      </section>
      <section
        v-else-if="!products.length && !serachResults && !loading"
        class="section"
      >
        <div class="content has-text-grey has-text-centered">
          <p>
            <b-icon icon="emoticon-sad" size="is-large"> </b-icon>
          </p>
          <p>There are no products here</p>
        </div>
      </section>
    </div>
    <div class="columns">
      <div class="column">
        <section class="pagination-section" v-if="products.length">
          <b-pagination
            v-if="!serachResults"
            :total="total"
            :current.sync="current"
            :range-before="rangeBefore"
            :range-after="rangeAfter"
            :order="order"
            :size="size"
            :simple="false"
            :rounded="false"
            :per-page="perPage"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page"
          >
            <!-- PREV BUTTON -->
            <b-pagination-button
              slot="previous"
              slot-scope="props"
              :page="props.page"
              tag="router-link"
              :to="{
                name: 'products',
                params: {
                  category: $route.params.category,
                  page: props.page.number,
                },
              }"
              :event="props.page.disabled ? '' : 'click'"
            >
              <b-icon icon="chevron-left" size="is-small"> </b-icon>
            </b-pagination-button>
            <!-- PAGES -->
            <b-pagination-button
              slot-scope="props"
              :page="props.page"
              :id="`page${props.page.number}`"
              tag="router-link"
              :to="{
                name: 'products',
                params: {
                  category: $route.params.category,
                  page: props.page.number,
                },
              }"
            >
              {{ props.page.number }}
            </b-pagination-button>
            <!-- NEXT BUTTON -->

            <b-pagination-button
              slot="next"
              slot-scope="props"
              :page="props.page"
              tag="router-link"
              :event="props.page.disabled ? '' : 'click'"
              :to="{
                name: 'products',
                params: {
                  category: $route.params.category,
                  page: props.page.number,
                },
              }"
            >
              <b-icon icon="chevron-right" size="is-small"> </b-icon>
            </b-pagination-button>
          </b-pagination>
        </section>
      </div>
    </div>
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
      this.current = parseInt(this.$route.params.page) || 1
      this.loadNewContent()
    },
  },
  components: {
    ProductList,
    Search,
  },
  computed: {
    calcOffset() {
      return this.perPage * (this.current - 1)
    },
  },
  data() {
    return {
      products: [],
      loading: true,
      total: -1,
      current: parseInt(this.$route.params.page) || 1,
      perPage: 12,
      rangeBefore: 3,
      rangeAfter: 3,
      order: 'is-centered',
      size: '',
      isSimple: false,
      isRounded: false,
      serachResults: null,
    }
  },
  created() {
    this.loadNewContent()
  },
  methods: {
    loadNewContent() {
      this.loading = true
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
    Search(data) {
      this.serachResults = data.results
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
