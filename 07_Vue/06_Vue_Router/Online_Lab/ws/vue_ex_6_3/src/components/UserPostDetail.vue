<template>
  <div>
    <p>번호 : {{ post.id }}</p>
    <p>제목 : {{ post.title }}</p>
    <p>내용 : {{ post.content }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()

const id = ref(route.params.id)

const posts = ref([
  { id: 1, title: 'Post 1', content: 'Content 1' },
  { id: 2, title: 'Post 2', content: 'Content 2' },
  { id: 3, title: 'Post 3', content: 'Content 3' }
])

const post = ref(posts.value.find(post => post.id === Number(id.value)))

onBeforeRouteUpdate((to) => {
  id.value = to.params.id
  post.value = posts.value.find(post => post.id === Number(id.value))
})
</script>
