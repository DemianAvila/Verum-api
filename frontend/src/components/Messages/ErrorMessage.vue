<template>
  <div class="bg-red-200 w-full h-full border-2 
  border-red-700 text-red-700 flex items-center justify-center
  font-bold p-5 rounded-lg">
    {{ error_message }}    
  </div>
</template>
<script>
export default {
  name:"ErrorMessage",
  props: [
    "error_message"
  ]
}
</script>