import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/admin/schools',
    name: 'AdminSchools',
    component: () => import('../views/admin/SchoolView.vue')
  },
  {
    path: '/admin/classrooms',
    name: 'AdminClassrooms',
    component: () => import('../views/admin/ClassroomView.vue')
  },
  {
    path: '/admin/users',
    name: 'AdminUsers',
    component: () => import('../views/admin/UserView.vue')
  },
  {
    path: '/admin/scores',
    name: 'AdminScores',
    component: () => import('../views/admin/ScoreView.vue')
  },
  {
    path: '/admin/notifications',
    name: 'AdminNotifications',
    component: () => import('../views/admin/NotificationView.vue')
  },
  {
    path: '/users',
    name: 'Users',
    component: () => import('../views/admin/UserView.vue')
  },
  {
    path: '/scores',
    name: 'Scores',
    component: () => import('../views/admin/ScoreView.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
