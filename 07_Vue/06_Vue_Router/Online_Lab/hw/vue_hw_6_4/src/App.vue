<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
    <div class="wrapper">
      <h1>router 연습하기</h1>
      <!-- <MainPage /> -->
      <nav>
        <!-- <RouterLink to="/"></RouterLink> -->
         <RouterLink :to="{ name : 'some'}">Some</RouterLink> |
         <RouterLink :to="{ name : 'other'}">Other</RouterLink> |
         <RouterLink :to="{ name : 'students'}">Students</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
