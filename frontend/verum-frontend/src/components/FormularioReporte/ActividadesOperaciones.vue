<template>
    <div
    class="w-full
    h-full
    flex
    flex-col">
        <div class="w-full
        h-[10%]">
            <h1 class="text-3xl p-3 font-bold">Actividades y operaciones</h1>
        </div>
        <div class="w-full
        h-full
        flex
        flex-row
        justify-between">
            <div class="w-[48%]
            h-[90%]
            overflow-y-auto">   
                <div class="w-full h-[25%] p-3">
                    <p>Actividad principal</p>
                    <textarea class="bg-blue-200 w-full h-[85%] py-1 rounded-lg" v-model="$store.state.report_form.main_activities"></textarea>
                </div>
                <div class="w-full h-[25%] p-3">
                    <p>Principales productos</p>
                    <textarea class="bg-blue-200 w-full h-[85%] py-1 rounded-lg" v-model="$store.state.report_form.main_products"></textarea>
                </div>
                <div class="w-full h-[25%] p-3">
                    <p>SCIAN</p>
                    <textarea class="bg-blue-200 w-full h-[85%] py-1 rounded-lg" v-model="$store.state.report_form.scian"></textarea>
                </div>
                <div class="w-full h-[25%] p-3">
                    <p>Marcas que se comercializan</p>
                    <textarea class="bg-blue-200 w-full h-[85%] py-1 rounded-lg" v-model="$store.state.report_form.comercialized_brands"></textarea>
                </div>
                <div class="w-full h-[25%] p-3">
                    <p>Método de operaciones</p>
                    <textarea class="bg-blue-200 w-full h-[85%] py-1 rounded-lg" v-model="$store.state.report_form.operation_method"></textarea>
                </div>
                
                
            </div>
            <div class="w-[48%]
            h-[90%]
            overflow-y-auto"> 
                11<div class="w-full h-[25%] p-3">
                    <p>Principales clientes</p>
                    <textarea class="bg-blue-200 w-full h-[85%] py-1 rounded-lg" v-model="$store.state.report_form.main_customers"></textarea>
                </div>  
                <div class="w-full h-[25%] p-3">
                    <p>Alcance</p>
                    <textarea class="bg-blue-200 w-full h-[85%] py-1 rounded-lg" v-model="$store.state.report_form.reach"></textarea>
                </div>
                <div class="w-full p-3">
                    <div class="flex flex-row">
                        <p class="w-[30%]">Importaciones</p>
                        <input type="checkbox" v-model="importaciones">
                    </div>
                    <div class="w-full h-[40%]" v-if="importaciones">
                        <textarea class="bg-blue-200 w-full h-[85%] py-1 rounded-lg" v-model="$store.state.report_form.importation"></textarea>
                    </div>  
                    <div class="flex flex-row">
                        <p class="w-[30%]">Exportaciones</p>
                        <input type="checkbox" v-model="exportaciones">
                    </div>
                    <div class="w-full h-[40%]" v-if="exportaciones">
                        <textarea class="bg-blue-200 w-full h-[85%] py-1 rounded-lg" v-model="$store.state.report_form.exportation"></textarea>
                    </div>                   
                </div>
                <div class="w-full h-[25%] p-3">
                    <p>Personal que labora en la empresa</p>
                    <textarea class="bg-blue-200 w-full h-[85%] py-1 rounded-lg" v-model="$store.state.report_form.working_staff"></textarea>
                </div>
                <div class="w-full h-[25%] p-3">
                    <p>Tamaño de la empresa</p>
                    <textarea class="bg-blue-200 w-full h-[85%] py-1 rounded-lg" v-model="$store.state.report_form.enterprice_size"></textarea>
                </div>
            </div>
        </div>
    </div> 
</template>

<script>

export default {
    name: "ActividadesOperaciones",
    data: function() {
        return {
            importaciones: false,
            exportaciones: false
        }
    }
};
</script>
