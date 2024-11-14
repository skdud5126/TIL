<!-- components/ChildPage 컴포넌트 작성한다. -->
<template>
  <div class="children">
    <!-- '자식 페이지'문구를 작성한다. -->
    <h4>자식 페이지</h4>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  child:Object
})
</script>

<style scoped>

</style>