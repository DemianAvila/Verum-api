<template>
    <div 
    class="w-full
    h-full
    flex
    flex-col">
      <div class="w-full
      h-[10%]
      overflow-y-auto">
        <h1 class="text-3xl p-3 font-bold">Datos generales del principal</h1>
      </div>
      <div class="w-full
      h-full
      flex
      flex-row
      justify-between">
        <div class="w-[48%]
        h-[90%]
        overflow-y-auto">
          <div class="p-3 w-full flex justify-between">
            <input class="bg-blue-200 w-[48%] py-1 rounded-lg" type="text" placeholder="Nombre" required v-model="$store.state.report_form.name">
            <input class="bg-blue-200 w-[48%] py-1 rounded-lg" type="text" placeholder="Segundo nombre" v-model="$store.state.report_form.sec_name">
          </div>
          <div class="p-3 w-full flex justify-between">
            <input class="bg-blue-200 w-[48%] py-1 rounded-lg" type="text" placeholder="Primer apellido" required v-model="$store.state.report_form.first_last_name">
            <input class="bg-blue-200 w-[48%] py-1 rounded-lg" type="text" placeholder="Segundo apellido" required v-model="$store.state.report_form.last_last_name">
          </div>
          <div class="p-3">
            <input class="bg-blue-200 w-full py-1 rounded-lg " type="text" placeholder="Nacionalidad" v-model="$store.state.report_form.nationality">
          </div>
          <div class="p-3">
            <input class="bg-blue-200 w-full py-1 rounded-lg " type="text" placeholder="Originario de" v-model="$store.state.report_form.from">
          </div>
          <div class="flex flex-col p-3">
            <div class="flex flex-row">
              <p class="w-[40%]">Fecha de nacimiento</p> 
              <input class="bg-blue-200 w-[60%] py-1 rounded-lg" type="date" v-model="nacimiento">
            </div>
            <div class="p-3 w-full" v-if="Number.isInteger(edad())">
              Edad {{edad()}} años
            </div>
          </div>
          <div class="p-3">
            <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="Ocupación" v-model="$store.state.report_form.ocupation">
          </div>
        </div>
        <div class="w-[48%]
        h-[90%]
        overflow-y-auto">
          <p>Domicilio particular</p>
          <div class="p-3">
            <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="Calle" required v-model="$store.state.report_form.steet_part">
          </div>
          <div class="p-3 w-full flex justify-between">
            <input class="bg-blue-200 w-[48%] py-1 rounded-lg" type="text" placeholder="Numero exterior" required v-model="$store.state.report_form.ext_num_part">
            <input class="bg-blue-200 w-[48%] py-1 rounded-lg" type="text" placeholder="Numero interior" v-model="$store.state.report_form.int_num_part"/>
          </div>
          <div class="p-3">
            <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="Código postal" v-model="$store.state.report_form.zip_code_part">
          </div>
          <div class="p-3">
            <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="Colonia" v-model="$store.state.report_form.location_part">
          </div>
          <div class="p-3">
            <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="Estado" v-model="$store.state.report_form.state_part">
          </div>
          <div class="p-3">
            <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="País" v-model="$store.state.report_form.country_part">
          </div>
        </div>
      </div>
    </div>
</template>

<script>

export default {
    name: 'DatosGenerales',
    data: function () {
    return {
      nacimiento: ""
    }
  },
  methods: {
    edad: function(){
      let cumple = new Date(this.nacimiento);
      let diferencia = Date.now() - cumple;
      //let anios = new Date(diferencia);
      this.$mostrar_edad = true;
      return  Math.floor(diferencia/1000/60/60/24/365);
    }
  }
}
</script>

