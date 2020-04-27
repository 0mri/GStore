<template>
  <div class="log"></div>
</template>

<script>
export default {
  created() {
    this.$store.dispatch('auth/logoutUser').then(() => {
      this.$router.push({ name: 'signin' })
    })
  }
}
</script>

<style scoped></style>
