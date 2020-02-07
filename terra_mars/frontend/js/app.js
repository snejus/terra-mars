import Vue from 'vue';
import VueRouter from 'vue-router';
import BootstrapVue from 'bootstrap-vue';

import App from './App.vue';
import Games from './games/Games.vue';
import Players from './players/Players.vue';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(VueRouter);
Vue.use(BootstrapVue);

const routes = [
  { path: '/', redirect: '/games' },
  { path: '/games', name: 'Games', component: Games },
  { path: '/players', name: 'Players', component: Players },
];

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes,
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
