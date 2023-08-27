<template>
  <div>
    <h5 class="text-2xl text-[#003b5a] font-bold border-b-2 border-[#003b5a] p-2">
      {{ text }}
    </h5>
  </div>
</template>
<script>
export default {
  name: "CustomTitle5",
  props: [
    "text"
  ]   
}
</script>
