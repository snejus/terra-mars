import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

export default class GamesApi {
  static getPlayers() {
    const url = '/api/player/';
    return axios
      .get(url)
      .then((response) => response.data)
      .catch((e) => {
        console.log(e);
      });
  }
}
