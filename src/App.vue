<template>
  <div id="app">
    <NavBar @ToggleSideBar="$refs.sidebar.ToggleSideBar()" />
    <MainSideBar ref="sidebar" />
    <component class="background" :is="layout">
      <router-view />
    </component>
  </div>
</template>
<script>
import MainSideBar from './components/MainSideBar'
import NavBar from '@/components/NavBar'
const default_layout = 'default'
export default {
  computed: {
    layout() {
      return (this.$route.meta.layout || default_layout) + '-layout'
    },
  },
  components: {
    MainSideBar,
    NavBar,
  },
  mounted() {},
}
</script>
<style lang="scss">
.background {
  background-color: #f7f7f7;
}
html {
  scroll-behavior: smooth;
}
.im-fullheight-nav {
  min-height: calc(100vh - 3.25rem);
}
.im-vcentered {
  display: flex !important;
  align-items: center;
}
.im-fullheight {
  min-height: calc(100vh);
}
.button {
  border-radius: 0px !important;
}
.input {
  transition: 0.3s !important;
  border-radius: 0 !important;
  // border-color: lighten($primary, 15%) !important;
}
.input:hover {
  border-color: lighten($primary, 5%) !important;
}

.v-lazy-image {
  filter: blur(2px);
  transition: filter 0.5s;
}
.v-lazy-image-loaded {
  filter: blur(0px);
}
.image {
  object-fit: cover !important;
}
</style>
