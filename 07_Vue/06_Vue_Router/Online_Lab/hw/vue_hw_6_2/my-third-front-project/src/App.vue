<template>
  <div>
    <MainPage />
    <RouterLink :to="{name:'some'}">Some</RouterLink> | 
    <RouterLink :to="{name : 'other'}">Other</RouterLink>

    <RouterView />
  </div>
</template>

<script setup>
import MainPage from '@/components/MainPage.vue';
</script>

<style scoped>

</style>