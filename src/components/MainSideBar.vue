<template>
  <section>
    <b-sidebar
      type="is-light"
      :fullheight="fullheight"
      :fullwidth="fullwidth"
      :overlay="overlay"
      :right="right"
      :open.sync="open"
    >
      <div class="p-1">
        <b-menu ref="menu">
          <article v-if="loggedIn" class="media">
            <figure class="media-left">
              <p class="image">
                <router-link :to="{ name: 'about' }">
                  <img
                    class="is-rounded image is-32x32"
                    :src="user.profile_image"
                  />
                </router-link>
              </p>
            </figure>

            <div class="media-content">
              <div class="content">
                <p>
                  <strong
                    ><router-link :to="{ name: 'about' }">{{
                      user.username
                    }}</router-link>
                  </strong>
                </p>
                <br />
              </div>
            </div>
            <div class="media-right">
              <button @click="open = false" class="delete"></button>
            </div>
          </article>
          <b-menu-list v-if="loggedIn" label="Menu">
            <b-menu-item
              tag="router-link"
              icon="account"
              :to="{ name: 'about' }"
              label="Profile"
            ></b-menu-item>
            <b-menu-item
              tag="router-link"
              :to="{ name: 'cart' }"
              icon="cart"
              label="My Cart"
            ></b-menu-item>
            <b-menu-item
              tag="router-link"
              :to="{ name: 'products', params: { category: 'all' } }"
              icon="sitemap"
              label="Products"
            ></b-menu-item>
            <b-menu-item
              tag="router-link"
              :to="{ name: 'orders' }"
              icon="bag-personal"
              label="My Orders"
            ></b-menu-item>
          </b-menu-list>
          <b-menu-list label="Actions">
            <b-menu-item
              v-if="loggedIn"
              tag="router-link"
              :to="{ name: 'logout' }"
              label="Logout"
            ></b-menu-item>
            <b-menu-item
              v-if="!loggedIn"
              tag="router-link"
              :to="{ name: 'signin' }"
              label="Log in"
            ></b-menu-item>
            <b-menu-item
              v-if="!loggedIn"
              tag="router-link"
              :to="{ name: 'signup' }"
              label="Sign up"
            ></b-menu-item>
          </b-menu-list>
        </b-menu>
      </div>
    </b-sidebar>
  </section>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
export default {
  name: 'main-side-bar',
  data() {
    return {
      open: false,
      overlay: true,
      fullheight: true,
      fullwidth: false,
      right: false,
    }
  },
  computed: {
    ...mapGetters({
      loggedIn: 'auth/loggedIn',
    }),
    ...mapState({
      numOfItems: (state) => state.cart.items.length,
      user: (state) => state.User.user,
    }),
  },
  methods: {
    ToggleSideBar() {
      this.open = !this.open
    },
  },
  mounted() {
    const menuItems = this.$refs.menu.$children
    menuItems.forEach((menuItem) => {
      menuItem.$el.addEventListener('click', () => {
        this.open = false
      })
    })
  },
}
</script>

<style scoped>
.p-1 {
  padding: 1em;
}
.b-sidebar .sidebar-background {
  z-index: 41 !important;
}
</style>
