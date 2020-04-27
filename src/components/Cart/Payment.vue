<template>
  <div class="columns is-gapless is-centered">
    <div class="column is-6">
      <b-loading :is-full-page="true" :active.sync="isLoading"> </b-loading>
      <div v-show="!isLoading">
        <div class="box has-text-centered">
          <div id="dropin-container"></div>
          <b-button
            v-show="!isLoading"
            :loading="loadingButton"
            :type="error ? 'is-danger' : 'is-info'"
            id="submit-button"
            >Pay Now</b-button
          >
        </div>
        <span class="tag is-danger" v-if="error">{{
          error.response.data.error
        }}</span>
        <!-- <section>
          <form @submit.prevent="loginUser">
            <div class="header">
              <h1 class="title has-text-centered is-3 is-uppercase">
                Checkout
                <hr />
              </h1>
            </div>

            <div class="">
              <b-field label="Cardholder Name">
                <b-input
                v-model="card.holderName"
                  class="credit-card"
                  placeholder="Cardholder Name"
                  type="text"
                ></b-input>
              </b-field>
              <b-field label="Card Number" :type="error ? 'is-danger' : null">
                <b-input
                  v-model="card.number"
                  v-cleave="{
                    creditCard: true,

                    onCreditCardTypeChanged: cardChanged,
                  }"
                  placeholder="•••• •••• •••• ••••"
                  type="tel"
                ></b-input>
                {{ cardType }}
              </b-field>
              <b-field grouped>
                <b-field expanded label="Expiration Date">
                  <b-input
                    v-model="card.expDate"
                    v-cleave="{ date: true, datePattern: ['m', 'y'] }"
                    placeholder="MM/YY"
                    type="tel"
                  ></b-input>
                </b-field>
                <b-field label="CVV" expanded>
                  <b-input v-model="card.cvv" type="tel" maxlength="4" placeholder="•••"></b-input>
                </b-field>
              </b-field>
            </div>

            <footer class="has-text-centered">
              <hr />
              <b-button
                expanded
                v-show="!isLoading"
                :loading="loadingButton"
                :type="error ? 'is-danger' : 'is-info'"
                id="submit-button"
                >Pay Now</b-button
              >
            </footer>
          </form>
        </section> -->
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import Cleave from 'cleave.js'
import { mapState } from 'vuex'
const cleave = {
  name: 'cleave',
  bind(el, binding) {
    const input = el.querySelector('input')
    input._vCleave = new Cleave(input, binding.value)
  },
  unbind(el) {
    const input = el.querySelector('input')
    input._vCleave.destroy()
  },
}
export default {
  directives: { cleave },
  name: 'payment',
  props: {
    client_token: String,
  },

  data() {
    return {
      isCreditCart: false,
      isLoading: true,
      loadingButton: false,
      error: '',
      card: {
        number: '',
        holderName: '',
        cvv: '',
        expDate: '',
      },
      cardType: '',
    }
  },
  computed: mapState({
    cart: (state) => state.cart.items,
  }),
  methods: {
    cardChanged(type) {
      this.cardType = type
    },
  },
  created() {
    const braintree = require('braintree-web-drop-in')
    // console.log(this.cart)

    braintree
      .create({
        authorization: this.client_token,
        container: '#dropin-container',
        // paypal: {
        //   flow: 'checkout',
        //   value: '11',
        // },
        card: {
          cardholderName: {
            required: true,
          },
        },
      })
      .then((instance) => {
        this.isLoading = false
        document
          .querySelector('#submit-button')
          .addEventListener('click', () => {
            instance.requestPaymentMethod((err, payload) => {
              this.loadingButton = true
              if (err) {
                this.loadingButton = false
                return
              }
              // Submit payload.nonce to your server
              this.$store
                .dispatch('cart/CheckOutCart', payload.nonce)
                .then(({ data }) =>
                  // get success/fail transaction page
                  this.$router.push({
                    name: 'checkout-show',
                    hash: '/#' + data.status,
                    params: { data: data },
                  })
                )
                .catch((error) => {
                  this.loadingButton = false
                  this.error = error
                })
            })
          })
      })
  },
}
</script>

<style>
.braintree-sheet {
  border: unset;
  border-radius: unset;
}
</style>
