<template>
  <div class="card h-100">
    <RouterLink
      :to="{ name: 'MovieDetailView', params: { moviePk: movie.id } }"
    >
      <img
        :src="getImageUrl(movie.poster_path)"
        class="card-img-top"
        alt="..."
      />
      <div class="card-body">
        <h5 class="card-title">{{ movie.title || movie.name }}</h5>
        <div class="card-title">{{ movie.overview }}</div>
      </div>
    </RouterLink>
  </div>
</template>

<script setup>
const props = defineProps(["movie"]);

const getImageUrl = (path) => {
  return path ? `https://image.tmdb.org/t/p/w500${path}` : "";
};
</script>

<style scoped>
.card a,
.card a:hover {
  color: inherit;
  text-decoration: none;
}
</style>
