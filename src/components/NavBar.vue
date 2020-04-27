<template>
  <!-- <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link v-if="!loggedIn" to="/login">Login</router-link>
    <span v-if="!loggedIn">|</span>
    <router-link v-if="loggedIn" to="/about">About</router-link>
    <span v-if="loggedIn">|</span>
    <router-link v-if="!loggedIn" to="/signup">Signup</router-link>
    <span v-if="!loggedIn">|</span>
    <router-link v-if="loggedIn" to="/products">Products</router-link>
    <span v-if="loggedIn">| </span>
    <router-link v-if="loggedIn" to="/cart"
      >My Cart
      <span v-if="numOfItems" class="tag is-danger ">{{
        numOfItems
      }}</span></router-link
    >
    <span v-if="loggedIn">| </span>
    <router-link v-if="loggedIn" to="/logout">Logout</router-link>
  </div> -->
  <b-navbar
    :mobile-burger="true"
    shadow
    :fixedTop="true"
    wrapper-class="container"
  >
    <template slot="brand">
      <b-navbar-item
        tag="router-link"
        :to="{ name: 'products', params: { category: 'all' } }"
      >
        <img src="@/assets/logo.png" />
      </b-navbar-item>
    </template>
    <template slot="start"> </template>

    <template slot="end">
      <b-navbar-item v-if="!loggedIn" tag="div">
        <div class="buttons">
          <router-link :to="{ name: 'signup' }" class="button is-primary">
            <strong>Sign up</strong>
          </router-link>
          <router-link :to="{ name: 'signin' }" class="button is-light">
            Log in
          </router-link>
        </div>
      </b-navbar-item>
      <b-navbar-item tag="router-link" :to="{ name: 'cart' }" v-if="loggedIn">
        <!-- <router-link :to="{ name: 'cart' }" tag="a" class=""> -->
        <!-- v-bind:type="numOfItems > 0 ? 'is-primary' : 'is-dark'" -->
        <b-icon
          type="is-primary"
          v-bind:icon="numOfItems > 0 ? 'cart' : 'cart-outline'"
        >
        </b-icon>
        <span v-if="numOfItems > 0" class="tag badge is-primary">{{
          numOfItems
        }}</span>
        <!-- </router-link> -->
      </b-navbar-item>
      <b-navbar-dropdown v-if="loggedIn" :label="username">
        <b-navbar-item tag="router-link" :to="{ name: 'about' }">
          Profile
        </b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ name: 'orders' }">
          My Orders
        </b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ name: 'logout' }">
          Logout
        </b-navbar-item>
      </b-navbar-dropdown>
    </template>
    <template slot="burger">
      <a
        @click.prevent="toggle"
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </template>
  </b-navbar>
</template>

<script>
import { mapGetters, mapState } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters({
      loggedIn: 'auth/loggedIn',
    }),
    ...mapState({
      numOfItems: (state) => state.cart.items.length,
      username: (state) => state.User.user.username,
    }),
  },
  data: () => ({
    isBurgerActive: false,
  }),
  methods: {
    toggle() {
      this.isBurgerActive = !this.isBurgerActive
      this.$emit('ToggleSideBar')
    },
  },
}
</script>

<style lang="scss" scoped>
.badge {
  position: absolute;
  top: 9px;
  right: 2px;
  font-size: 0.6rem !important;
  font-weight: 500 !important;
  border-radius: 999px !important;
  font-size: 0.55rem !important;
  height: 1.7em !important;
  padding-left: 0.7em !important;
  padding-right: 0.7em !important;
}
</style>
