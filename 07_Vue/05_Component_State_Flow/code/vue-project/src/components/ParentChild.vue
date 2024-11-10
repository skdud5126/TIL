<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps}}</p>
    <ParentGrandChild 
      :my-msg="myMsg"
      @update-name="updateName"
    />

    <!--<button @click="$emit('someEvent')">클릭</button>-->
    <button @click="buttonClick">클릭</button>

    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
// 내려받은 props를 선언

// 1. 배열 선언 방식
// defineProps(['myM/g'])

// 2. 객체 선언 방식
defineProps({
  myMsg : String,
  dynamicProps: String,  
})

// props 데이터를 활용해야하는 경우
// const props = defineProps({myMsg : String})
// console.log(props)
// console.log(props.myMsg)

// emit 이벤트 선언(배열방식, 객체방식)
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

const buttonClick = function () {
  emit('someEvent')
}

const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
  emit('updateName')
}

import ParentGrandChild from '@/components/ParentGrandChild.vue';
</script>

<style scoped>

</style>