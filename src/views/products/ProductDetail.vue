<template>
  <div>
    <b-loading :active.sync="loading"></b-loading>
    <div class="columns is-hidden-mobile">
      <div class="column"></div>
    </div>
    <div v-if="error">
      <section class="section">
        <div class="content has-text-grey has-text-centered">
          <p>
            <b-icon icon-pack="fas" icon="ghost" size="is-large"> </b-icon>
          </p>
          <p>This product is not exist or not featured anymore</p>
        </div>
      </section>
    </div>
    <div v-else>
      <div class="columns is-vcentered is-gapless">
        <div class="column">
          <div class="box">
            <transition name="fade">
              <div v-if="!loading" class="columns is-gapless">
                <div class="column is-4">
                  <b-carousel
                    v-if="product.images.length"
                    :autoplay="false"
                    :indicator-inside="false"
                  >
                    <b-carousel-item
                      v-for="(image, i) in product.images"
                      :key="i"
                    >
                      <span class="image is-5by4">
                        <v-lazy-image
                          alt="Placeholder image"
                          :src="image.image"
                          :src-placeholder="
                            `https://i.picsum.photos/id/${product.id +
                              i +
                              10}/10/10.jpg`
                          "
                        />
                        <!-- <v-lazy-image
                          alt="Placeholder image"
                          :src="
                            `https://i.picsum.photos/id/${product.id +
                              i +
                              10}/600/400.jpg`
                          "
                        /> -->
                      </span>
                    </b-carousel-item>
                  </b-carousel>
                  <b-carousel
                    v-else
                    :autoplay="false"
                    :indicator-inside="false"
                  >
                    <b-carousel-item v-for="(item, i) in 4" :key="i">
                      <span class="image is-5by4">
                        <v-lazy-image
                          alt="Placeholder image"
                          :src="
                            `https://i.picsum.photos/id/${product.id +
                              i +
                              10}/300/300.jpg`
                          "
                          :src-placeholder="
                            `https://i.picsum.photos/id/${product.id +
                              i +
                              10}/20/20.jpg`
                          "
                        />
                        <!-- <v-lazy-image
                          alt="Placeholder image"
                          :src="
                            `https://i.picsum.photos/id/${product.id +
                              i +
                              10}/600/400.jpg`
                          "
                        /> -->
                      </span>
                    </b-carousel-item>
                  </b-carousel>
                </div>
                <div class="column">
                  <div class="">
                    <div class="card-content">
                      <div class="media">
                        <div class="">
                          <strong class="title is-5">{{ product.name }}</strong>
                          <p class="">
                            <small class="substitle is-6 rate">
                              <router-link
                                :to="{
                                  name: 'products',
                                  params: {
                                    category: product.category.slug,
                                  },
                                }"
                              >
                                {{ product.category.name }}</router-link
                              >
                            </small>
                          </p>
                          <span class="rate">
                            <b-taglist>
                              <b-tag ellipsis type="is-info">first</b-tag>
                              <b-tag type="is-info">second</b-tag>
                              <b-tag type="is-info">third</b-tag>
                              <b-tag type="is-info">fourth</b-tag>
                            </b-taglist>
                          </span>
                          <!-- <span class="rate">
                          <b-rate
                            v-model="rate"
                            icon-pack="mdi"
                            :show-score="true"
                            :disabled="true"
                          >
                          </b-rate>
                        </span> -->
                        </div>
                      </div>

                      <div class="level is-mobile">
                        <div class="level-left">
                          <div class="level-item">
                            <span class="has-text-grey">Price:</span>
                          </div>
                        </div>
                        <div class="level-right">
                          <div class="level-item">
                            <span class="title is-4 has-text-secondary "
                              >{{ product.price }}$</span
                            >
                          </div>
                        </div>
                      </div>
                      <div class="level is-mobile">
                        <div class="level-left">
                          <div class="level-item">
                            <span class="has-text-grey">QTY:</span>
                          </div>
                        </div>
                        <div class="level-right">
                          <div class="level-item">
                            <b-numberinput
                              min="1"
                              max="10"
                              v-model="qty"
                              type="is-primary"
                              size="is-small"
                              :editable="false"
                            ></b-numberinput>
                          </div>
                        </div>
                      </div>
                      <!-- <div class="level is-mobile">
                  <div class="level-left">
                    <div class="level-item">
                      <span class="has-text-grey">Color:</span>
                    </div>
                  </div>
                  <div class="level-right">
                    <div class="level-item">
                      <b-radio-button
                        v-model="radioButton"
                        native-value="green"
                        type="is-primary "
                      >
                        <span>Green</span>
                      </b-radio-button>

                      <b-radio-button
                        v-model="radioButton"
                        native-value="yellow"
                        type="is-primary"
                      >
                        <span>Yellow</span>
                      </b-radio-button>

                      <b-radio-button
                        v-model="radioButton"
                        native-value="blue"
                        type="is-primary"
                      >
                        Blue
                      </b-radio-button>
                    </div>
                  </div>
                </div> -->
                      <div class="level is-mobile">
                        <div class="level-left">
                          <a @click="setFocus" class="level-item">
                            <span class="icon has-text-primary"
                              ><i class="fas fa-reply"></i
                            ></span>
                          </a>
                        </div>
                        <div class="level-right">
                          <div class="level-item ">
                            <!-- <b-button
                        @click="addToCart(product)"
                        type="is-primary cart-btn"
                        >Add to Cart</b-button
                      > -->
                            <b-button
                              @click="addToCart(product, qty)"
                              ref="CartBtn"
                              type="is-primary cart-btn"
                            >
                              <span>Add to cart</span>
                              <div class="cart">
                                <svg viewBox="0 0 36 26">
                                  <polyline
                                    points="1 2.5 6 2.5 10 18.5 25.5 18.5 28.5 7.5 7.5 7.5"
                                  ></polyline>
                                  <polyline
                                    points="15 13.5 17 15.5 22 10.5"
                                  ></polyline>
                                </svg>
                              </div>
                            </b-button>
                          </div>
                          <div class="level-item">
                            <b-button
                              disabled
                              tag="router-link"
                              :to="{
                                name: 'cart',
                                params: { singleProduct: product },
                              }"
                              type="is-primary is-outlined"
                              >Buy Now</b-button
                            >
                          </div>
                        </div>
                      </div>

                      <!-- <div class="media">
                    <div class="media-content">
                      <p class="subtitle is-6">Price:</p>
                    </div>
                    <div class="media-right">
                      <div class="media-content">
                        <span class="title is-4 has-text-primary "
                          >{{ product.price }}$</span
                        >
                      </div>
                    </div>
                  </div> -->
                    </div>
                  </div>
                </div>
              </div>

              <div v-if="loading" class="columns is-gapless">
                <div class="column is-centered is-4">
                  <figure class="is-4by3">
                    <b-skeleton height="275px"></b-skeleton>
                  </figure>
                  <nav class="level is-mobile">
                    <div class="level-item">
                      <b-skeleton width="49px" height="49px"></b-skeleton>
                    </div>
                    <div class="level-item">
                      <b-skeleton width="49px" height="49px"></b-skeleton>
                    </div>
                    <div class="level-item">
                      <b-skeleton width="49px" height="49px"></b-skeleton>
                    </div>
                    <div class="level-item">
                      <b-skeleton width="49px" height="49px"></b-skeleton>
                    </div>
                    <div class="level-item">
                      <b-skeleton width="49px" height="49px"></b-skeleton>
                    </div>
                    <div class="level-item">
                      <b-skeleton width="49px" height="49px"></b-skeleton>
                    </div>
                  </nav>
                </div>
                <div class="column">
                  <div class="">
                    <div class="card-content">
                      <div class="">
                        <b-skeleton width="100%"></b-skeleton>
                        <p class="">
                          <b-skeleton width="80%"></b-skeleton>
                        </p>
                        <b-skeleton width="20%"></b-skeleton>
                      </div>
                      <br /><br /><br />
                      <div class="level is-mobile">
                        <div class="level-left">
                          <div class="level-item">
                            <b-skeleton width="50px"></b-skeleton>
                          </div>
                        </div>
                        <div class="level-right">
                          <div class="level-item">
                            <b-skeleton width="100px"></b-skeleton>
                          </div>
                        </div>
                      </div>
                      <div class="level is-mobile">
                        <div class="level-left">
                          <div class="level-item">
                            <b-skeleton width="30px"></b-skeleton>
                          </div>
                        </div>
                        <div class="level-right">
                          <div class="level-item">
                            <b-skeleton height="20px" width="20px"></b-skeleton>
                          </div>
                          <div class="level-item">
                            <b-skeleton width="40px"></b-skeleton>
                          </div>
                          <div class="level-item">
                            <b-skeleton height="20px" width="20px"></b-skeleton>
                          </div>
                        </div>
                      </div>
                      <div class="level is-mobile">
                        <div class="level-left">
                          <div class="level-item">
                            <b-skeleton height="30px" width="30px"></b-skeleton>
                          </div>
                        </div>
                        <div class="level-right">
                          <div class="level-item">
                            <b-skeleton
                              height="36px"
                              width="110px"
                            ></b-skeleton>
                          </div>
                          <div class="level-item">
                            <b-skeleton
                              height="36px"
                              width="100px"
                            ></b-skeleton>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </transition>
          </div>
        </div>
      </div>
      <div class="column box">
        <div class="card-content">
          <div v-if="(product.comments || []).length === 0">
            <article class="media">
              <div class="media-content">
                <div class="content">
                  <p>
                    <strong>No comments </strong>
                    <small>be the first one who comment</small>
                  </p>
                </div>
              </div>
            </article>
          </div>
          <article
            v-else
            v-for="(comment, index) in product.comments"
            :key="comment.id"
            class="media"
          >
            <figure class="media-left">
              <p class="image is-48x48">
                <img
                  class="is-rounded"
                  src="@/assets/images/product_image_small.png"
                />
              </p>
            </figure>
            <div class="media-content">
              <div class="content">
                <p>
                  <strong>{{ comment.user }}</strong>
                  <br />
                  <small>
                    {{ comment.content }}
                  </small>
                  <br />
                  <small>
                    <a
                      @click="
                        isOpen == comment.id
                          ? (isOpen = false)
                          : (isOpen = comment.id)
                      "
                      >Reply</a
                    >
                    ·
                    <span class="has-text-grey">{{
                      comment.created_at
                    }}</span></small
                  >
                </p>
              </div>
              <b-collapse
                slot="trigger"
                :open="isOpen == comment.id"
                @open="isOpen = comment.id"
                animation="slide"
              >
                <form @submit.prevent="PostComment(comment.id, reply, index)">
                  <b-field>
                    <b-input v-model="reply" placeholder="Write your reply">
                    </b-input>
                    <span class="control">
                      <b-button
                        native-type="submit"
                        icon-left="send"
                        class="is-primary"
                      >
                      </b-button>
                    </span>
                  </b-field>
                </form>
              </b-collapse>
              <article
                v-for="reply in comment.replies"
                :key="reply.id"
                class="media"
              >
                <figure class="media-left">
                  <p class="image is-48x48">
                    <img
                      class="is-rounded"
                      src="@/assets/images/product_image_small.png"
                    />
                  </p>
                </figure>
                <div class="media-content">
                  <div class="content">
                    <p>
                      <strong>{{ reply.user }}</strong>
                      <br />
                      {{ reply.content }}
                      <br />
                      <small
                        ><span class="has-text-grey">{{
                          reply.created_at
                        }}</span></small
                      >
                    </p>
                  </div>
                </div>
              </article>
            </div>
          </article>

          <article class="media">
            <div class="media-content">
              <form @submit.prevent="PostComment(null, comment)">
                <b-field>
                  <b-input
                    placeholder="Write your comment"
                    ref="comment"
                    style="width: 100%;"
                    v-model="comment"
                  >
                  </b-input>
                  <span class="control">
                    <b-button
                      native-type="submit"
                      value="Submit"
                      icon-left="send"
                      class="is-primary"
                      tag="button"
                    >
                    </b-button>
                  </span>
                </b-field>
              </form>
            </div>
          </article>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import productService from '@/services/productService'
export default {
  nema: 'product-detail',
  data() {
    return {
      product: {},
      loading: true,
      rate: 3.7,
      radioButton: 'green',
      qty: 1,
      comment: '',
      reply: '',
      isOpen: '',
      error: null,
    }
  },
  computed: {
    // calcQty() {
    //   this.qty++
    // },
  },
  created() {
    productService
      .fetchProduct(this.$route.params.slug)
      .then(({ data }) => {
        this.product = data
      })
      .catch((err) => {
        if (err.response.status === 404) this.error = err.response.status
      })
      .finally(() => {
        this.loading = false
      })
  },
  methods: {
    setFocus() {
      this.$refs.comment.$el.children[0].focus()
    },
    PostComment(parent, conent, index) {
      if (conent == '') return
      const comment = {
        parent: parent,
        product: this.product.id,
        content: conent,
      }
      productService
        .commentProduct(comment)
        .then(({ data }) => {
          if (parent) this.product.comments[index].replies.push(data)
          else this.product.comments.push(data)
        })
        .finally(() => {
          this.comment = ''
          this.reply = ''
          this.isOpen = false
        })
    },
    getImgUrl() {
      return `https://picsum.photos/id/504/500/384`
    },
    toast(product) {
      this.$buefy.toast.open({
        message: `Added ${this.qty} ${product.product_name} to cart`,
        type: 'is-secondary',
        position: 'is-top',
        closable: false,
        queue: false,
        indefinite: true,
      })
    },
    async addToCart(product) {
      const button = this.$refs.CartBtn.$el

      if (!button.classList.contains('loading')) {
        button.classList.add('loading')

        const p = {
          id: product.id,
          product_slug: product.slug,
          product_name: product.name,
          product_price: product.price,
          product_quantity: this.qty,
        }
        this.$store.dispatch('cart/addToCart', p).then(() => this.toast(p))
        setTimeout(() => {
          button.classList.remove('loading')
        }, 2500)
      }
    },
  },
}
</script>

<style scoped lang="scss">
.is-active .al img {
  filter: grayscale(0%);
}
.al img {
  filter: grayscale(100%);
}
.rate {
  margin: 0 0 0.6rem 0;
}
.qty-input {
  max-width: 30px;
}
.social {
  padding-bottom: 0.7rem;
  padding-top: 0.7rem;
}

.cart-btn {
  --text: #fff;
  --cart: #fff;
  --tick: var(--background);
  -webkit-appearance: none;
  -webkit-tap-highlight-color: transparent;
  mask-image: -webkit-radial-gradient(white, black);
  overflow: hidden;
  cursor: pointer;
  text-align: center;
  background: var(--background);
  transform: scale(var(--scale, 1));
  transition: transform 0.4s cubic-bezier(0.36, 1.01, 0.32, 1.27);
  &:active {
    --scale: 0.95;
  }
  span {
    font-size: 14px;
    font-weight: 500;
    display: block;
    position: relative;
    padding-left: 24px;
    margin-left: -8px;
    line-height: 26px;
    transform: translateY(var(--span-y, 0));
    transition: transform 0.7s ease;
    &:before,
    &:after {
      content: '';
      width: var(--w, 2px);
      height: var(--h, 14px);
      border-radius: 1px;
      position: absolute;
      left: var(--l, 8px);
      top: var(--t, 6px);
      background: currentColor;
      transform: scale(0.75) rotate(var(--icon-r, 0deg))
        translateY(var(--icon-y, 0));
      transition: transform 0.65s ease 0.05s;
    }
    &:after {
      --w: 14px;
      --h: 2px;
      --l: 2px;
      --t: 12px;
    }
  }
  .cart {
    position: absolute;
    left: 50%;
    top: 50%;
    margin: -13px 0 0 -18px;
    transform-origin: 12px 23px;
    transform: translateX(-120px) rotate(-18deg);
    &:before,
    &:after {
      content: '';
      position: absolute;
    }
    &:before {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      box-shadow: inset 0 0 0 2px var(--cart);
      bottom: 0;
      left: 9px;
      filter: drop-shadow(11px 0 0 var(--cart));
    }
    &:after {
      width: 16px;
      height: 9px;
      background: var(--cart);
      left: 9px;
      bottom: 7px;
      transform-origin: 50% 100%;
      transform: perspective(4px) rotateX(-6deg) scaleY(var(--fill, 0));
      transition: transform 1.2s ease var(--fill-d);
    }
    svg {
      z-index: 1;
      width: 36px;
      height: 26px;
      display: block;
      position: relative;
      fill: none;
      stroke: var(--cart);
      stroke-width: 2px;
      stroke-linecap: round;
      stroke-linejoin: round;
      polyline {
        &:last-child {
          stroke: var(--tick);
          stroke-dasharray: 10px;
          stroke-dashoffset: var(--offset, 10px);
          transition: stroke-dashoffset 0.4s ease var(--offset-d);
        }
      }
    }
  }
  &.loading {
    --scale: 0.95;
    --span-y: -32px;
    --icon-r: 180deg;
    --fill: 1;
    --fill-d: 0.8s;
    --offset: 0;
    --offset-d: 1.73s;
    .cart {
      animation: cart 2.5s linear forwards 0.2s;
    }
  }
}

@keyframes cart {
  12.5% {
    transform: translateX(-60px) rotate(-18deg);
  }
  25%,
  45%,
  55%,
  75% {
    transform: none;
  }
  50% {
    transform: scale(0.9);
  }
  44%,
  56% {
    transform-origin: 12px 23px;
  }
  45%,
  55% {
    transform-origin: 50% 50%;
  }
  87.5% {
    transform: translateX(70px) rotate(-18deg);
  }
  100% {
    transform: translateX(140px) rotate(-18deg);
  }
}

@media only screen and (max-width: 600px) {
  .box {
    padding: 0;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition-property: opacity;
  transition-duration: 0.25s;
}

.fade-enter-active {
  transition-delay: 0.25s;
}

.fade-enter,
.fade-leave-active {
  opacity: 0;
}
// Center & dribbble
</style>
