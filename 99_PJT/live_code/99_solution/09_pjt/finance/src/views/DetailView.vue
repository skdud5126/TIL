<script setup>
import axios from "axios";
import dayjs from "dayjs";
import { useRoute } from 'vue-router'
import ArrowBack from "@/components/Common/ArrowBack.vue";
import LoadingIcon from "@/components/Common/LoadingIcon.vue";
import { ref } from 'vue';

const route = useRoute();

const detailURL = "https://www.googleapis.com/youtube/v3/videos"
const API_KEY = "AIzaSyChh0pNXw1tFzg-jKvohZ6gtwxwOgjg-UE"

const isLoading = ref(false);
const video = ref("");
const isLaterVideo = ref("");
const videoSrc = ref("");

const checkVideoInStorage = () => {
  const listString = localStorage.getItem("laterVideoList");
  if (listString === null) {
    return false;
  }
  const laterVideoList = JSON.parse(listString);
  if (laterVideoList.arr.includes(video.value.videoId)) {
    return true;
  } else {
    return false;
  }
}

const registerLaterVideo = () => {
  const listString = localStorage.getItem("laterVideoList");
  if (listString === null) {
    localStorage.setItem(
      "laterVideoList",
      `{"arr": ["${video.value.videoId}"]}`
      );
    } else {
      const laterVideoList = JSON.parse(listString);
      laterVideoList.arr.push(video.value.videoId);
      localStorage.setItem("laterVideoList", JSON.stringify(laterVideoList));
    }
    isLaterVideo.value = true;
}

const unregisterLaterVideo = () => {
  const listString = localStorage.getItem("laterVideoList");
  const laterVideoList = JSON.parse(listString);
  const idx = laterVideoList.arr.indexOf(video.videoId);
  laterVideoList.arr.splice(idx, 1);
  localStorage.setItem("laterVideoList", JSON.stringify(laterVideoList));
  isLaterVideo.value = false;
}

axios.get(detailURL, {
  params: {
    key: API_KEY,
    part: "snippet",
    id: route.params.videoId,
  },
}).then((response) => {
  const item = response.data.items[0];
  video.value = {
    videoId: item.id,
    title: item.snippet.title,
    description: item.snippet.description,
    publishedAt: dayjs(item.snippet.publishedAt).format("YYYY-MM-DD"),
  };
  videoSrc.value = `https://www.youtube.com/embed/${video.value.videoId}?autoplay=1`;
  isLaterVideo.value = checkVideoInStorage();
  isLoading.value = false
}).catch((error) => {
  console.log(error);
});

</script>

<template>
  <div class="detail-view">
    <LoadingIcon v-if="isLoading" />
    <div v-else>
      <ArrowBack />
      <h1>{{ video.title }}</h1>
      <div class="upload-date">업로드 날짜: {{ video.publishedAt }}</div>
      <iframe
        width="560"
        height="315"
        :src="videoSrc"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
      ></iframe>
      <p class="description">{{ video.description }}</p>
      <button
        v-if="isLaterVideo"
        type="button"
        class="btn btn-danger"
        v-on:click="unregisterLaterVideo"
      >
        저장 취소
      </button>
      <button
        v-else
        type="button"
        class="btn btn-primary"
        v-on:click="registerLaterVideo"
      >
        동영상 저장
      </button>
    </div>
  </div>
</template>

<style scoped>
.loading-icon-container {
  height: 80vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
}
h1 {
  margin-top: 20px;
  margin-bottom: 20px;
  font-weight: bold;
}
.upload-date {
  margin-bottom: 20px;
}
.description {
  margin-top: 20px;
}
</style>