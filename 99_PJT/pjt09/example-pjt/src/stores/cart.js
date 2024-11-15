import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCartStore = defineStore('cart', () => {
  // 여러 개의 컴포넌트에서 활용하는 데이터만
  // store로 관리해야 한다.
  // -> 여러 명이 작업할 때 체감이 될 것!

  let products = ref([])
  let carts = ref([])

  // 데이터 다운로드
  const getProducts = () => {
    // axios는 Promise 객체와 동일하게 활용한다.
    axios.get('https://fakestoreapi.com/products')
    .then((response) => {
      console.log("response =", response)
      products.value = response.data
    }).catch((error) => {
      console.log("error = ", error)
    })
  }

  // 상세 페이지 상품 조회
  const getProductById = (id) => {
    const product = products.value.find((prod) => prod.id == id)
    // console.log("product = ", product)
    return product
  }

  // 1. 장바구니에 추가하기
  const addToCart = (product) => {
    // 장바구니에 포함되지 않았다면 추가
    const index = carts.value.findIndex((element) => element.id === product.id )
    if (index === -1) {
      alert('장바구니 페이지로 이동합니다.')
      carts.value.push(product)
    } else {
      alert('이미 추가된 상품입니다.')
    }
  }
  // 2. 장바구니에서 삭제하기
  const deleteToCart = (productId) => {
    // 1. id를 통해서 해당 상품의 index를 찾는다.
    // 2. 해당 index를 기준으로 하나를 제거한다. (splice)
    const index = carts.value.findIndex((element) => element.id === productId)
    if (index !== -1){
      // 있는 상품이라면 splice를 통해 인덱스로부터 1개를 제거
      carts.value.splice(index, 1)
    }
  }
  // 3. 장바구니에 특정 상품이 포함되어 있는가?

  return { products, carts, getProducts, getProductById, addToCart, deleteToCart }
}, {persist : true})
