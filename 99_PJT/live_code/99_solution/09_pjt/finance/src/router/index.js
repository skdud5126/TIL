import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LaterView from '../views/LaterView.vue'
import SearchView from '../views/SearchView.vue'
import DetailView from '../views/DetailView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/search', component: SearchView },
  { path: '/later', component: LaterView },
  {
		path: "/videos/:videoId",
		name: "detail",
		component: DetailView,
	},
]

// 3. `routes`를 옵션으로 전달해 라우터 인스턴스를 생성.
// 여기에 추가 옵션을 전달할 수 있지만, 지금은 간단하게 나타냄.
const router = createRouter({
  // 4. 사용할 히스토리 모드 정의. 여기서는 간단하게 해시 모드를 사용.
  history: createWebHistory(),
  routes, // `routes: routes`와 같음
})

export default router;