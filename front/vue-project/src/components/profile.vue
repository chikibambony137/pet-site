<template>
    <div class="profile-page">
      <header>
        <h1>Профиль пользователя</h1>
      </header>
  
      <div class="profile-details">
        <img :src="avatar" alt="Аватар пользователя" class="avatar" />
        <div class="user-info">
          <h2>{{ userName }}</h2>
          <p><strong>Email:</strong> {{ email }}</p>
          <p><strong>Номер телефона:</strong> {{ phone }}</p>
          <h3>О себе:</h3>
          <p>{{ aboutMe }}</p>
        </div>
      </div>
  
      <footer>
        <button @click="editProfile">Редактировать профиль</button>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        avatar: '/ava.jpg', // Путь к изображению аватара
        userName: 'Имя пользователя',
        email: 'user@example.com',
        phone: '+7 (123) 456-78-90',
        aboutMe: 'Здесь небольшое описание о пользователе.',
      };
    },
    methods: {
      editProfile() {
        // Эта функция может быть реализована для перехода на страницу редактирования профиля
        alert('Функция редактирования профиля будет добавлена позже.');
      }
    }
  };
  </script>
