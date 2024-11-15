<template>
  <h1>상품 목록 리스트</h1>
  <div class="product-list">
    <div 
      v-for="product in store.products"
      :key="product.id"
      class="product-card"
    >
      <img :src="product.image" alt="image" class="product-img">
      <div class="product-details">
        <h3>{{ product.title }}</h3>
        <p>가격 : ${{ product.price }}</p>
        <button @click="goDetail(product.id)">상세 페이지로 이동</button>
        <button @click="addToCart(product)">장바구니로 이동</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCartStore } from '@/stores/cart.js'
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'

const store = useCartStore()
const router = useRouter()

// API로 데이터를 다운로드 받아야한다.
// setup에서 호출하는게 맞을까?
// 무슨 문제점이 발생할 수 있을까?
// -> DOM 입장에서 없는 데이터로 화면을 그리려고 시도 할 수 있다.
// setup: DOM이 그려지기 전에 호출
// 데이터 다운로드는 DOM이 그려지고 난 후에 가져오는 걸 권장
onMounted(() => {
  store.getProducts()
})

const goDetail = (product) => {
  router.push({name : 'productdetail', params : {'product_id' : product}})
}

const addToCart = (product) => {
  store.addToCart(product)
  router.push({name : 'cart'})
}

</script>

<style scoped>
.product-list{
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.product-card{
  border : 1px solid #000;
  width: 200px;
  padding : 15px;
}

.product-img{
  width: 100%;

}

.product-details{
  text-align: center;
}
</style>