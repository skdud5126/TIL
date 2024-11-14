<!-- ProductList 컴포넌트
      - App 컴포넌트의 하위 컴포넌트이다.
      - src/components 폴더 내에 위치한다.
      - userProductStore에 있는 'products' state를 출력한다. -->
<template>
  <div>
    <h1>Product List</h1>
    <ul 
      v-for="product in store.products"
      :key="product.id"
    >
      <li>{{ product.id }} - {{ product.title }} - {{ product.body }}</li>
    </ul>

  </div>
</template>

<script setup>
import  {useProductStore} from '@/stores/product.js'

const store = useProductStore()


</script>

<style scoped>

</style>