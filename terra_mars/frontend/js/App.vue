<style>
/* @import "../assets/bootstrap.min.css"; */
.padding {
  height: 70px;
  width: 100%;
}
</style>

<template>
  <div id="app">
    <Navigation class="fixed-top" />
    <div class="padding" />
    <router-view />
  </div>
</template>

<script>
import Navigation from './Navigation.vue';

export default {
  name: 'App',
  components: {
    Navigation,
  },
};
</script>
