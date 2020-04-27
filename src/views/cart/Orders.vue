<template>
  <section class="section">
      <b-table
        :data="false ? [] : orders"
        :striped="true"
        :hoverable="isHoverable"
        :loading="isLoading"
        :mobile-cards="true"
      >
        <template slot-scope="props">
          <b-table-column field="id" label="Order ID">
            <b>{{ props.row.id }}</b>
          </b-table-column>
          <b-table-column field="date" label="Date" width="40">
            {{ new Date(props.row.created_at).toLocaleDateString('en-GB') }}
          </b-table-column>

          <b-table-column field="name" label="Name">
            {{ props.row.owner }}
          </b-table-column>

          <!-- <b-table-column field="date" label="Date" centered>
                    <span class="tag is-success">
                        {{ new Date(props.row.date).toLocaleDateString() }}
                    </span>
                </b-table-column> -->

          <b-table-column label="Status">
            <span :class="computedStatus(props.row.status)">
              {{ props.row.status }}
            </span>
            <span></span>
          </b-table-column>
          <b-table-column field="price" label="Price">
            {{ props.row.order_total }}$
          </b-table-column>
          <b-table-column label="View Order">
            <b-button
              tag="router-link"
              :to="{
                name: 'order-detail',
                params: {
                  id: props.row.id,
                  url: props.row.url,
                },
              }"
              size="is-small"
              type="is-info is-outlined"
              icon-right="eye"
            />
          </b-table-column>
        </template>

        <template :slot="!isLoading ? 'empty' : ''">
          <section class="section">
            <div class="content has-text-grey has-text-centered">
              <p>
                <b-icon icon="emoticon-sad" size="is-large"> </b-icon>
              </p>
              <p>You dont have any orders yet</p>
              <b-button
                tag="router-link"
                :to="{ name: 'products', params: { category: 'all' } }"
                type="is-success"
                >Start Shopping</b-button
              >
            </div>
          </section>
        </template>
      </b-table>

    <!-- <div v-if="orders.length" class="">
      <div class="columns is-centered">
        <div class="column">
          <p class="">Total Price: {{ sumItems }}$</p>
        </div>
      </div>
      <div class="columns is-centered">
        <div class="column">
          <b-button @click="orderCart(cart)" type="is-primary">
            Order Now!
          </b-button>
        </div>
      </div>
    </div> -->
  </section>
</template>

<script>
export default {
  computed: {},
  data() {
    return {
      orders: [],
      isHoverable: true,
      isLoading: true,
    }
  },
  created() {
    this.$store
      .dispatch('orders/getAllOrders')
      .then((orders) => (this.orders = orders))
      .finally(() => (this.isLoading = false))
  },
  methods: {
    computedStatus(status) {
      if (status == 'created') return 'tag is-warning'
      else if (status == 'paid') return 'tag is-info'
      else if (status == 'shipped') return 'tag is-success'
      else if (status == 'refunded') return 'tag is-danger'
      return ''
    },
  },
}
</script>

<style></style>
