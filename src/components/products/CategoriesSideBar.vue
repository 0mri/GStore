<template>
  <!-- <b-menu>
    <b-menu-list label="Categories">
      <b-menu-item
        tag="router-link"
        :to="{
          name: 'products',
          params: {
            category: 'all',
          },
        }"
        :active="isActive"
        label="All"
      ></b-menu-item>
      <b-menu-item tag="a" :active="false" :expanded="true">
        <template slot="label" slot-scope="props">
          Home
          <b-icon
            class="is-pulled-right"
            :icon="props.expanded ? 'menu-up' : 'menu-down'"
          ></b-icon>
        </template>
        <b-menu-item
          v-for="category in categories"
          :key="category.slug"
          :label="category.name"
          :active="isActive"
          tag="router-link"
          :to="{ name: 'products', params: { category: category.slug } }"
        >
        </b-menu-item>
      </b-menu-item>
    </b-menu-list>
  </b-menu> -->
  <b-sidebar
    type="is-light"
    position="fixed"
    :fullheight="fullheight"
    :fullwidth="false"
    :overlay="overlay"
    :right="right"
    :open.sync="open"
    mobile="is-fullwidth"
  >
    <div class="p-1">
      <b-menu ref="menu">
        <b-menu-list ref="menulist" label="Categories">
          <b-menu-item
            tag="router-link"
            :to="{
              name: 'products',
              params: {
                category: 'all',
              },
            }"
            :active="isActive"
            label="All"
          ></b-menu-item>
          <b-menu-item
            v-for="category in categories"
            :key="category.slug"
            :label="category.name"
            :active="isActive"
            tag="router-link"
            :to="{ name: 'products', params: { category: category.slug } }"
          >
          </b-menu-item>
        </b-menu-list>
      </b-menu>
    </div>
  </b-sidebar>
</template>

<script>
export default {
  name: 'cat-side-bar',
  props: {
    categories: Array,
  },
  data() {
    return {
      loading: true,
      isActive: false,
      overlay: true,
      fullheight: true,
      fullwidth: false,
      right: false,
      open: false,
    }
  },

  mounted() {},
  beforeUpdate() {
    let menuItems = this.$refs.menu.$children
    for (var i = 0; i < menuItems.length; ++i) {
      menuItems[i].$el.addEventListener('click', () => {
        this.open = false
      })
    }
  },
}
</script>

<style scoped lang="scss">
// .p-1 {
//   padding: 0.5em;
// }
// li {
//   text-align: left;
// }
.p-1 {
  padding: 1em;
}
@media screen and (max-width: 1023px) {
  .b-sidebar {
    .sidebar-content {
      &.is-mini-mobile {
        &:not(.is-mini-expand),
        &.is-mini-expand:not(:hover) {
          .menu-list {
            li {
              a {
                span:nth-child(2) {
                  display: none;
                }
              }
              ul {
                padding-left: 0;
                li {
                  a {
                    display: inline-block;
                  }
                }
              }
            }
          }
          .menu-label:not(:last-child) {
            margin-bottom: 0;
          }
        }
      }
    }
  }
}
@media screen and (min-width: 1024px) {
  .b-sidebar {
    .sidebar-content {
      &.is-mini {
        &:not(.is-mini-expand),
        &.is-mini-expand:not(:hover) {
          .menu-list {
            li {
              a {
                span:nth-child(2) {
                  display: none;
                }
              }
              ul {
                padding-left: 0;
                li {
                  a {
                    display: inline-block;
                  }
                }
              }
            }
          }
          .menu-label:not(:last-child) {
            margin-bottom: 0;
          }
        }
      }
    }
  }
}
</style>
