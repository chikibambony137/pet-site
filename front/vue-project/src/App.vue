<template>
  <div class="home-page">
  <header class="navbar">
    <div class="menu-icon" @click="toggleMenu">
      <span class="line" v-bind:class="{ open: isOpen }"></span>
      <span class="line" v-bind:class="{ open: isOpen }"></span>
      <span class="line" v-bind:class="{ open: isOpen }"></span>
    </div>

    <div class="logo-container" @click="reloadPage">
      <router-link to="/home">
      <img class="logo" src="/logo.png" alt="Логотип" />
      </router-link>
      <h1 class="company-name">BryakBlog</h1>
      
    </div>

    <div class="avatar-container" @click="openProfile">
      <router-link to="/profile">
      <img class="avatar" src="/ava.jpg" alt="Аватар" />
      </router-link>
    </div>

    <div v-if="isProfileContainerVisible" class="profile-container">
      <router-view></router-view>
      <button class="close-button" @click="closeProfileContainer">✕</button>
    </div>

    <div :class="['dropdown', { 'slide-in': isOpen, 'slide-out': !isOpen }]">

      <ul class="menu-list">
        <li><button class="menu-button" @click="toggleAbout">Обо мне</button></li>
        <li><button class="menu-button" @click="toggleProjects">Проекты</button></li>
        <li><button class="menu-button" @click="toggleIdeas">Идеи</button></li>
        <li><button class="menu-button" @click="toggleContacts">Контакты</button></li>
        <li><button class="menu-button" @click="togglePhoto" >Фотографии</button></li>
        <li><button class="menu-button" @click="toggleMemes" >Приколюхи</button></li>
      </ul>

    </div>

    <div v-if="isContainerVisible" class="info-container" :style="{ width: infoWidth }">

        <AboutMe v-if="showAbout" @close="showAbout = false" />
        <Projects v-if="showProjects" @close="showProjects = false" />
        <Ideas v-if="showIdeas" @close="showIdeas = false" />
        <Contacts v-if="showContacts" @close="showContacts = false" />
        <Photo v-if="showPhoto" @close="showPhoto = false" />
        <Memes v-if="showMemes" @close="showMemes = false" />

        <button class="close-button" @click="closeInfoContainer">✕</button>

    </div>

    <div class="home-label">
      <label>
        Добро пожаловать!
      </label>
    </div>

  </header>
  </div>
</template>

<script>
import AboutMe from './components/aboutme.vue'; // Импортируем компонент "Обо мне"
import Projects from './components/projects.vue';
import Ideas from './components/ideas.vue';
import Contacts from './components/contacts.vue';
import Photo from './components/photo.vue';
import Memes from './components/memes.vue';


export default {
  components: {
    AboutMe, Projects, Ideas, Contacts, Photo, Memes
  },
  
  data() {
    return {
      isOpen: false,
      showAbout: false,
      showProjects: false,
      showIdeas: false,
      showContacts: false,
      showPhoto: false,
      showMemes: false,
      infoWidth: '75%',

      isContainerVisible: false,
      isProfileContainerVisible: false,
    };
  },
  
  methods: {
    toggleMenu() {
      this.isOpen = !this.isOpen;
      this.infoWidth = this.isOpen ? '75%' : '95%'; // Изменяем ширину в зависимости от состояния меню
    },
    
    toggleAbout() {
      this.showContacts = false;
      this.showIdeas= false;
      this.showProjects = false;
      this.showPhoto = false;
      this.showMemes = false;

      this.isContainerVisible = true;
      this.showAbout = true;

      setTimeout(this.toggleMenu, 100)
    },

    toggleProjects() {
      this.showContacts = false;
      this.showIdeas= false;
      this.showAbout = false;
      this.showPhoto = false;
      this.showMemes = false;

      this.isContainerVisible = true;
      this.showProjects = true;

      setTimeout(this.toggleMenu, 100)
    },

    toggleIdeas() {
      this.showContacts = false;
      this.showAbout = false;
      this.showProjects = false;
      this.showPhoto = false;
      this.showMemes = false;

      this.isContainerVisible = true;
      this.showIdeas= true;

      setTimeout(this.toggleMenu, 100)
    },

    toggleContacts() {
      this.showAbout = false;
      this.showProjects = false;
      this.showIdeas= false;
      this.showPhoto = false;
      this.showMemes = false;

      this.isContainerVisible = true;
      this.showContacts = true;

      setTimeout(this.toggleMenu, 100)
    },

    togglePhoto() {
      this.showAbout = false;
      this.showProjects = false;
      this.showIdeas= false;
      this.showMemes = false;
      this.showContacts = false;

      this.isContainerVisible = true;
      this.showPhoto = true;

      setTimeout(this.toggleMenu, 100)
    },

    toggleMemes() {
      this.showAbout = false;
      this.showProjects = false;
      this.showIdeas= false;
      this.showContacts = false;
      this.showPhoto = false;

      this.isContainerVisible = true;
      this.showMemes = true;

      setTimeout(this.toggleMenu, 100)
    },

    closeInfoContainer() {
      this.isContainerVisible = false;
    },

    closeProfileContainer() {
      this.isProfileContainerVisible = false;
    },

    reloadPage() {
      // this.forceUpdate();
      location.reload();
    },

    openProfile() {
      this.isProfileContainerVisible = !this.isProfileContainerVisible;
    }
  }
};
</script>
