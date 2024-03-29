<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, watch, onMounted, onBeforeMount, type Ref } from 'vue';
import { useStateStore } from '@/stores/state'
import HelloWorld from './components/HelloWorld.vue'
import Switch from './components/ToggleSwitch.vue'

const state = useStateStore()
const themeSwitcherValue: Ref<boolean> = ref(state.currentTheme == "dark")
watch(themeSwitcherValue, (newValue, oldValue)=>{
  state.setTheme(newValue ? "dark" : "light")
})

onBeforeMount(()=>{
  const preferTheme = localStorage.getItem("preferredColorScheme")
  if (preferTheme) {
    document.documentElement.className = preferTheme;
  }
})
onMounted(()=>{
  // This removes the background overwrite that happens in index.html
  // Keep these two files in sync!
  setTimeout(()=>{
    document.body.style.backgroundColor = ""
    document.body.style.transition = ""
  }, 0)
})
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="Django server" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <a href="/rest/">Rest</a>
        <a href="/admin/">Admin</a>
        <a v-if="!state.user?.auth" href="/accounts/login/">Login</a>
        <template v-else>
          <a href="/accounts/logout/">Profile</a>
          <a @click.stop.prevent="state.logOutUser" href="/#">Logout</a>
        </template>
      </nav>
      <div style="display: flex; justify-content: space-between; width: 100%;">
        <h3 class="heading">Theme Selector: </h3>
        <h3>🌞 <Switch class="themeSwitch" v-model="themeSwitcherValue" /> 🌙</h3>
      </div>
      <span>Notice how it does not flash the screen on refresh on either of the two themes.</span>
    </div>
  </header>
  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.heading {
  color: var(--color-heading);
}

:deep(.themeSwitch.active .ball) {
  background-color: goldenrod;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
  display: flex;
  flex-wrap: wrap;
  justify-content: start;
  gap: 1px;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
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

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }

  nav a {
    width: unset;
    flex-basis: 85px;
  }
}
</style>
