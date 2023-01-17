<template>
  <div class="w-screen h-screen">
    <div class="bg-white w-full h-[5%] flex flex-row justify-between min-h-[30px]">
      <img src="@/assets/reports_assets/logo.png" alt="Verum" class="px-5">
      <button class="px-5" @click="$store.state.show_navmenu = !$store.state.show_navmenu">
        <i class="fa-solid fa-bars"></i>
      </button>
    </div>
    <div v-if="$store.state.show_navmenu" class="w-full h-[95%] fixed bg-black opacity-50">
      <div v-for="menu, index in $store.state.form_counter.types.persona_fisica.menus" :key="index">
        <button @click="assign(menu)" class="text-white">{{menu.name}}</button> 
      </div>
    </div>
    <div
      class="w-full h-[95%] flex flex-col justify-center items-center"
      style="background-image: url('wave-haikei.png');
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;">
      <router-view />
    </div>
  </div>
</template>
<script>
  export default {
    methods: {
      assign: function(menu){
        console.log(menu)
        this.$store.state.form_counter.selector = menu.index;
        console.log(this.$store.state.form_counter.selector)
      }
    }    
  }
</script>
