<style>
</style>

<template>
  <div>
    <b-card-group deck columns>
    <div v-for="player in players" :key="player.name">
      <b-card
        border-variant="success"
        :header="player.name"
        class="text-center">
        <b-card-text>
          Games played: {{ player.games_played }}
          <br>
          Favourite corporation: {{ getFavouriteCorporation(player) }} ()

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
    GamesApi.getStats().then((data) => {
      this.players = this.parseStats(data);
    });
  },
  methods: {
    parseStats(stats) {
      const players = {};
      // console.log(stats);
      for (let index = 0; index < stats.length; index++) {
        const playerName = stats[index].player.name;
        if (!(playerName in players)) {
          players[playerName] = { name: playerName, games_played: 1, corporations: {} };
        } else {
          players[playerName].games_played++;
        }

        // TODO: Add wins count
        // TODO: For some reason corporation names that include spaces are not handled correctly

        const corporationName = stats[index].corporation.name;
        if (!(corporationName in players[playerName].corporations)) {
          players[playerName].corporations[corporationName] = 1;
        } else {
          players[playerName].corporations[corporationName]++;
        }
      }
      return players;
    },
    getFavouriteCorporation(player) {
      console.log(player.corporations);
      const favouriteCorporations = this.getMax(player.corporations);
      console.log(favouriteCorporations);
      return favouriteCorporations.join(' and ');
    },

    getMax(object) {
      return Object.keys(object).filter((x) => object[x] == Math.max.apply(null,
        Object.values(object)));
    },
  },
};
</script>
