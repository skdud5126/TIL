import { createRouter, createWebHistory } from 'vue-router'
import SomeView from '@/views/SomeView.vue'
import OtherView from '@/views/OtherView.vue'
import StudentViews from '@/views/StudentViews.vue'
import StudentsDetailView from '@/views/StudentsDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name : 'some',
      component : SomeView
    },
    {
      path : '/other',
      name : 'other',
      component : OtherView
    },
    {
      path : '/students',
      name : 'students',
      component : StudentViews,
    },
    {
      path : '/students/:name',
      name : 'studentsDetail',
      component : StudentsDetailView,
    }

  ]
})

export default router
