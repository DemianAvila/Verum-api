<template>
  <div class="w-full h-full flex flex-col">
    <div class="w-full h-[10%] overflow-y-auto">
      <h1 class="text-3xl p-3 font-bold">Infraestructura</h1>
    </div>
    <div class="w-[48%] h-[90%] overflow-y-auto">
      <div class="p-3">
        <input
          class="bg-blue-200 w-full py-1 rounded-lg"
          type="text"
          placeholder="Inmueble"
          v-model="$store.state.report_form.property"
        />
      </div>
      <div class="p-3">
        <input
          class="bg-blue-200 w-full py-1 rounded-lg"
          type="text"
          placeholder="Superficie"
          v-model="$store.state.report_form.surface"
        />
      </div>
      <div class="p-3">
        <input
          class="bg-blue-200 w-full py-1 rounded-lg"
          type="text"
          placeholder="Distribución"
          v-model="$store.state.report_form.distribution"
        />
      </div>
      <div class="p-3">
        <input
          class="bg-blue-200 w-full py-1 rounded-lg"
          type="text"
          placeholder="Anexos"
          v-model="$store.state.report_form.attached"
        />
      </div>
      <div class="p-3">
        <input
          class="bg-blue-200 w-full py-1 rounded-lg"
          type="text"
          placeholder="Equipo de trabajo"
          v-model="$store.state.report_form.job_equipment"
        />
      </div>
      <div class="p-3">
        <input
          class="bg-blue-200 w-full py-1 rounded-lg"
          type="text"
          placeholder="Equipo de oficina"
          v-model="$store.state.report_form.office_equipment"
        />
      </div>
      <div class="p-3">
        <input
          class="bg-blue-200 w-full py-1 rounded-lg"
          type="text"
          placeholder="Equipo de transporte"
          v-model="$store.state.report_form.transport_equipment"
        />
      </div>
      <div class="p-3">
        <input
          class="bg-blue-200 w-full py-1 rounded-lg"
          type="text"
          placeholder="Seguros"
          v-model="$store.state.report_form.insurances"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InfraestructurA",
};
</script>
