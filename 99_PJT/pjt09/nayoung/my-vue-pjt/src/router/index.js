import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import MovieListView from '@/views/MovieListView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name : 'home',
      component : HomeView
    },
    {
      path : '/movies',
      name : 'movie-list',
      component : MovieListView
    },
    {
      path : '/:movieId',
      name : 'movie-detail',
      component : MovieDetailView
    }
  ],
}, {persist : true})

export default router
