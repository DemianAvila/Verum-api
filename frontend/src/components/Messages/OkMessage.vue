<template>
  <div class="bg-green-200 w-full h-full border-2 
  border-green-700 text-green-700 flex items-center justify-center
  font-bold p-5 rounded-lg">
    {{ ok_message }}    
  </div>
</template>
<script>
export default {
  name:"OkMessage",
  props: [
    "ok_message"
  ]
}
</script>