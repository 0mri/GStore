<template>
  <section class="section">
    <div v-if="cart.length" class="columns">
      <div class="column is-9">
        <div class="columns is-multiline">
          <div v-for="product in cart" :key="product.id" class="column is-12">
            <div class="box">
              <article class="media">
                <figure class="media-left">
                  <p class="image is-96x96">
                    <v-lazy-image
                      alt="Placeholder image"
                      :src-placeholder="
                        `https://i.picsum.photos/id/${product.id +
                          10}/10/10.jpg`
                      "
                      :src="
                        `https://i.picsum.photos/id/${product.id +
                          10}/500/500.jpg`
                      "
                    />
                    <!-- <img
                      src="https://bulma.io/images/placeholders/128x128.png"
                    /> -->
                  </p>
                  <p>
                    <b-field>
                      <b-numberinput
                        class="qty-input"
                        controls-position="compact"
                        min="1"
                        max="10"
                        v-model="product.quantity"
                        type="is-primary"
                        size="is-small"
                        :editable="false"
                      ></b-numberinput>
                    </b-field>
                  </p>
                </figure>
                <div class="media-content">
                  <div class="content">
                    <p>
                      <span class="title is-5">
                        <router-link
                          :to="{
                            name: 'product-detail',
                            params: { slug: product.product_slug },
                          }"
                          >{{ product.product_name }}</router-link
                        >
                      </span>
                      <br />

                      <span class="subtitle is-6"
                        >{{ product.product_price }}$</span
                      >
                      <br />
                      <span class="subtitle is-6"
                        >QTY: {{ product.quantity }}</span
                      >
                      <br /><br />
                      <small class="has-text-grey">Free Shipping</small>
                    </p>
                  </div>
                </div>
                <div class="media-right">
                  <b-field>
                    <a
                      @click.prevent="removeItem(product)"
                      class="has-text-secondary"
                    >
                      <b-icon
                        size="is-small"
                        pack="fas"
                        icon="trash-alt"
                      ></b-icon>
                    </a>
                  </b-field>
                </div>
              </article>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-3">
        <div class="box">
          <div class="title is-4">
            Order Summary
          </div>
          <div class="field">
            <div class="level is-mobile">
              <div class="level-left">
                <div class="level-item">
                  <small>Subtotal</small>
                </div>
              </div>
              <div class="level-right">
                <div class="level-item">
                  <span>USD ${{ sumItems }}</span>
                </div>
              </div>
            </div>
          </div>
          <div class="field">
            <div class="level is-mobile">
              <div class="level-left">
                <div class="level-item">
                  <small>Shipping</small>
                </div>
              </div>
              <div class="level-right">
                <div class="level-item">
                  <span>USD $0.00</span>
                </div>
              </div>
            </div>
          </div>
          <b-field>
            <b-button
              @click="checkOut"
              :loading="checkOutLoading"
              type="is-primary is-fullwidth"
              >Checkout</b-button
            >
          </b-field>
        </div>
      </div>
    </div>
    <section v-else class="section content has-text-grey has-text-centered">
      <p>
        <b-icon icon="emoticon-sad" size="is-large"> </b-icon>
      </p>
      <p>Your Shopping Cart is empty</p>
      <b-button
        tag="router-link"
        :to="{ name: 'products', params: { category: 'all' } }"
        type="is-success"
        >Start Shopping</b-button
      >
    </section>
  </section>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
import paymentService from '@/services/paymentService'
export default {
  data() {
    return {
      isHoverable: true,
      checkOutLoading: false,
      isComponentModalActive: false,
    }
  },
  components: {},
  computed: {
    ...mapState({
      cart: (state) => state.cart.items,
    }),
    ...mapGetters('cart', ['sumItems']),
  },
  created() {
    // console.log(this.cart)
  },
  methods: {
    removeItem(product) {
      this.$buefy.dialog.confirm({
        message:
          '<strong class="title is-5">Are you sure about this? </strong> </br> This action will remove this item from your shopping cart.',
        onConfirm: () => this.$store.dispatch('cart/removeFromCart', product),
      })
    },
    checkOut() {
      this.checkOutLoading = true
      paymentService
        .retrieveNonce()
        .then(({ data }) => {
          this.$router.push({
            name: 'checkout',
            params: { token: data.token },
          })
        })
        .catch(() => {})
        .finally(() => {
          this.checkOutLoading = false
        })
    },
  },
}
</script>

<style>
.qty-input {
  margin-top: 0.75rem;
  width: 96px !important;
}
/* input {
  width: 44px !important;
} */
</style>
