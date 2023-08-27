<template>
  <div class="w-screen h-screen">
    <LogoMenuHeader v-if="this.$store.state.components_info.showHeaderBar"/>
    <div
      class="w-full flex flex-col justify-center items-center"
      :class="{
        'h-[95%]': this.$store.state.components_info.showHeaderBar,
        'h-full': !this.$store.state.components_info.showHeaderBar
      }"
      style="background-image: url('wave-haikei.png');
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;">
      <router-view />
    </div>
  </div>
</template>
<script>
  import LogoMenuHeader from "@/components/Headers/LogoMenuHeader.vue"
  export default {
    components: {
      LogoMenuHeader
    }
  }
</script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap');
  body{
    font-family: 'Roboto', sans-serif;
  }
</style>