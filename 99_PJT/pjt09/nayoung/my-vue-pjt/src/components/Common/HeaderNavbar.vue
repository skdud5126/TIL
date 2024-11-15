
<template>
  <nav class="navbar bg-body-tertiary">
    <div class="navbar-content">
      <RouterLink :to="{name : 'home'}" class="navbar-brand">
        <img src="@/assets/ssafy-logo.png" alt="Bootstrap" width="40p" height="30">
      </RouterLink>
      <RouterLink :to="{name : 'movie-list'}" class="movie-link">영화 조회</RouterLink>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
nav {
  background-color: gray;
  padding: 0 20px;
}

.navbar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%; /* 전체 너비 사용 */
}

nav a {
  color: black;
  font-weight: bold;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: green;
}
</style>