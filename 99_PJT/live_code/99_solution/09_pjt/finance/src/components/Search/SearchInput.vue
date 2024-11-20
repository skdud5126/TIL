<script setup>
import { ref } from 'vue';

const userInput = ref("");

const emit = defineEmits(['getVideos'])

const getSearchData = () => {
  emit('getVideos', userInput.value)
}

</script>

<template>
  <div>
    <div class="input-group">
      <input
        type="text"
        class="form-control"
        placeholder="검색어를 입력하세요"
        v-model="userInput"
        v-on:keyup.enter="getSearchData"
      />
      <button class="btn btn-success" type="button" @click="getSearchData">
        찾기
      </button>
    </div>
  </div>
</template>

