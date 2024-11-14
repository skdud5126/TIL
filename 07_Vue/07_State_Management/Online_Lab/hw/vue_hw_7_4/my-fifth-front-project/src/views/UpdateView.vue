<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름 : {{ detailInfo.name }}</p>
    <p>잔고 : {{ detailInfo.balance }}</p>
    <button @click="store.updateInfo(route.params.name)">+</button>
  </div>
</template>

<script setup>
import {useRoute} from 'vue-router'
import {useBalanceStore} from '@/stores/balance.js'

const store = useBalanceStore()
const route = useRoute()


const detailInfo = store.detailInfo(route.params.name)



</script>

<style scoped>

</style>