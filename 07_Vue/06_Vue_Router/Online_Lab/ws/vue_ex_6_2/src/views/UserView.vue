<template>
  <div>
    <h1>User Profile</h1>
    <!-- <p>Username : {{ $route.params.username }}</p> -->
    <p>Username : {{ username }}</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute()

const username = route.params.username

</script>

<style scoped>

</style>