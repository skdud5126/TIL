<template>
  <div class="youtube-card" @click="handleClick">
    <img :src="thumbnail" alt="YouTube Video Thumbnail" />
    <div class="content-wrapper">
      <h3 v-html="title"></h3>
      <div class="youtube-description"># {{ descriptions }}</div>
    </div>
  </div>
</template>

<script setup>
import {} from 'vue'

const props = defineProps(['thumbnail', 'title', 'descriptions'])

const emit = defineEmits()

const handleClick = () => {
  emit('click')
}
</script>

<style>
.youtube-card {
  display: flex;
  flex-direction: row;
  align-items: start;
  border: 1px solid #ccc;
  padding: 10px;
  cursor: pointer;
  margin-bottom: 1rem;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.youtube-card img {
  width: 200px;
  height: auto;
  border-radius: 4px;
}
.content-wrapper {
  margin-left: 1rem;
  flex-grow: 1;
}
.youtube-card h3 {
  margin-top: 0;
  font-size: 1.5em;
}
.youtube-description {
  font-size: 0.9em;
  margin-top: 0.5rem;
  color: #555;
}
</style>
