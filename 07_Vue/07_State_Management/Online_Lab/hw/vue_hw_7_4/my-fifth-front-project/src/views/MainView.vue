<template>
  <div>
    <h1>메인 페이지</h1>
    <MainPage
      v-for="balance in store.balances"
      :key="balance.name"
      :balance="balance"
    />
  </div>
</template>

<script setup>
import MainPage from '@/components/Mainpage.vue'
import { useBalanceStore } from '@/stores/balance.js'

const store = useBalanceStore()

</script>

<style scoped>

</style>