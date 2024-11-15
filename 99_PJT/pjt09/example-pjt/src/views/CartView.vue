<template>
  <h1>장바구니</h1>
  <div v-if="store.carts.length > 0">
    <div class="product-list">
    <div 
      v-for="product in store.carts"
      :key="product.id"
      class="product-card"
    >
      <img :src="product.image" alt="image" class="product-img">
      <div class="product-details">
        <h3>{{ product.title }}</h3>
        <p>가격 : ${{ product.price }}</p>
        <button @click="goDetail(product.id)">상세 페이지로 이동</button>
        <button @click="deleteToCart(product)">장바구니에서 제거</button>
      </div>
    </div>
  </div>
  </div>
  <div v-else>
    <p>장바구니가 비어 있습니다.</p>
  </div>
</template>

<script setup>
import { useCartStore } from '@/stores/cart'
import { useRouter } from 'vue-router'

const store = useCartStore()
const router = useRouter()

const goDetail = (product) => {
  router.push({name : 'productdetail', params : {'product_id' : product}})
}

const deleteToCart = (product) => {
  store.deleteToCart(product.id)
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