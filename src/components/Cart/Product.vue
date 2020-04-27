<template>
  <div class="tile is-parent">
    <div class="tile is-child box">
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
          <img
            src="@/assets/images/product_image_small.png"
            alt="Placeholder image"
          />
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
</template>

<script>
export default {
  props: {
    product: Object,
  },
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
.box {
  padding: 0;
}
.tile.is-parent {
  padding: 0.5rem;
}
</style>
