<template>
  <div>
    <a :href="href"
      class="text-white
      border-b-2 border-white">
      {{ text }}
    </a>
  </div>
</template>
<script>
export default {
  name:"LinkForward",
  props: [
    "text",
    "href"
  ]   
}
</script>
