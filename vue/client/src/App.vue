<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, watch, onMounted, onBeforeMount, type Ref } from 'vue';
import { useStateStore } from '@/stores/state'
import HelloWorld from './components/HelloWorld.vue'
import Switch from './components/ToggleSwitch.vue'

const store = useStateStore()
const themeSwitcherValue: Ref<boolean> = ref(store.currentTheme == "dark")
watch(themeSwitcherValue, (newValue, oldValue)=>{
  store.setTheme(newValue ? "dark" : "light")
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

const cookies = ref(false)
setTimeout(()=>{
  cookies.value = true
}, 1500)
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
      </nav>
      <div style="display: flex; justify-content: space-between; width: 100%;">
        <h3>Theme Selector: </h3>
        <h3>🌞 <Switch class="themeSwitch" v-model="themeSwitcherValue" /> 🌙</h3>
      </div>
      <span>Notice how it does not flash the screen on refresh on either of the two themes.</span>
    </div>
  </header>
  <RouterView />
  <Transition name="cookie-transition">
    <dialog class="cookie" v-if="cookies" open @click="cookies=false">
      <div>
        <h2>This webpage uses cookies! 🍪</h2>
        <p>But don't worry, we won't sell your data to any big corp, or anyone else.</p>
        <p>Click here to discard this message.</p>
      </div>
      <img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fpurepng.com%2Fpublic%2Fuploads%2Flarge%2Fpurepng.com-cookiefood-bakery-sweet-cookie-biscuit-941524621515qlctx.png&f=1&nofb=1&ipt=4775ddaed5e03227d733a58df57d073c8e73a01f5af512c90c2356e31f8fd2b7&ipo=images" alt="">
    </dialog>
  </Transition>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
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
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

dialog.cookie {
  position: fixed;
  bottom: 50px;
  left: 50%;
  translate: -50%;
  color: inherit;
  border-radius: 0 20px 20px 0;
  border: none;
  padding: 3px;
  padding-left: 0;
  background: linear-gradient(110deg, transparent, rgb(0, 189, 126));
}

dialog.cookie:hover {
  background: linear-gradient(110deg, transparent, red);
}

dialog.cookie div {
  background: linear-gradient(90deg, var(--color-background), var(--color-background-soft));
  padding: 20px 40px 20px 40px;
  border-radius: 0 20px 20px 0;
}

dialog.cookie img {
  position: absolute;
  bottom: -50px;
  right: calc(100% - 20px);
  height: 200px;
  animation: spin 4s infinite;
  pointer-events: none;
}

@keyframes spin {
  0% {
    transform: rotate3d(0, 1, 0, 0deg);
    filter: drop-shadow(0px 0px 3px wheat);
  }
  70% {
    transform: rotate3d(0, 1, 0, 360deg);
    filter: drop-shadow(0px 0px 20px goldenrod);
  }
  100% {
    transform: rotate3d(0, 1, 0, 360deg);
    filter: drop-shadow(0px 0px 3px wheat);
  }
}

.cookie-transition-enter-active,
.cookie-transition-leave-active {
  transition: all 2s ease;
  opacity: 100%;
}

.cookie-transition-enter-from,
.cookie-transition-leave-to {
  transform: translateX(200px);
  opacity: 0%;
}
.cookie-transition-leave-to {
  transform: translateY(70px);
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
}
</style>
