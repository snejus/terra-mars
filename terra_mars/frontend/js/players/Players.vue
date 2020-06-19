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
        <b-card-text>
          Games played: {{ player.games_played }}
          <br>
          Games won: {{ player.games_won}}
          <br>
          Favourite corporation: {{ player.favourite_corporation.name }}
          ({{ player.favourite_corporation.times_played }})
        </b-card-text>
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
    GamesApi.getPlayerSummaries().then((data) => {
      this.players = this.sortByGamesPlayed(data);
    });
  },
  methods: {
    sortByGamesPlayed(data) {
      return data.sort((a, b) => b.games_played - a.games_played);
    },
  },
};
</script>
