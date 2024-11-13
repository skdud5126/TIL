<template>
  <div>
    <p><strong>{{username}}</strong>이 작성한 게시글</p>
    <ol>
      <UserPostListItem v-for="post in posts" :key="post.id" :post="post"/>
    </ol>
    <!-- <RouterLink :to="{name : 'post-detail', params:{id:id}}"/> -->
     <!-- <UserPostDetail /> -->
     <RouterView />
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { RouterView, useRoute } from 'vue-router';
import UserPostListItem from '@/components/UserPostListItem.vue';
import UserPostDetail from '@/components/UserPostDetail.vue';


const route = useRoute()

const username = ref(route.params.username)



const posts = ref([
  {id:1, title:'Post 1', content : 'Content 1'},
  {id:2, title:'Post 2', content : 'Content 2'},
  {id:3, title:'Post 3', content : 'Content 3'}
])
</script>

<style scoped>

</style>