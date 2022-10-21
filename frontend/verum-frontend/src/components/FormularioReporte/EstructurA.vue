<template>
  <div class="w-full h-full flex flex-col">
    <div class="w-full h-[10%] overflow-y-auto">
      <h1 class="text-3xl p-3 font-bold">Estructura</h1>
    </div>
    <div class="w-full h-full flex flex-row justify-between">
      <div class="w-[48%] h-[90%] overflow-y-auto">
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Fundador"
            required
            v-model="$store.state.report_form.founder"
          />
        </div>
        <div class="p-3">
          <textarea
            class="bg-blue-200 h-[10rem] w-full py-1 rounded-lg"
            placeholder="Fecha de establecido"
            v-model="$store.state.report_form.stablished_date"
          ></textarea>
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Denominación Comercial"
            v-model="$store.state.report_form.com_denom"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Registrado a Nombre de: "
            v-model="$store.state.report_form.registred_by"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Propietario Real"
            v-model="$store.state.report_form.real_property"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Encargado de la tienda"
            v-model="$store.state.report_form.in_charge"
          />
        </div>
        <div class="p-3">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="Registrado como"
            v-model="$store.state.report_form.registred_as"
          />
        </div>
        <div class="p-3 flex flex-row">
          <p class="w-[80%]">Sociedad Privada</p>
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="checkbox"
            v-model="sociedad_privada"
          />
        </div>
        <div class="p-3" v-if="sociedad_privada">
          <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="text"
            placeholder="¿Con quien?"
            v-model="$store.state.report_form.private_society"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EstructurA",
  data: function () {
    return {
      sociedad_privada: false,
    };
  },
};
</script>
