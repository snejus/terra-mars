<style>
</style>

<template>
  <div>
    <b-card-group deck columns>
    <div v-for="player in players" :key="player.id">
      <b-card
        border-variant="success"
        :header="player.name"
        class="text-center">
        <b-card-text>Hello</b-card-text>
      </b-card>
    </div>
    </b-card-group>
  </div>
</template>
<script>
import GamesApi from '../apis/GamesApi';

export default {
  name: 'Players',
  components: {
  },
  data() {
    return {
      players: null,
    };
  },
  computed: {
  },
  created() {
    GamesApi.getPlayers().then((data) => {
      this.players = data;
    });
  },
  methods: {
  },
};
</script>
