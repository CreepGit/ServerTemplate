<script lang="ts" setup>
import { ref } from 'vue';
const cookies = ref(false)
setTimeout(()=>{
  cookies.value = true
}, 1500)
</script>

<template>
  <Transition name="cookie-transition">
    <dialog class="cookie" v-if="cookies" open @click="cookies=false">
      <div>
        <h2>This webpage uses cookies! 🍪</h2>
        <p>But don't worry, we won't sell your personal data to a big corporation, or anyone else for that matter.
        <span class="highlightOnHover">Click to discard</span> this message or <span @click.stop class="learnMore">click here to learn more.</span></p>
      </div>
      <img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fpurepng.com%2Fpublic%2Fuploads%2Flarge%2Fpurepng.com-cookiefood-bakery-sweet-cookie-biscuit-941524621515qlctx.png&f=1&nofb=1&ipt=4775ddaed5e03227d733a58df57d073c8e73a01f5af512c90c2356e31f8fd2b7&ipo=images" alt="">
    </dialog>
  </Transition>
</template>

<style scoped>
dialog.cookie {
  position: fixed;
  left: 0;
  bottom: 0;
  color: inherit;
  border: none;
  padding: 3px;
  padding-bottom: 0;
  background: linear-gradient(0deg, transparent, rgb(0, 189, 126));
  border-radius: 20px 20px 0 0;
}

dialog.cookie:hover {
  background: linear-gradient(110deg, transparent, red);
  filter: drop-shadow(0 0 15px red);
  cursor: pointer;
}

dialog.cookie:hover .highlightOnHover {
  color: red;
  text-decoration: underline;
}

.learnMore:hover {
  color: hsla(160, 100%, 37%, 1);
  text-decoration: underline;
}

dialog.cookie div {
  background: linear-gradient(0deg, var(--color-background), var(--color-background-soft));
  padding: 15px;
  border-radius: 20px 20px 0 0;
}

dialog.cookie img {
  position: absolute;
  bottom: calc(100% - 30px);
  right: 50%;
  translate: 50%;
  height: 200px;
  animation: spin 4s infinite;
  pointer-events: none;
}

@keyframes spin {
  0% {
    transform: rotate3d(0, 10, -1, 0deg);
    filter: drop-shadow(0px 0px 3px wheat);
  }
  70% {
    transform: rotate3d(0, 10, -1, 360deg);
    filter: drop-shadow(0px 0px 20px goldenrod);
  }
  100% {
    transform: rotate3d(0, 10, -1, 360deg);
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
    transform: translateY(200px);
    opacity: 0%;
}
.cookie-transition-leave-to {
    transform: translateY(70px);
}


@media (min-width: 700px) {
    dialog.cookie {
        left: 50%;
        min-width: 65%;
        translate: -50%;
        bottom: 50px;
        border-radius: 0 20px 20px 0;
        background: linear-gradient(110deg, transparent, rgb(0, 189, 126));
        padding-left: 0;
        padding-bottom: 3px;
    }

    .cookie-transition-enter-from,
    .cookie-transition-leave-to {
        transform: translateX(200px);
        opacity: 0%;
    }
    .cookie-transition-leave-to {
        transform: translateY(70px);
    }

    dialog.cookie div {
        background: linear-gradient(90deg, var(--color-background), var(--color-background-soft));
        padding: 20px 40px 20px 40px;
        border-radius: 0 20px 20px 0;
    }

    dialog.cookie img {
        bottom: -50px;
        right: calc(100% - 20px);
        translate: 0;
    }
}
</style>