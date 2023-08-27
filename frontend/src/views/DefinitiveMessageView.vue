<template>
  <div class="w-full h-full login_gradient">
    <LogoBigHeader />
    <div class="w-full flex flex-col items-center justify-center">
      <div class="w-[80%]">
        <ErrorMessage 
        v-if="$route.query.level==='error'"
        :error_message="message_catalogue[$route.query.type]" 
        />
        <OkMessage
        v-else-if="$route.query.level==='ok'" 
        :ok_message="message_catalogue[$route.query.type]"
        />
      </div>
    </div>
    <LinkForward :href="$route.query.goto" 
    text="Volver"
    class="w-[80%] m-5"/>
  </div>
</template>
<script>
  import LogoBigHeader from '@/components/Headers/LogoBigHeader.vue';
  import ErrorMessage from '@/components/Messages/ErrorMessage.vue';
  import OkMessage from '@/components/Messages/OkMessage.vue';
  import LinkForward from '../components/Links/LinkForward.vue';

  export default {
    components: {
      LogoBigHeader,
      ErrorMessage,
      OkMessage,
      LinkForward
    },
    mounted: function(){
    this.$store.state.components_info = false
    },
    data: function(){
      return {
        message_catalogue:{
          reset_pass: `Si tienes un correo registrado en esta plataforma, \
          revisa tu bandeja de entrada para obtener una liga de reestablecimiento, \
          si deseas darte de alta, contactanos`
        }
      }
    }
  }
</script>

