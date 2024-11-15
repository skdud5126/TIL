<template>
  <div>
  <h1>Movie List</h1>
  <div class="movie-list">
      <MovieCard       
      v-for="movie in store.movies" 
      :key="movie.id"
      :movie="movie"  
      class="movie-card"
      />
  </div>
</div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie.js'
import { onMounted } from 'vue'
import MovieCard from '@/components/MovieCard.vue'

const store = useMovieStore()
onMounted(() => {
  store.getMovie()
})

</script>


<style scoped>
div{
  margin: 0 auto;
}
.movie-list{
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: space-between;
}

.movie-card{
  border : 1px solid gray;
  width: calc(20% - 20px);
  box-sizing: border-box;
  padding : 15px;
  /* text-align: center; */
}


</style>