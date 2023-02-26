<script setup lang="ts">
import { useStateStore } from "@/stores/state";
const state = useStateStore()
</script>

<template>
  <div class="about">
    <h1>About you</h1>
    <table>
      <tr v-for="[key, value] in Object.entries(state.user as any)">
        <td>{{ key }}</td>
        <td>{{ value }}</td>
      </tr>
    </table>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
  }
}
</style>
