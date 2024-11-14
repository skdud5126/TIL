<template>
    <div>
      <p>이름 : {{ balance.name }}</p>
      <p>잔고 : {{ balance.balance }}</p>
      <button @click="updateBtn(balance.name)">updateBalance</button>
      <hr>
    </div>
</template>

<script setup>
import {useRouter} from 'vue-router'

defineProps({
  balance : Object
})

const router = useRouter()

const updateBtn = function (name) {
  router.push({name : 'update', params : {'name': name}})
}
</script>

<style scoped>

</style>