<template>
  <section class="section">
    <div class="columns">
      <div class="column has-text-centered">
        <div class="content response">
          <div v-scroll-reveal="{ delay: 50 }" class="icon">
            <img
              v-if="data.status === 'success'"
              src="@/assets/images/success.svg"
              alt=""
            />
            <img v-else src="@/assets/images/fail.svg" alt="" />
          </div>

          <h1 v-scroll-reveal="{ delay: 200 }">{{ data.header }}</h1>
          <section>
            <h6 v-scroll-reveal="{ delay: 300 }">{{ data.message }}</h6>

            <strong v-scroll-reveal="{ delay: 400 }"
              >Transaction ID: {{ data.transaction.id }}</strong
            >
            <br />
            <strong v-scroll-reveal="{ delay: 500 }"
              >Amount: {{ data.transaction.amount }}$ USD</strong
            >
          </section>

          <div v-scroll-reveal="{ delay: 600 }">
            <section class="section" v-if="data.status === 'success'">
              <b-field>
                <b-button
                  tag="router-link"
                  :to="{ name: 'products', params: { category: 'all' } }"
                  type="is-success"
                  >Continue Shopping</b-button
                >
              </b-field>
              <b-field> </b-field>
            </section>
            <section v-else>
              <b-field>
                <b-button
                  tag="router-link"
                  :to="{ name: 'products', params: { category: 'all' } }"
                  type="is-success"
                  >Continue Shopping</b-button
                >
              </b-field>
              <b-field>
                <b-button
                  tag="router-link"
                  :to="{ name: 'orders' }"
                  type="is-info"
                  >My Orders</b-button
                >
              </b-field>
              <b-field>
                <b-button
                  tag="router-link"
                  :to="{ name: 'cart' }"
                  type="is-warning"
                  >Try Again</b-button
                >
              </b-field>
            </section>
          </div>
        </div>
      </div>
    </div>

    <!-- <section v-scroll-reveal="{ delay: 800 }" class="section">
      <aside class="drawer dark">
        <article class="content compact">
          <section>
            <h5>Transaction</h5>
            <table cellpadding="0" cellspacing="0">
              <tbody>
                <tr>
                  <td>ID</td>
                  <td>{{ data.transaction.id }}</td>
                </tr>
                <tr>
                  <td>Amount</td>
                  <td>{{ data.transaction.amount }}$</td>
                </tr>
                <tr>
                  <td>Date</td>
                  <td>
                    {{
                      new Date(data.transaction.created_at).toLocaleString(
                        'en-GB'
                      )
                    }}
                  </td>
                </tr>
              </tbody>
            </table>
          </section>

          <section>
            <h5>Payment</h5>

            <table cellpadding="0" cellspacing="0">
              <tbody>
                <tr>
                  <td>last_4</td>
                  <td>{{ data.transaction.credit_card_details.last_4 }}</td>
                </tr>
                <tr>
                  <td>card_type</td>
                  <td>{{ data.transaction.credit_card_details.card_type }}</td>
                </tr>
                <tr>
                  <td>expiration_date</td>
                  <td>
                    {{ data.transaction.credit_card_details.expiration_date }}
                  </td>
                </tr>
                <tr>
                  <td>cardholder_name</td>
                  <td>
                    {{ data.transaction.credit_card_details.cardholder_name }}
                  </td>
                </tr>
              </tbody>
            </table>
          </section>

          <section v-if="data.transaction.customer_details">
            <h5>Customer Details</h5>
            <table cellpadding="0" cellspacing="0">
              <tbody>
                <tr>
                  <td>id</td>
                  <td>{{ data.transaction.customer_details.id }}</td>
                </tr>
                <tr>
                  <td>first_name</td>
                  <td>{{ data.transaction.customer_details.first_name }}</td>
                </tr>
                <tr>
                  <td>last_name</td>
                  <td>{{ data.transaction.customer_details.last_name }}</td>
                </tr>
                <tr>
                  <td>email</td>
                  <td>{{ data.transaction.customer_details.email }}</td>
                </tr>
                <tr>
                  <td>company</td>
                  <td>{{ data.transaction.customer_details.company }}</td>
                </tr>
                <tr>
                  <td>website</td>
                  <td>{{ data.transaction.customer_details.website }}</td>
                </tr>
                <tr>
                  <td>phone</td>
                  <td>{{ data.transaction.customer_details.phone }}</td>
                </tr>
                <tr>
                  <td>fax</td>
                  <td>{{ data.transaction.customer_details.fax }}</td>
                </tr>
              </tbody>
            </table>
          </section>
        </article>
      </aside>
    </section> -->
  </section>
</template>

<script>
export default {
  data() {
    return {
      data: this.$route.params.data,
    }
  },
  created() {
    if (!this.data) this.$router.push('/')
  },
}
</script>

<style scoped>
.icon {
  width: 100px;
  height: 100px;
}
</style>
