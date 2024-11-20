<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
    video: {
      description: String,
      publishTime: String,
      thumbnails: {
        default: {
          height: Number,
          width: Number,
          url: String,
        },
        high: Object,
        medium: Object,
      },
      title: String,
      videoId: String,
    },
  })

const video = ref(props.video)

const thumbnailSrc = computed(() => {
  return video.value.thumbnails.medium.url;
})

const title = computed(() => {
  return video.value.title;
})

const router = useRouter()

const moveToDetail = () => {
  router.push(`/videos/${video.value.videoId}`);
}

</script>

<template>
  <div>
    <div
      class="video-card card text-bg-light border-secondary"
      v-on:click="moveToDetail"
    >
      <img
        class="card-img-top"
        v-bind:src="thumbnailSrc"
        v-on:click="moveToDetail"
        alt="video"
      />
      <div class="card-body">
        <p class="card-text">{{ title }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.video-card {
  width: 300px;
  height: 300px;
}
.card-text {
  font-size: 1.2rem;
  font-weight: bolder;
}
</style>