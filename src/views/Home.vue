<template>
  <div class="home">
    <HelloWorld msg="Hello there" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld,
  },
  beforeCreate() {
    this.$router.push({ name: 'products', params: { category: 'all' } })
  },
}
</script>
