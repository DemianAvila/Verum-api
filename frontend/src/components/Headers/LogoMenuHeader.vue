<template lang="">
  <div class="bg-white w-full h-[5%] flex flex-row justify-between min-h-[30px]">
    <img src="@/assets/reports_assets/logo.png" alt="Verum" class="px-5">
    <button class="px-5" @click="$store.state.show_navmenu = !$store.state.show_navmenu">
      <i class="fa-solid fa-bars"></i>
    </button>
  </div>
</template>
<script>
export default {
    name: "LogoMenuHeader",
}
</script>
