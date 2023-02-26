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
  slug: string,
  is_staff: boolean,
}

export const useStateStore = defineStore("state", () => {
  function fetch2(url: string, method: string = ""): Promise<any> {
    const csrftoken = Cookies.get('csrftoken') as string;
    return new Promise(async(resolve, reject)=>{
      fetch(url, {
        headers: { "X-CSRFToken": csrftoken },
        method: method||"GET",
      }).then(async response => {
        if (response.status == 200) {
          try {
            resolve(await response.json())
          } catch (error) {
            if (method == "POST") {
              resolve()
            }
            reject("Can't turn response into JSON")
          }
        }
        reject(`Bad response code ${response.status} (${response.statusText})`)
      })
    })
  }

  function logOutUser() {
    fetch2("/accounts/logout/", "POST").then(()=>{
      fetch2("rest/who/").then((data: User)=>{
        user.value = data
      })
    })
  }

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

  fetch2("rest/who/").then((data: User)=>{
    console.log(data)
    user.value = data
  })

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

  return { user, loggedIn, runningOnDev, setTheme, currentTheme, browserPrefersDarkTheme, logOutUser, fetch2 };
});
