<template>
  <div>
    <h1>Todo Project</h1>
    <h2>완료된 Todo 개수 : {{ store.doneTodosCount }}</h2>
    <TodoList />
    <TodoForm />
  </div>
</template>

<script setup>
import TodoForm from '@/components/TodoForm.vue';
import TodoList from '@/components/TodoList.vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()


</script>

<style scoped>

</style>



<!-- <script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
// 1. 중앙 저장소 가져오기
import { useCounterStore } from '@/stores/counter';

// 2. 중앙 저장소를 활용해 인스턴스 생성
const store = useCounterStore()

// 3. 중앙 저장소에 상태를 참조
console.log(store.count)

// 액션 호출
// store.increment()

// [주의] 각 컴포넌트에서는 중앙저장소에 새로운 상태를 생성할 수 없다.
// store.ssafy = 'ssafy'


</script>

<template>
  <header>
    <div>
      <p>getters: {{ store.doubleCount }}</p>
      <button @click="store.increment()">++</button>
    </div>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style> -->
