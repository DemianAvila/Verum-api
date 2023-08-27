<template>
  <button class="bg-[#3730a3]
  text-white
  w-full
  h-full
  rounded-lg
  p-5
  flex
  items-center
  justify-center
  font-bold">
    {{ text }}
  </button>
</template>
<script>
export default {
  name: "MainButton",
  props: [
    "text"
  ]
}
</script>
