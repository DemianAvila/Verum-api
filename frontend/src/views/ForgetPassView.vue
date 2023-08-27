<template>
  <div class="w-full h-full login_gradient">
    <LogoBigHeader />
    <div class="w-full h-[40%] flex flex-col items-center justify-center">
      <CustomTitle5 text="Recuperar la contraseña" class="w-[80%] h-[10%] m-5"/>
      <TextInputs 
      class="w-[80%] h-[10%] m-5" 
      placeholder="Ingresa tu correo"
      type="text"
      @keydown.enter="tryToRecover()"
      v-model="email"/>
      <MainButton text="Recupera tu contraseña"
      class="w-[80%] h-[10%] m-5"
      @click="tryToRecover()"/>
      <ErrorMessage 
      class="w-[80%] m-5"
      v-if="error" 
      :error_message="error_message" />
    </div>
  </div>
</template>
<script>
  import CustomTitle5 from "@/components/Titles/CustomTitle5.vue";
  import TextInputs from "../components/Inputs/TextInputs.vue";
  import MainButton from "../components/Buttons/MainButton.vue";
  import ErrorMessage from "../components/Messages/ErrorMessage.vue";
  import LogoBigHeader from "../components/Headers/LogoBigHeader.vue";

  export default {
    components: {
      CustomTitle5,
      TextInputs,
      MainButton,
      ErrorMessage,
      LogoBigHeader
    },
    data: function(){
      return {
        email: "",
        error: false,
        error_message : ""
      }
    },
    mounted: function(){
      this.$store.state.components_info = false
    },
    methods: {
      tryToRecover: function(){
        //RESTART THE ERROR BOX MESSAGE
        this.error = false;
        this.error_message = "";
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        //CALL THE API
        if (this.email==="") {
          this.error = true;
          this.error_message = "Introduce tu correo electrónico de acceso";
          return null;
        } else if (!(emailRegex.test(this.email))){
          this.error = true;
          this.error_message = "Introduce un correo electrónico válido";
          return null;
        }
        //SEND TO A RETURN SCREEN
        this.$router.push({
          path:"/definitive_message",
          query: {
            "level": "ok",
            "type": "reset_pass",
            "goto": "/"
          }
        })
      }
    }
  }
</script>
