<template>
  <div>
    <h1>UserView</h1>
    <RouterLink :to="{name : 'user-profile'}">Profile</RouterLink>
    <RouterLink :to="{name : 'user-posts'}">Posts</RouterLink>
    <h2>{{ $route.params }} 유저 프로필 페이지</h2>
    <h2>{{ $route.params.id }} 유저 프로필 페이지</h2>
    <h2>{{ userId }} 유저 프로필 페이지</h2>

    <button @click="goHome">Home!</button>
    <button @click="routeUpdate">100번 유저 페이지로!</button>
    <hr>
    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'
// import { useRoute } from 'vue-router';
import { RouterLink, RouterView, useRoute, useRouter,onBeforeRouteLeave, onBeforeRouteUpdate} from 'vue-router'


const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()
const goHome = function () {
  router.push({ name : 'home'})
  // router.replace({name:'home'})
}

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})

const routeUpdate = function () {
  router.push({name:'user', params : {id : 100}})
}

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})

</script>

<style scoped>

</style>