<template>
    <div
    class="w-full
    h-full
    flex
    flex-col">
        <div class="w-full
        h-[10%]
        overflow-y-auto">
            <h1 class="text-3xl p-3 font-bold">Datos generales</h1>
        </div>
        <div class="w-full
        h-full
        flex
        flex-row
        justify-between">
            <div class="w-[48%]
            h-[90%]
            overflow-y-auto">
                <p class="text-xl font-bold p-3">Domicilio fiscal</p>
                <div class="p-3">
                    <input class="bg-blue-200 w-full py-1 rounded-lg " type="text" placeholder="Calle" required v-model="$store.state.report_form.steet">
                </div>
                <div class="p-3 w-full flex justify-between">
                    <input class="bg-blue-200 w-[48%] py-1 rounded-lg" type="text" placeholder="Numero exterior" required v-model="$store.state.report_form.ext_num">
                    <input class="bg-blue-200 w-[48%] py-1 rounded-lg" type="text" placeholder="Numero interior" v-model="$store.state.report_form.int_num"/>
                </div>
                <div class="p-3">
                    <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="Código postal" v-model="$store.state.report_form.zip_code">
                </div>
                <div class="p-3">
                    <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="Colonia" v-model="$store.state.report_form.location">
                </div>
                <div class="p-3">
                    <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="Estado" v-model="$store.state.report_form.state">
                </div>
                <div class="p-3">
                <input class="bg-blue-200 w-full py-1 rounded-lg" type="text" placeholder="País" v-model="$store.state.report_form.country">
                </div>
            </div>

            <div class="w-[48%]
            h-[90%]
            overflow-y-auto">
                <p class="text-xl font-bold p-3">Datos de contacto</p>
                <div class="p-3 flex flex-row justify-between" v-for="telefono, index in num_telefono" :key="index">
                    <input type="text" class="bg-blue-200 w-[80%] py-1 rounded-lg" placeholder="Teléfono" :value="telefono">
                    <button class="bg-blue-900 text-white w-[10%]" @click="num_telefono.splice(index, 1)">-</button>
                </div>
                <div class="px-3">
                    <button class="bg-blue-900 text-white py-1 rounded-lg px-2"  @click="num_telefono.push('')">Añadir número telefónico</button>
                </div>
                <div class="p-3">
                    <input type="text" class="bg-blue-200 w-full py-1 rounded-lg" placeholder="Correo electrónico" v-model="$store.state.report_form.email">
                </div>
                <div class="p-3">
                    <input type="text" class="bg-blue-200 w-full py-1 rounded-lg" placeholder="Página web" v-model="$store.state.report_form.web_page">
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'DomicilioFiscal',
    data: function () {
    return {
      num_telefono: [""]
    }
  }
}
</script>
