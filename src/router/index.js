import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'signin',
    component: () => import('../views/Login.vue'),
    meta: {
      requiresLogged: true,
    },
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/Signup.vue'),
    meta: {
      requiresLogged: true,
    },
  },
  {
    path: '/logout',
    name: 'logout',
    component: () => import('../views/Logout.vue'),
  },
  {
    path: '/about/',
    name: 'about',
    component: () => import('../views/About.vue'),
    meta: {
      requiresAuth: true,
    },
  },

  //PRODUCT
  {
    path: '/products/:category?/:page?',
    name: 'products',
    component: () => import('../views/products/Category.vue'),
    meta: {
      requiresAuth: true,
      layout: 'default',
    },
  },
  {
    path: '/product/:slug',
    name: 'product-detail',
    component: () => import('../views/products/ProductDetail.vue'),
    meta: {
      requiresAuth: true,
      layout: 'default',
    },
  },
  //CART
  // {
  //   path: '/products/',
  //   name: 'products',
  //   component: () => import('../views/cart/Products.vue'),
  //   // meta: {
  //   //   requiresAuth: true
  //   // }
  // },
  {
    path: '/cart/',
    name: 'cart',
    component: () => import('../views/cart/MyCart.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/cart/checkout/',
    name: 'checkout',
    component: () => import('../views/cart/Checkout.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/checkout/',
    name: 'checkout-show',
    component: () => import('../views/cart/CheckoutShow.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/orders/',
    name: 'orders',
    component: () => import('../views/cart/Orders.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/order/:id/',
    name: 'order-detail',
    component: () => import('../views/cart/DetailOrder.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  //oAUTH
  {
    path: '/auth/:provider/callback',
    component: {
      template: '<div class="auth-component"></div>',
    },
  },
  {
    path: '/*',
    name: '404',
    component: () => import('../views/404.vue'),
    meta: {
      requiresAuth: true,
    },
  },
]

const router = new VueRouter({
  mode: 'history',
  linkActiveClass: 'is-active',
  base: process.env.BASE_URL,
  routes,
})

export default router
