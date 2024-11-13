
<template>
  <header>
    <nav>
      <RouterLink :to="{name : 'home'}">Home</RouterLink> |
      <RouterLink :to="{name : 'about'}">About</RouterLink> |
      <RouterLink :to="{name :'user'}">User</RouterLink>
    </nav>
    <RouterView />
  </header>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
</style>
