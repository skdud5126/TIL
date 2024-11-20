<script setup>
import axios from "axios";
import dayjs from "dayjs";
import LaterVideoList from "@/components/Later/LaterVideoList.vue";
import ArrowBack from "@/components/Common/ArrowBack.vue";
import LoadingIcon from "@/components/Common/LoadingIcon.vue";
import { ref, onMounted } from 'vue';

const URL = "https://www.googleapis.com/youtube/v3/videos"
const API_KEY = "AIzaSyChh0pNXw1tFzg-jKvohZ6gtwxwOgjg-UE"

const laterVideoList = ref([]);
const isLaterVideo = ref(false);
const isLoading = ref(false)

const setLaterVideoList = (videoIds) => {
  videoIds.forEach((videoId) => {
    axios
    .get(URL, {
      params: {
        key: API_KEY,
        part: "snippet",
        id: videoId,
      },
    }).then((response) => {
      const data = response.data.items[0];
      laterVideoList.value.push({
        videoId: data.id,
        title: data.snippet.title,
        description: data.snippet.description,
        publishTime: dayjs(data.snippet.publishedAt).format("YYYY-MM-DD"),
        thumbnails: data.snippet.thumbnails,
        channelId: data.snippet.channelId,
      });
    }).catch((error) => {
      console.log(error);
    });
  });
}

onMounted(() => {
  isLoading.value = true
  const listString = localStorage.getItem("laterVideoList");
  if (listString === null) {
    isLaterVideo.value = false
  }
  const laterVideoList = JSON.parse(listString);

  if(laterVideoList && laterVideoList.arr.length > 0) {
    setLaterVideoList(laterVideoList.arr);
    isLaterVideo.value = true;
  }
    isLoading.value = false
})
</script>

<template>
  <div class="later-view">
    <ArrowBack />
    <h1>나중에 볼 동영상</h1>
    <LoadingIcon v-if="isLoading" />
    <div v-else>
      <div v-if="isLaterVideo">
        <LaterVideoList v-bind:laterVideoList="laterVideoList" />
      </div>
      <div v-else>등록된 비디오 없음</div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  margin-top: 20px;
  margin-bottom: 20px;
  font-weight: bold;
}
.loading-icon-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 80vh;
}
</style>