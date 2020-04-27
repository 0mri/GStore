<template>
  <!-- <form @submit.prevent="signupUser">
    <div class="card">
      <div class="card-header">
        <p class="card-header-title">
          Sign Up
        </p>
      </div>
      <div class="card-content">
        <div class="content">
          <section>
            <b-field>
              <b-input
                placeholder="Username"
                maxlength="30"
                v-model="username"
              ></b-input>
            </b-field>

            <b-field>
              <b-input
                placeholder="Password"
                type="password"
                maxlength="30"
                v-model="password"
              ></b-input>
            </b-field>
            <b-field>
              <b-input
                placeholder="Repeat Password"
                type="password"
                maxlength="30"
                v-model="password2"
              ></b-input>
            </b-field>
            <b-field>
              <b-button
                :loading="loading"
                expanded
                native-type="submit"
                type="is-primary"
                >Sign Up</b-button
              >
            </b-field>
            <p>{{ this.error }}</p>
          </section>
        </div>
      </div>
    </div>
  </form> -->
  <form @submit.prevent="SignUpUser">
    <div class="header">
      <h1 class="title has-text-centered is-3 is-uppercase">
        Sign Up
        <hr />
      </h1>
    </div>
    <div class="content">
      <b-field :type="error ? 'is-danger' : null">
        <b-input
          required
          :disabled="this.loading"
          v-model="username"
          placeholder="Username"
          type="text"
        ></b-input>
      </b-field>
      <b-field :type="error ? 'is-danger' : null">
        <b-input
          required
          :disabled="this.loading"
          v-model="password"
          placeholder="Password"
          type="password"
        ></b-input>
      </b-field>
      <b-field :type="error ? 'is-danger' : null">
        <b-input
          required
          :disabled="this.loading"
          v-model="password2"
          placeholder="Repeat Password"
          type="password"
        ></b-input>
      </b-field>
      <b-field>
        <b-button
          :loading="loading"
          native-type="submit"
          type="is-primary is-small is-uppercase is-fullwidth"
          >Sign Up</b-button
        >
      </b-field>
      <!-- <b-field>
        <b-button
          type="is-second is-small is-uppercase is-fullwidth"
          >Sign up with Google</b-button
        >
      </b-field>
      <b-field>
        <b-button
          type="is-twitter is-small is-uppercase is-fullwidth"
          >Sign up with Facebook</b-button
        >
      </b-field> -->
    </div>

    <footer>
      <hr />
      <div class="level">
        <div class="level-item">
          <span>
            Already signed up?
            <router-link to="login">Sign In</router-link>
          </span>
        </div>
      </div>
    </footer>
  </form>
</template>

<script>
// import axios from "axios";
export default {
  data() {
    return {
      username: '',
      password: '',
      password2: '',
      error: '',
      loading: false,
    }
  },
  methods: {
    SignUpUser() {
      if (this.password === this.password2) {
        this.loading = true
        this.$store
          .dispatch('auth/registerUser', {
            username: this.username,
            password: this.password,
            confirm: this.password2,
          })
          .then(() =>
            this.$store
              .dispatch('auth/loginUser', {
                username: this.username,
                password: this.password,
              })
              .then(() => {
                this.$router.push(
                  { name: 'products', params: { category: 'all' } },
                  () => {
                    this.Notify('Registeration Success', 'is-success')
                  }
                )
              })
          )
          .catch(({ response }) => {
            this.error = true
            const err = response.data
            if (err.username) this.Notify(err.username[0], 'is-danger')
            else if (err.password) this.Notify(err.password[0], 'is-danger')
          })
          .finally(() => (this.loading = false))
      } else {
        this.error = true
        this.Notify("Passwords don't match", 'is-danger')
      }
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
