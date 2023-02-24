import { ref, computed, devtools } from "vue";
import { defineStore } from "pinia";
import type { Ref, ComputedRef } from 'vue';
import Cookies from 'js-cookie'

function discardEmptyValues(o: Object): Object {
  return Object.fromEntries(Object.entries(o).filter((k, v) => v));
}

interface User {
  auth: boolean,
  username: string,
  email: string,
  url: string,
  specifier: string,
  is_staff: boolean,
}

export const useStateStore = defineStore("state", () => {
  const user: Ref<User|undefined> = ref(undefined);
  const loggedIn: ComputedRef<boolean> = computed(()=>{
    if (user.value == undefined)
      return false;
    return user.value.auth
  })
  // True if running on 'npm run dev', false if app gotten from django
  const runningOnDev = ref(!(devtools == undefined || devtools.enabled == false))
  if (runningOnDev.value)
    document.title = "Dev " + document.title

  if (!runningOnDev.value) {
    fetch("rest/who/")
    .then((data: any) => data.json())
    .then((data: any) => {
      user.value = data;
      console.log(data);
    });
  }

  function setTheme(name: string) {
    document.documentElement.className = name;
    currentTheme.value = name
    localStorage.setItem("preferredColorScheme", name)
  }
  const browserPrefersDarkTheme = ref(false)
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    browserPrefersDarkTheme.value = true
  }
  const currentTheme = ref(localStorage.getItem("preferredColorScheme") || (browserPrefersDarkTheme.value ? "dark" : "light"))
  setTheme(currentTheme.value)

  function logOutUser() {
    let csrftoken = Cookies.get('csrftoken') as string;
    fetch("/accounts/logout/", {
        method: 'POST',
        headers: { "X-CSRFToken": csrftoken },
    }).then(data=>console.log("Logout:", data.status))
  }

  return { user, loggedIn, runningOnDev, setTheme, currentTheme, browserPrefersDarkTheme, logOutUser };
});
