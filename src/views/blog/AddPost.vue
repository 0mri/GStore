<template>
  <section class="section">
    <h1>Add Post</h1>
    <div class="columns">
      <div class="column">
        <b-field label="Title" label-position="on-border">
          <b-input v-model="post.title" type="text"> </b-input>
        </b-field>
        <b-field label="Body" label-position="on-border">
          <b-input v-model="post.body" type="textarea"> </b-input>
        </b-field>
        <b-field>
          <b-button @click="submit" :loading="loading" type="is-primary">
            Submit Post
          </b-button>
        </b-field>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      post: {
        title: '',
        body: ''
      },
      loading: false
    }
  },
  methods: {
    submit() {
      this.loading = true
      setTimeout(() => {
        axios
          .post('api/blog/posts/', this.post)
          .then(() => {
            //   console.log(res)
          })
          .catch(err => {
            this.$buefy.toast.open({
              message: err,
              type: 'is-danger',
              queue: false
            })
          })
          .finally(() => {
            this.loading = false
          })
      }, 300)
    }
  }
}
</script>

<style></style>
