import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import UserView from '@/views/UserView.vue'
import {ref} from 'vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path : '/user/:username',
      name : 'user',
      component : UserView,
      // 4. 다른 주소에서 UserView 컴포넌트 주소로 진입할 때 admin이 아니면 진입을 금지한다.
      beforeEnter : (to,from) => {
        // - 동적 파라미터 username이 admin이 아니라면 경고 대화상자를 출력한다.
        const requestusername = to.params.username
        if ( requestusername !== 'admin') {
          window.alert('접근할 수 없습니다.')
          return {name : 'home'}
        }
      }
    }
  ]
})




export default router
