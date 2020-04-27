<template>
  <!-- <form @submit.prevent="loginUser">
    <div class="card">
      <div class="card-header">
        <p class="card-header-title">
          Login
        </p>
      </div>
      <div class="card-content">
        <div class="content">
          <b-field>
            <b-button expanded type="is-facebook" icon-left="facebook"
              >Login with Facebook</b-button
            >
          </b-field>
          <b-field>
            <b-button
              @click="AuthProvider('google')"
              expanded
              type="is-google"
              icon-left="google"
              >Login with Google</b-button
            >
          </b-field>
          <br />
          <section>
            <b-field :type="error ? 'is-danger' : null">
              <b-input
                placeholder="Username"
                maxlength="30"
                v-model="user.username"
              ></b-input>
            </b-field>
            <b-field :type="error ? 'is-danger' : null">
              <b-input
                placeholder="Password"
                type="password"
                maxlength="30"
                v-model="user.password"
              ></b-input>
            </b-field>

            <b-field>
              <b-button
                :loading="loading"
                native-type="submit"
                type="is-primary"
                expanded
                >Login</b-button
              >
            </b-field>
          </section>
        </div>
      </div>
    </div>
  </form> -->
  <form class="form" @submit.prevent="loginUser">
    <div class="header">
      <h1 class="title has-text-centered is-3 is-uppercase">
        Sign In
        <hr />
      </h1>
    </div>

    <div class="content">
      <b-field :type="error ? 'is-danger' : null">
        <b-input
          :disabled="this.loading"
          v-model="user.username"
          placeholder="Username"
          type="text"
        ></b-input>
      </b-field>
      <b-field :type="error ? 'is-danger' : null">
        <b-input
          :disabled="this.loading"
          v-model="user.password"
          placeholder="Password"
          type="password"
        ></b-input>
      </b-field>
      <b-field style="float: left; margin-bottom: 1.75rem">
        <b-checkbox disabled size="is-small">Stay sign in?</b-checkbox>
      </b-field>
      <b-field>
        <b-button
          :loading="loading"
          native-type="submit"
          :disabled="this.loading"
          type="is-primary is-small is-uppercase is-fullwidth"
          >Sign In</b-button
        >
      </b-field>
    </div>

    <footer>
      <hr />
      <div class="level">
        <div class="level-item">
          <span>
            Don't have an account?
            <router-link :to="{ name: 'signup' }">Sign Up</router-link>
          </span>
        </div>
      </div>
    </footer>
  </form>
</template>

<script>
// import VueSocialauth from 'vue-social-auth'
// import axios from "axios";
export default {
  name: 'login',
  components: {},
  data() {
    return {
      user: {
        username: '',
        password: '',
      },
      error: false,
      loading: false,
    }
  },
  methods: {
    AuthProvider(provider) {
      var self = this

      this.$auth
        .authenticate(provider)
        .then((response) => {
          self.SocialLogin(provider, response)
        })
        .catch(() => {
          // console.log({ err: err })
        })
    },
    loginUser() {
      this.loading = true
      this.error = false
      this.$store
        .dispatch('auth/loginUser', this.user)
        .then(() => {
          this.error = false
          this.$router.push(
            { name: 'products', params: { category: 'all' } },
            () => {
              this.Notify(`Wellcome back ${this.user.username}`, 'is-success')
            }
          )
        })
        .catch(() => {
          this.Notify('Incorrect credentials try again', 'is-danger')
          this.error = true // if the credentials were wrong set wrongCred to true
          this.user.username = ''
          this.user.password = ''
        })
        .finally(() => {
          this.loading = false
        })
    },
    Notify(message, type) {
      this.$buefy.toast.open({
        duration: 2500,
        message: message,
        position: 'is-top',
        type: type,
      })
    },
  },
}
</script>

<style></style>
