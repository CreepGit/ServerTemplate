<script setup lang="ts">
import { useStateStore } from "@/stores/state";
const state = useStateStore()
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      <template v-if="state.loggedIn">Logged in as '{{ state.user?.username }}'<br></template>
      <template v-else-if="state.user === undefined">Not Logged in, no server conection.<br></template>
      <template v-else>Not Logged in<br></template>
      You’ve successfully created a project with
      <a href="https://vitejs.dev/" target="_blank" rel="noopener">Vite</a> +
      <a href="https://vuejs.org/" target="_blank" rel="noopener">Vue 3</a> +
      <a href="https://www.djangoproject.com/" target="_blank" rel="noopener">Django</a> +
      <a href="https://www.django-rest-framework.org/" target="_blank" rel="noopener">Django Rest Framework</a> + 
      <a href="https://django-allauth.readthedocs.io/en/latest/" target="_blank" rel="noopener">Allauth</a>
    </h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
