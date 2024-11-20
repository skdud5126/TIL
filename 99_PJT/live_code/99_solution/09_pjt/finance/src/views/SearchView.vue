<script setup>
import dayjs from 'dayjs'
import { ref, onMounted } from "vue";
import axios from 'axios'
import SearchInput from "@/components/Search/SearchInput.vue";
import SearchVideoList from "@/components/Search/SearchVideoList.vue";
import ArrowBack from "@/components/Common/ArrowBack.vue";
import LoadingIcon from "@/components/Common/LoadingIcon.vue";

const URL = "https://www.googleapis.com/youtube/v3"
const API_KEY = "AIzaSyChh0pNXw1tFzg-jKvohZ6gtwxwOgjg-UE"
const isLoading = ref(false);
const videoList = ref([])
const word = ref('')

const getVideos = (userInput) => {
  word.value = userInput
  isLoading.value = true
  axios
      .get(`${URL}/search`, {
        params: {
          key: API_KEY,
          part: "snippet",
          type: "video",
          q: word.value,
          maxResults: 10,
        },
      })
      .then((response) => {
        const parsedVideoList = response.data.items.map((item) => {
          return {
            videoId: item.id.videoId,
            title: item.snippet.title,
            description: item.snippet.description,
            publishTime: dayjs(item.snippet.publishTime).format("YYYY-MM-DD"),
            thumbnails: item.snippet.thumbnails,
          };
        });
        
        videoList.value = parsedVideoList;
        isLoading.value = false
      })
      .catch((error) => {
        console.log(error);
      });
}


</script>

<template>
  <div class="search-view">
    <ArrowBack />
    <h1>비디오 검색</h1>
    <SearchInput class="search-input" @get-videos="getVideos" />
    <div v-if="isLoading">
      <LoadingIcon />
    </div>
    <div v-else>
      <SearchVideoList :video-list="videoList"/>
    </div>
  </div>
</template>

<style scoped>
.loading-icon-container {
  height: 80vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.search-input {
  margin-bottom: 20px;
}
</style>