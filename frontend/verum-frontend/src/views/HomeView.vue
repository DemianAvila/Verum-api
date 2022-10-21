<template>
  <div class="w-[80%] h-[80%] bg-white rounded-lg p-16 overflow-y-scroll">
    <div class="w-full flex flex-row">
      <div class="mx-4">
        <p>Tipo de formato</p>
      </div>
      <div class="mx-4">
        <select
          class="px-4 bg-blue-200 w-full py-1 rounded-lg"
          v-model="this.$store.state.report_form.format"
        >
          <option value="persona_fisica">Persona física</option>
          <option value="persona_moral">Persona moral</option>
        </select>
      </div>
    </div>
    <div v-if="this.$store.state.report_form.format == 'persona_fisica'">
      <button v-if="form_counter > 0" @click="form_counter -= 1">↑</button>
      <DomicilioFiscal v-if="form_counter == 0"></DomicilioFiscal>
      <EstructurA v-else-if="form_counter == 1"></EstructurA>
      <DatosGenerales v-else-if="form_counter == 2"></DatosGenerales>
      <AntecedenteS v-else-if="form_counter == 3"></AntecedenteS>
      <RegistrosOficiales v-else-if="form_counter == 4"></RegistrosOficiales>
      <ActividadesOperaciones v-else-if="form_counter == 5"></ActividadesOperaciones>
      <InfraestructurA v-else-if="form_counter == 6"></InfraestructurA>
      <ReferenciasComerciales v-else-if="form_counter == 7"></ReferenciasComerciales>
      <InformacionFinanciera v-else-if="form_counter == 8"></InformacionFinanciera>
      <button v-if="form_counter < 9" @click="form_counter += 1">↓</button>
      <button @click="print_obj()">Guardar</button>
    </div>
  </div>
</template>

<script>
import DomicilioFiscal from "@/components/FormularioReporte/DomicilioFiscal.vue";
import EstructurA from "@/components/FormularioReporte/EstructurA.vue";
import DatosGenerales from "@/components/FormularioReporte/DatosGenerales.vue";
import AntecedenteS from "@/components/FormularioReporte/AntecedenteS.vue";
import RegistrosOficiales from "@/components/FormularioReporte/RegistrosOficiales.vue";
import ActividadesOperaciones from "@/components/FormularioReporte/ActividadesOperaciones.vue";
import InfraestructurA from "@/components/FormularioReporte/InfraestructurA.vue";

import { jsPDF } from "jspdf";
import ReferenciasComerciales from "@/components/FormularioReporte/ReferenciasComerciales.vue";
import InformacionFinanciera from "@/components/FormularioReporte/InformacionFinanciera.vue";

export default {
  name: "HomeView",
  components: {
    DomicilioFiscal,
    EstructurA,
    DatosGenerales,
    AntecedenteS,
    RegistrosOficiales,
    ActividadesOperaciones,
    InfraestructurA,
    ReferenciasComerciales,
    InformacionFinanciera
},
  data: function () {
    return {
      num_telefono: [""],
      sociedad_privada: false,
      nacimiento: "",
      form_counter: 0,
    };
  },
  methods: {
    edad: function () {
      let cumple = new Date(this.nacimiento);
      let diferencia = Date.now() - cumple;
      //let anios = new Date(diferencia);
      return Math.floor(diferencia / 1000 / 60 / 60 / 24 / 365);
    },
    print_obj: function () {
      console.log(this.$store.state.report_form);
      const doc = new jsPDF();
      //var myImage = new Image();
      let image = require("@/assets/reports_assets/logo.png");
      //myImage.src = 'reports_assets/logo.png';
      //myImage.onload = function(){
        doc.addImage(image, "PNG", 10, 4, 60, 30);
        var address_str =
          "Calle 27 No. 283, Col. Jardines de Santa Clara, C.P. 55120, Ecatepec, Edo de México. Tel.- 55 + 5775 – 9254 www.verumexico.com.mx";
        doc.setFontSize(8);
        doc.text(30, 33, address_str);
        let y_pos = 50;
        const report_form = this.$store.state.report_form;
        doc.setFontSize(18);
        Object.keys(report_form).forEach(function (key) {
          if (key=="xlsx"){
            doc.text(10, y_pos, `${key}:`)
            for (let e of report_form[key]){
              doc.text(10, y_pos, e.join("|"))
              y_pos += 10;
            }
          }
          else{
            console.log(key);
            doc.text(10, y_pos, `${key}: ${report_form[key]}`);
            y_pos += 10;
          }
          
        });
        doc.save("reporte_empresa.pdf");
      //};
      
    },
  },
};
</script>
