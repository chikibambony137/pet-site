import { createRouter, createWebHistory } from 'vue-router';
import App from '../App.vue';
import Profile from '../components/profile.vue';

const routes = [
    {
      path: '/',
      name: 'Home',
      component: App, // ваш компонент главной страницы
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile, // ваш компонент профиля
    },
  ];
  

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
