<template>
  <section class="section">
    <span v-if="error">{{ error }}</span>
    <b-table
      :loading="isLoading"
      :data="order"
      ref="table"
      :opened-detailed="defaultOpenedDetails"
      detailed
      :detail-key="order.product"
      :show-detail-icon="true"
    >
      <template slot-scope="props">
        <b-table-column field="id" label="#" width="40" numeric>
          <b>{{ props.row.product.id }}</b>
        </b-table-column>

        <b-table-column field="product.name" label="Product Name">
          <template>
            <a @click="toggle(props.row)">
              {{ props.row.product.name }}
            </a>
          </template>
        </b-table-column>

        <!-- <b-table-column field="date" label="Date" sortable centered>
          <span class="tag is-success">
            {{ new Date(props.row.created_at).toLocaleDateString() }}
          </span>
        </b-table-column> -->

        <b-table-column field="quantity" label="Quantity">
          <span class="tag is-success">
            {{ props.row.quantity }}
          </span>
        </b-table-column>
        <b-table-column field="product.price" label="Price">
          <span> {{ props.row.product.price }} </span>
        </b-table-column>
      </template>

      <template slot="detail" slot-scope="props">
        <article class="media">
          <figure class="media-left">
            <p class="image is-64x64">
              <v-lazy-image
                alt="Placeholder image"
                :src="
                  `https://picsum.photos/id/${props.row.product.id +
                    10}/128/128.jpg`
                "
              />
              <!-- <img
                src="https://buefy.org//static/img/placeholder-128x128.png"
              /> -->
            </p>
          </figure>
          <div class="media-content">
            <div class="content">
              <p>
                <strong>
                  <router-link
                    :to="{
                      name: 'product-detail',
                      params: {
                        slug: props.row.product.slug,
                      },
                    }"
                  >
                    {{ props.row.product.name }}</router-link
                  >
                </strong>
                <br />
                <small class="">
                  <router-link
                    :to="{
                      name: 'products',
                      params: {
                        category: props.row.product.category.slug,
                      },
                    }"
                    >{{ props.row.product.category.name }}
                  </router-link>
                </small>
                <br />
                {{ props.row.product.description }}
              </p>
            </div>
          </div>
        </article>
      </template>
    </b-table>
  </section>
</template>

<script>
export default {
  name: 'detail-order',
  data() {
    return {
      order: [],
      defaultOpenedDetails: [],
      isLoading: true,
      error: '',
    }
  },
  created() {
    this.$store
      .dispatch('orders/getDetailOrder', this.$route.params.id)
      .then((order) => (this.order = order.orderitem_set))
      .catch(({ response }) => (this.error = response.data.detail))
      .finally(() => (this.isLoading = false))
  },
  methods: {
    toggle(row) {
      this.$refs.table.toggleDetails(row)
    },
  },
}
</script>

<style></style>
