<template>
  <div class="container">
    <div class="search-container">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="영화 제목을 검색해보세요"
        class="search-input"
        v-on:keyup.enter="searchReviews"
      />
      <button @click="searchReviews" class="search-button">검색</button>
    </div>
    <div>
      <div v-for="(video, index) in videos" :key="index">
        <YoutubeCard
          :thumbnail="video.snippet.thumbnails.default.url"
          :title="video.snippet.title"
          :descriptions="video.snippet.description"
          @click="openModal(index)"
          data-bs-toggle="modal"
          data-bs-target="#youtubeTrailerModal"
        />
      </div>
    </div>
    <YoutubeReviewModal
      :videoTitle="videoTitle"
      :currentVideoId="currentVideoId"
    />
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import YoutubeReviewModal from "@/components/YoutubeReviewModal.vue";
import YoutubeCard from "@/components/YoutubeCard.vue";

const searchQuery = ref("");
const videos = ref([]);
const currentVideoId = ref("");
const youtubeKey = import.meta.env.VITE_YOUTUBE_API_KEY;
const videoTitle = ref("");

const searchReviews = () => {
  axios
    .get("https://www.googleapis.com/youtube/v3/search", {
      params: {
        part: "snippet",
        q: `영화 ${searchQuery.value} 리뷰`,
        key: youtubeKey,
        type: "video",
        maxResults: 10,
      },
    })
    .then((response) => {
      videos.value = response.data.items;
    })
    .catch((error) => {
      console.error("API 호출 중 에러 발생:", error);
    });
};

const openModal = (index) => {
  const VideoId = videos.value[index].id.videoId;
  currentVideoId.value = VideoId;
  videoTitle.value = videos.value[index].snippet.title;
};
</script>

<style>
.search-container {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
  margin-top: 2rem;
}

.search-input {
  width: 60%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.search-button {
  margin-left: 10px;
  padding: 10px 20px;
  font-size: 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #0056b3;
}
</style>
