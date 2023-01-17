<template>
  <div class="w-full h-full flex flex-col ">
    <div class="w-full h-[10%]">
      <h1 class="text-3xl p-3 font-bold">Información financiera</h1>  
    </div>
    <div class="w-full h-[10%]">
      <h1 class="text-1xl  px-3 py-1 font-bold">Activos</h1>
    </div>
    <div class="w-[60%] px-3" v-for="asset, index in $store.state.report_form.financial_info.assets" :key="index">
      <p>Fecha de cierre: </p>
      <input
            class="bg-blue-200 w-full py-1 rounded-lg"
            type="Date"
            placeholder="Fecha de cierre"
            required
            v-model="asset.end_date"
          />
      <div class="flex flex-row py-2">
        <p class="w-[30%]">Caja y bancos: $</p>
        <input
            class="bg-blue-200 w-[70%] py-1 rounded-lg"
            type="number"
            placeholder="Caja y bancos"
            required
            v-model="asset.cash"
          />
      </div>
      <div class="flex flex-row py-2">
        <p class="w-[30%]">Inventarios: $</p>
        <input
            class="bg-blue-200 w-[70%] py-1 rounded-lg"
            type="number"
            placeholder="Inventarios"
            required
            v-model="asset.inventory"
          />
      </div>
      <div class="flex flex-row py-2">
        <p class="w-[30%]">Clientes: $</p>
        <input
            class="bg-blue-200 w-[70%] py-1 rounded-lg"
            type="number"
            placeholder="Clientes"
            required
            v-model="asset.clients"
          />
      </div>
      <div class="flex flex-row py-2">
        <p class="w-full">
          Total: {{sum_assets(asset)}} $
        </p>
      </div>
      <div class="flex flex-row py-2">
        <p class="w-[30%]">Deudores diversos: $</p>
        <input
            class="bg-blue-200 w-[70%] py-1 rounded-lg"
            type="number"
            placeholder="Deudores diversos"
            required
            v-model="asset.debts"
          />
      </div>
      <div class="flex flex-row py-2">
        <p class="w-[30%]">Otros: $</p>
        <input
            class="bg-blue-200 w-[70%] py-1 rounded-lg"
            type="number"
            placeholder="Otros"
            required
            v-model="asset.others"
          />
      </div>
      <div class="flex flex-row py-2">
        <p class="w-full">
          Total activo circulante: {{sum_activo_circulante(asset)}} $
        </p>
      </div>
      <div class="flex flex-row py-2">
        <p class="w-[30%]">Activo fijo: $</p>
        <input
            class="bg-blue-200 w-[70%] py-1 rounded-lg"
            type="number"
            placeholder="Activo fijo"
            required
            v-model="asset.fix_asset"
          />
      </div>
      <div class="flex flex-row py-2">
        <p class="w-[30%]">Depreciacion: $</p>
        <input
            class="bg-blue-200 w-[70%] py-1 rounded-lg"
            type="number"
            placeholder="Depreciación"
            required
            v-model="asset.deprec"
          />
      </div>
      <div class="flex flex-row py-2">
        <p class="w-full">
          Total activo fijo: {{sum_activo_fijo(asset)}} $
        </p>
      </div>
      
    </div>

  </div>
</template>

<script>

export default {
  name: "InformacionFinanciera",
  methods: {
    sum_assets: function(asset){
      
            let result = asset.cash + asset.inventory + asset.clients
            if (! isNaN(result) && typeof(result)=='number'){
              return result;
            }
            else{
              return 0;
            }
    },
    sum_activo_circulante(asset){
      let result = asset.debts + asset.others
      if (! isNaN(result) && typeof(result)=='number'){
              return result;
            }
            else{
              return 0;
            } 
    },
    sum_activo_fijo(asset){
      let result = asset.fix_asset + asset.deprec
      if (! isNaN(result) && typeof(result)=='number'){
              return result;
            }
            else{
              return 0;
            } 
    }
  }
}
</script>
