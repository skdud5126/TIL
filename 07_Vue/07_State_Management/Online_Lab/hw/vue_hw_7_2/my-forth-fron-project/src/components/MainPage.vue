<!-- components/MainPage 컴포넌트를 작성한다. -->
<template>
  <div>
    <!-- 'pinia 연습하기' 문구를 포함한다. -->
    <h1>pinia 연습하기</h1>
    <ParentPage 
      v-for="family in familyInfo"
      :key="family.familyName"
      :family="family"
    />
  </div>
</template>

<script setup>
// MainPage 컴포넌트에 하위 컴포넌트로 등록한다.
import ParentPage from  '@/components/ParentPage.vue'

// MainPage 컴포넌트에서 store에 저장된 familyInfo 정보를 불러온다.
import { useFamilyStore } from '@/stores/family.js'

const store = useFamilyStore()

const familyInfo = store.familyInfo


</script>

<style scoped>

</style>