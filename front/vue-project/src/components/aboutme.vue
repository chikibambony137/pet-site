<script>
import axios from 'axios';

export default {
  data() {
    return {
      aboutMe: ''  // Переменная для хранения информации
    };
  },
  mounted() {
    this.fetchAboutMe();  // Вызов функции для получения данных
  },
  methods: {
    async fetchAboutMe() {  // Добавляем async
      try {
        const response = await axios.get('http://127.0.0.1:8000/aboutme');  // Добавляем await
        this.aboutMe = response.data.text;  // Сохраняем полученные данные
      } catch (error) {
        alert('Ошибка при получении данных: ' + error);  // Исправляем вывод ошибки
      }
    }
  }
}
</script>

<template>
  <div class="about-me">
    <h2>Обо мне</h2>
    <p>{{ aboutMe }}</p>  <!-- Выводим информацию -->
  </div>
</template>