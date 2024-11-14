import { defineStore } from "pinia";
import { ref } from 'vue'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
      {
        name : '김하나',
        balance : 100000
      },
      {
        name : '김두리',
        balance : 10000
      },
      {
        name : '김서이',
        balance : 100
      }
    ])

    const detailInfo = function (name) {
      return balances.value.find((balance) => balance.name === name)
    }

    const updateInfo = function(name) {
      balances.value = balances.value.map((info) => {
        if (info.name === name) {
          info.balance+=1000
        }
        return info
      })
    }
  return {balances, detailInfo, updateInfo}
})