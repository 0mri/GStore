<template>
  <section>
    <b-carousel>
      <b-carousel-item>
        <section :class="`hero is-medium is-primary`">
          <div class="hero-body has-text-centered">
            <h1 class="title">
              {{ `Welcome ${username}` }}
            </h1>
          </div>
        </section>
      </b-carousel-item>
    </b-carousel>
    <div v-if="error">
      <p>{{ error }}</p>
    </div>
    <!-- <section class="section">
      <div class="title">
        Hot Products
      </div>
    </section>
    <b-carousel-list v-model="test" :data="items" :items-to-show="3">
      <template slot="item" slot-scope="props">
        <div class="card">
          <div class="card-image">
            <figure class="image is-4by3">
              <a @click="info(props.index)"><img :src="props.list.image"/></a>
            </figure>
            <b-tag type="is-danger" rounded style="position: absolute; top: 0;"
              ><b>50%</b></b-tag
            >
          </div>
          <div class="card-content">
            <div class="content">
              <p class="title is-6">{{ props.list.title }}</p>
              <p class="subtitle is-7">@johnsmith</p>
              <div class="field is-grouped">
                <p class="control" v-if="props.list.rating">
                  <b-rate :value="props.list.rating" show-score disabled />
                </p>
                <p class="control" style="margin-left: auto">
                  <button class="button is-small is-danger is-outlined">
                    <b-icon size="is-small" icon="heart" />
                  </button>
                </p>
              </div>
            </div>
          </div>
        </div>
      </template>
    </b-carousel-list> -->
  </section>
</template>

<script>
// import Search from './Search'
// import axios from 'axios'
import { mapGetters, mapState } from 'vuex'
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  computed: {
    ...mapGetters('auth', ['accessToken']),
    ...mapState('User', ['user']),
    username() {
      return this.user ? this.user.username : 'guest'
    },
  },
  components: {
    // Search,
  },
  created() {
    if (this.accessToken != null) {
      // axios
      //   .get('api/blog/posts/')
      //   .then(({ data }) => {
      //     this.loading = false
      //     if (data) this.posts = data
      //   })
      //   .catch((err) => {
      //     this.error = err.response.statusText
      //   })
      //   .finally(() => {
      //     this.loading = false
      //   })
    }
  },
  data() {
    return {
      loading: false,
      error: false,
      posts: [],
      test: 0,
      items: [
        {
          title: 'Slide 1',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
          rating: 4.4,
        },
        {
          title: 'Slide 2',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
          rating: 3.5,
        },
        {
          title: 'Slide 3',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
          rating: 5,
        },
        {
          title: 'Slide 4',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
        },
        {
          title: 'Slide 5',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
          rating: 5,
        },
        {
          title: 'Slide 6',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
          rating: 4,
        },
        {
          title: 'Slide 7',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
          rating: 2.7,
        },
        {
          title: 'Slide 8',
          image: 'https://buefy.org/static/img/placeholder-1280x960.png',
          rating: 1.5,
        },
      ],
    }
  },
  methods: {
    info(value) {
      this.test = value
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss"></style>
