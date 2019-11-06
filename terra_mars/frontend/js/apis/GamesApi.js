import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

export default class GamesApi {
  static getPlayerSummaries() {
    const url = '/api/playersummary/';
    return axios
      .get(url)
      .then((response) => response.data)
      .catch((e) => {
        console.log(e);
      });
  }

  static getStats() {
    const url = '/api/player_game_stats/';
    return axios
      .get(url)
      .then((response) => response.data)
      .catch((e) => {
        console.log(e);
      });
  }
}
