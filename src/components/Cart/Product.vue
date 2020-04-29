<template>
  <div class="tile is-parent">
    <div class="tile is-child">
      <div class="box">
        <router-link
          :to="{
            name: 'product-detail',
            params: {
              slug: product.slug,
            },
          }"
        >
          <div class="card-image">
            <figure class="image is-4by3">
              <v-lazy-image
                alt="Placeholder image"
                style="border-radius: 6px 6px 0px 0px;"
                :src="
                  product.image.image ||
                    `https://i.picsum.photos/id/${product.id + 10}/600/400.jpg`
                "
                src-placeholder="https://i.picsum.photos/id/5/20/20.jpg"
              />
              <!-- <v-lazy-image
                alt="Placeholder image"
                style="border-radius: 6px 6px 0px 0px;"
                :src-placeholder="
                  `https://i.picsum.photos/id/${product.id + 10}/60/40.jpg`
                "
                :src="
                  `https://i.picsum.photos/id/${product.id + 10}/600/400.jpg`
                "
              /> -->

              <div class="quantity-display">
                <span :class="calcQuantity">{{
                  product.quantity_avialable
                }}</span>
              </div>
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="">
                <p class="subtitle is-7">{{ product.name }}</p>
                <p class="title is-6">{{ product.price }}$</p>
              </div>
            </div>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    product: Object,
  },
  components: {},
  computed: {
    calcQuantity() {
      if (this.product.quantity_avialable < 10) return 'tag is-danger '
      else if (this.product.quantity_avialable < 20) return 'tag is-warning '
      return 'tag is-info '
    },
  },
  methods: {
    addToCart(product) {
      this.$emit('addToCart', product)
    },
  },
}
</script>

<style scoped>
.tag {
  border-radius: 6px 0px 0px 0px;
}
.box {
  padding: 0;
  -webkit-box-shadow: 0 2px 3px rgba(10, 10, 10, 0.02),
    0 0 0 1px rgba(10, 10, 10, 0.05) !important;
  box-shadow: 0 2px 3px rgba(10, 10, 10, 0.02), 0 0 0 1px rgba(10, 10, 10, 0.05) !important;
}

.tile.is-parent {
  padding: 0.35rem !important;
}
.quantity-display {
  position: absolute;
  bottom: 0;
  right: 0;
}
</style>
