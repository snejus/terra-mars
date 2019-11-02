<template>
  <b-navbar type="light" variant="light">
    <b-navbar-nav>
      <b-nav-item v-for="link in links" :key="link.id" :to="link.page">{{ link.text }}</b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navigation',
  data() {
    return {
      links: [
        {
          id: 0,
          text: 'Games',
          page: '/games',
        },
      ],
    };
  },
  created() {
  },
};
</script>
