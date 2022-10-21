<template>
  <div class="w-full h-full flex flex-col overflow-y-scroll">
    <div class="w-full h-[10%]">
      <h1 class="text-3xl p-3 font-bold">Referencias Comerciales</h1>
    </div>
    <div class="w-[48%] h-[90%] overflow-y-auto">
      <div v-for="referencia, index in this.$store.state.report_form.comercial_references"
      :key="index" 
      class="w-full
      h-full
      flex
      flex-col">
        <div class="p-3 flex flex-row">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Nombre"
            v-model="referencia.name"
          />
          <button @click="this.$store.state.report_form.comercial_references.splice(index, 1)" class="px-5">-</button>
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Ciudad"
            v-model="referencia.city"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Estado"
            v-model="referencia.state"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Telefono"
            v-model="referencia.phone"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Contacto"
            v-model="referencia.contact"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Tiempo de conocerlos"
            v-model="referencia.reference_time"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Limite de crédito"
            v-model="referencia.credit_limit"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Plazo comercial"
            v-model="referencia.comertial_lapse"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Consumo mensual aproximado"
            v-model="referencia.monthly_bought"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Producto"
            v-model="referencia.product"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Forma de pago"
            v-model="referencia.payments"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Concepto"
            v-model="referencia.concept"
          />
        </div>
      </div>
      <div class="w-[48%] h-[90%]">
        <button @click="this.$store.state.report_form.comercial_references.push({})">
          Añadir referencia comercial
        </button>
      </div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: "ReferenciasComerciales",
};
</script>
