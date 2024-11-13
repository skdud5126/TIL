<!-- <template>
  <div>
    <h1>학생 상세 정보 목록입니다.</h1>
    <div 
      v-for="student in students" 
      :key="student.name"
      @click="moveToPage(student.name)"
    >
      <p>
        {{ student.name }} 학생 정보 보기
      </p>
    </div>
  </div>
</template>

<script setup>

import { useRouter } from 'vue-router';

const students = [
  {id : 1, name : '김하나'},
  {id : 2, name : '김두리'},
  {id : 3, name : '김서이'}
]

const router = useRouter()

const moveToPage = function(name)  {
  router.push({name : 'studentsDetail', parmas : {name : name}})
}

</script>

<style scoped>

</style> -->



<template>
  <div>
    <h1>학생 상세 정보 목록 입니다.</h1>
    <div 
      v-for="student in students"
      :key="student.name"
      @click="moveToPage(student.name)"
    >
      <p>{{ student.name }} 학생 정보 보기</p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()

const moveToPage = function(name) {
  router.push({ name: 'studentsDetail', params: { name: name }})
}

const students = [
  {
    pk: 1,
    name: '김하나'
  },
  {
    pk: 2,
    name: '김두리'
  },
  {
    pk: 3,
    name: '김서이'
  },
]

</script>

<style lang="scss" scoped>

</style>
