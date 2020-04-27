<template>
  <section class="section">
    <payment :client_token="token"></payment>
  </section>
</template>

<script>
import Payment from '../../components/Cart/Payment'
import { mapGetters } from 'vuex'
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
  },
  created() {
   if (!this.token) this.$router.push('/cart')
  },
}
</script>

<style></style>
