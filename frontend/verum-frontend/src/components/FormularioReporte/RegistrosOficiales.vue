<template>
    <div class="w-full
    h-full
    flex
    flex-col">
      <div class="w-full
      h-[10%]
      overflow-y-auto">
        <h1 class="text-3xl p-3 font-bold">Registros oficiales</h1>
      </div>
    <div class="w-[48%]
    h-[90%]
    overflow-y-auto">
      <div class="p-3">
        <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="RFC" v-model="$store.state.report_form.rfc">
      </div>
      <div class="p-3">
        <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="CURP" v-model="$store.state.report_form.curp">
      </div>
    </div>
  </div>
</template>

<script>
    export default{
        name: "RegistrosOficiales"
    }
</script>

