<template>
  <div>
      <div class="poster">
        <img :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" alt="Movie Poster" >
      </div>
      <div class="description">
        <p><strong>{{ movie.title }}</strong></p>
        <p>{{ movie.overview }}</p>
      </div>
  </div>
</template>

<script setup>
defineProps({
  movie:Object
})
</script>

<style scoped>
.poster{
  text-align: center;
}
.description{
  margin-top: 10px;
}

</style>