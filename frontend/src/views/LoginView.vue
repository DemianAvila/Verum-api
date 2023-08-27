<template lang="">
  <div class="w-full h-full login_gradient">
    <LogoBigHeader />
    <div class="w-full h-[20%] flex flex-col items-center justify-center">
      <CustomTitle5 text="Ingresa" class="w-[80%] h-[10%] m-5"/>
      <TextInputs v-for="item, index in this.$store.state.login_structure.login_inputs" 
      :key="index"
      :class="item.class" 
      :placeholder="item.placeholder"
      :type="item.type"
      v-model="item.data"
      @keydown.enter="login()"/>
      <MainButton text="Ingresar"
      class="w-[80%] h-[10%] m-5"
      @click="login()"/>
      <LinkForward text="Olvidé mi contraseña" 
      href="/forgot_pass"
      class="w-[80%] h-[10%]"/>
      <ErrorMessage 
      class="w-[80%] m-5"
      v-if="error" 
      :error_message="error_message" />
    </div>
  </div>
</template>
<script>
import TextInputs from "@/components/Inputs/TextInputs.vue";
import CustomTitle5 from "@/components/Titles/CustomTitle5.vue";
import MainButton from "../components/Buttons/MainButton.vue";
import LinkForward from "../components/Links/LinkForward.vue";
import ErrorMessage from "../components/Messages/ErrorMessage.vue";
import LogoBigHeader from "../components/Headers/LogoBigHeader.vue";
export default {
  components: {
    TextInputs,
    CustomTitle5,
    MainButton,
    LinkForward, 
    ErrorMessage,
    LogoBigHeader
  },
  mounted: function(){
    this.$store.state.components_info = false
  },
  data: function(){
    return {
      error: false,
      error_message: ""
    }
  },
  methods: {
    login: function(){
      //RESTART THE ERROR BOX MESSAGE
      this.error = false;
      this.error_message = "";
      //GET THE LOGIN INFO FROM THE COMPONENTS
      const login_info = this.$store.state.login_structure.login_inputs;
      const mail = login_info.filter(x => x.field_name === "email")[0].data;
      const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      const pass = login_info.filter(x => x.field_name === "password")[0].data
      //CHECK THE MAIL CASES, RETURN AND RENDER AN ERROR IF WRONG
      if (mail==="") {
        this.error = true;
        this.error_message = "Introduce tu correo electrónico de acceso";
        return null;
      } else if (!(emailRegex.test(mail))){
        this.error = true;
          this.error_message = "Introduce un correo electrónico válido";
          return null;
      }
      if (pass==="") {
        this.error = true;
        this.error_message = "Introduce tu contraseña";
        return null;
      }
      //CHECH THE API ENDPOINT TO STORE USERS
      //SAVE THE CREDENTIALS IN SESSION COOKIES
      sessionStorage.email = mail;
    }
  }
}
</script>

<style>
  .login_gradient{
    background: rgb(255,255,255);
    background: linear-gradient(180deg, rgba(255,255,255,1) 10%, rgba(9,9,121,0) 100%); 
  }
</style>