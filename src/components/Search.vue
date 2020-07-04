<template>
  <b-field grouped>
    <p class="control is-hidden-mobile">
      <b-button @click="$emit('OpenSideBar')">
        <b-icon pack="fas" icon="list" type="is-primary" size="is-small">
        </b-icon>
      </b-button>
    </p>
    <b-autocomplete
      :data="data"
      placeholder="Search"
      field="title"
      v-model="searchField"
      :loading="isFetching"
      :keep-first="false"
      :clearable="true"
      :clear-on-select="true"
      :open-on-focus="true"
      expanded
      icon="magnify"
      @input="(val) => (val.length == 0 ? $emit('clearSearch') : null)"
      @typing="getAsyncData"
      @select="(option) => selected(option.slug)"
    >
      <template slot-scope="props">
        <div class="media">
          <div class="media-left">
            <v-lazy-image
              :src="
                `https://picsum.photos/id/${props.option.id + 10}/32/32.jpg`
              "
              src-placeholcer=""
            />
          </div>
          <router-link
            :to="{
              name: 'product-detail',
              params: {
                slug: props.option.slug,
              },
            }"
            class="media-content"
          >
            {{ props.option.name }}
            <br />
            <small> {{ props.option.category.name }} </small>
          </router-link>
        </div>
      </template>
    </b-autocomplete>
  </b-field>
</template>

<script>
import debounce from 'lodash/debounce'
import productService from '@/services/productService'
export default {
  name: 'search',
  data() {
    return {
      data: [],
      isFetching: false,
      searchField: '',
    }
  },
  methods: {
    // You have to install and import debounce to use it,
    // it's not mandatory though.
    getAsyncData: debounce(function(name) {
      if (!name.length) {
        this.data = []
        return
      }
      this.isFetching = true
      this.$emit('loading')
      productService
        .searchProducts(name, 8)
        .then(({ data }) => {
          this.data = data.results.slice(0, 3)
          this.$emit('search', data)
        })
        .catch((error) => {
          this.data = []
          throw error
        })
        .finally(() => {
          this.isFetching = false
          this.$emit('finishLoad')
        })
    }, 250),
    selected: function(slug) {
      this.$router.push({
        name: 'product-detail',
        params: {
          slug: slug,
        },
      })
    },
  },
}
</script>
