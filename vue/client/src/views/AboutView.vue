<script setup lang="ts">
import { useStateStore, type User } from "@/stores/state";
const state = useStateStore()

function submitName(e: any) {
  if (!state.user) return console.error("Client does not detect logged in user")
  state.fetch2(state.user.url as string, "PATCH", {username: e.target[0].value}).then((data: User)=>
    state.fetch2("/rest/who/").then((data: User)=>{
      state.user = data
    })
  )
}
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
    <template v-if="state.user?.auth">
      <label class="usernameChanger">
        Change username to
        <br>
        <form @submit.prevent.stop="submitName">
          <div class="inputGroup">
            <input type="text" name="name" :value="state.user.username">
            <input type="submit" value=">">
          </div>
        </form>
      </label>
    </template>
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
.usernameChanger {
  margin-top: 1em;
}
.inputGroup * {
  border: 1px solid var(--color-text);
  border-width: 1px 0px 1px 0px;
  background: var(--color-background-mute);
  color: var(--color-heading);
  padding: 0.2em 0.5em;
}
.inputGroup *:first-child {
  border-width: 1px 0px 1px 1px;
  border-radius: 1000px 0 0 1000px;
}
.inputGroup *:last-child {
  border-width: 1px 1px 1px 0px;
  border-radius: 0 1000px 1000px 0;
}
.inputGroup input[type=submit]:hover {
  background-color: var(--color-text);
  color: var(--color-background-mute);
}
</style>
