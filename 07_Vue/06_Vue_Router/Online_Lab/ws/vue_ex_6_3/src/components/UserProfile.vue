<template>
  <div>
    <h3>상세 프로필</h3>
    <p>반갑습니다. {{ username }}입니다.</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import {ref} from 'vue'

const route = useRoute()

const username = ref(route.params.username)
</script>

<style scoped>

</style>