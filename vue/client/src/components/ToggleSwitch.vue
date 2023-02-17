
Instructions

v-model works, it is a boolean
container styleable directly
style ball with :deep(.classname .ball) where .classname is the name you gave to the switch
conditional styles with .active and .focused (on container)
example, set ball colour to lime when it's active:
:deep(.classname.active .ball) {
    background-color: lime; 
}


<script setup lang="ts">
import { ref, defineEmits, defineProps } from 'vue';

const focused = ref(false)

defineProps(['modelValue'])
defineEmits(['update:modelValue'])
</script>

<template>
    <label :class="{active: modelValue, focused: focused}">
        <input
            type="checkbox"
            :checked="modelValue"
            @input="$emit('update:modelValue', ($event as any).target.checked)"
            @focus="focused=true"
            @blur="focused=false">
        <div class="ball"></div>
    </label>
</template>

<style scoped>
label {
    display: inline-block;
    border: 1px solid var(--color-text);
    min-height: fit-content;
    min-inline-size: 1em;
    width: 3em;
    border-radius: 10000em;
    box-shadow: #0003 0 0 5px 5px inset;
}
label.focused {
    box-shadow: #0003 0 0 5px 5px inset, gold 0 0 2px 2px;
}
label input {
    position: relative;
    opacity: 0%;
    pointer-events: none;
}
.ball {
    position: absolute;
    top: 0;
    left: 0;
    display: inline-block;
    height: calc(100% - 6px);
    margin: 3px;
    aspect-ratio: 1;
    background: var(--color-heading);
    transition: all 250ms ease-out;
    border-radius: 50%;
}
input:checked ~ .ball {
    left: unset;
    left: 100%;
    translate: calc(-100% - 6px);
}
</style>