import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const API_KEY = import.meta.env.VITE_TMDB_API_KEY

  // console.log(API_KEY)
  let movies = ref([])

  const getMovie = function () {
    axios({
      url: 'https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=1',
      method : 'GET', 
      headers : {
        accept: 'application/json',
        Authorization : `Bearer ${API_KEY}`
      }
    })
    .then((response) => {
      console.log(response.data)
      movies.value = response.data.results
      console.log(movies.value)
    }).catch((error) => {
      console.log(error)
    })
  }
  

  return { movies, getMovie }
})
