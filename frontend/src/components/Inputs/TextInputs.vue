<template>
  <input class="p-5 w-full h-full rounded-lg bg-[#e2e8f0]"
  :type="type" 
  :placeholder="placeholder"
  @input="captureInput()"
  v-model="input"
  >
</template>
<script>
export default {
    name: "TextInputs", 
    data: function(){
      return {
        input: null
      }
    },
    props: [
      "placeholder",
      "type"
    ],
    emits: [
      "emitInput"
    ],
    methods: {
      captureInput: function(){
        this.$emit("emitInput", this.input)
      }
    }

}
</script>
