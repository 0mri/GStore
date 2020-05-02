<template>
  <section class="section">
    <payment
      @complete="(data) => complete(data)"
      :productsToBuy="cart"
      :client_token="token"
    ></payment>
  </section>
</template>

<script>
import Payment from '../../components/Cart/Payment'
import { mapGetters, mapState } from 'vuex'
export default {
  data() {
    return {
      token: this.$route.params.token,
    }
  },
  components: {
    Payment,
  },
  computed: {
    ...mapGetters({
      loggedIn: 'auth/loggedIn',
    }),
    ...mapState({
      cart: (state) => state.cart.items,
    }),
  },
  created() {
    if (!this.token) this.$router.push('/cart')
  },
  methods: {
    complete(data) {},
  },
}
</script>

<style>

</style>
