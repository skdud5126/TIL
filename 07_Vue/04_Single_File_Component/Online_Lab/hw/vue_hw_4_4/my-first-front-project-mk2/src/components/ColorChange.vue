<!-- 1. 사용하지 않을 컴포넌트와 assets들을 모두 삭제한다. -->
  <!-- a. components/ 폴더의 모든 컴포넌트 -->
   <!-- b. assets/ 폴더의 모든 파일 -->
<!-- 2. 관련된 모든 코드를 삭제한다. 
        c. App.vue에 작성된 삭제된 component들
        d. main.js에 작성된 main.css import 문
     3. ColorChange.vue 컴포넌트를 생성한다.-->

<template>
  <div>
    <!-- e. 사용자가 값을 입력할 수 있도록 input 태그를 작성한다. -->
     <!-- h. 사용자가 입력한 값이 colorClass 변수에 할당 될 수 있도록 양방향 바인딩 directive를 사용한다. -->
    <input type="text" v-model="colorClass">
    <!-- f. '입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.' 문구를 포함한 p태글르 작성한다. -->
     <!-- i. colorClass변수의 값이 첫 번쨰 p태그의 class가 도리 수 있도록 단방향 바인딩 directive를 사용한다. -->
    <p :class="colorClass">입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>
  </div>
</template>

<script setup>
import  {ref} from  'vue'
const colorClass = ref('')
</script>

<style scoped>
/* g. 각각 글씨 색이 red, blue, green이 되도록 설정된 클래스 .red, .blue, .green을 style에 작성한다. */
.red{
  color : red;
}
.blue{
  color: blue;
}
.green{
  color:green;
}
</style>