<!-- components/ParentPage 컴포넌트를 작성한다. -->
<template>
  <div class="parent">
    <!-- '부모 컴포넌트'문구를 작성한다. -->
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage 
      v-for="child in family.children"
      :key="child.name"
      :child="child"
    />
  </div>
</template>

<script setup>
// ChildePate 컴포넌트 ParentPage 컴포넌트에 하위 컴포넌트로 등록한다.
import ChildPage from '@/components/ChildPage.vue'

defineProps({
  family:Object
})
</script>

<style scoped>
div{
  border: 1px gray solid;
  text-align:  center;
  background-color: gainsboro;
  padding : 20px;
  margin : 20px;
}

.children{
  background-color: antiquewhite;
}
</style>