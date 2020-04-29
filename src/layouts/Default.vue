<template>
  <div>
    <div class="im-fullheight-nav">
      <div class="container">
        <vue-page-transition name="fade">
          <slot />
        </vue-page-transition>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {},
}
</script>

<style></style>
