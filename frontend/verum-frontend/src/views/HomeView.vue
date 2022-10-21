<template>
  <div class="w-[80%]
  h-[80%]
  bg-white
  rounded-lg
  p-16">
    <button v-if="form_counter>0" @click="form_counter-=1">↑</button>
    <DomicilioFiscal v-if="form_counter==0"></DomicilioFiscal>
    <EstructurA v-else-if="form_counter==1"></EstructurA>
    <DatosGenerales v-else-if="form_counter==2"></DatosGenerales>
    <AntecedenteS v-else-if="form_counter==3"></AntecedenteS>
    <RegistrosOficiales v-else-if="form_counter==4"></RegistrosOficiales>
    <ActividadesOperaciones v-else-if="form_counter==5"></ActividadesOperaciones>
    <button v-if="form_counter<5" @click="form_counter+=1">↓</button>
    <button @click="print_obj()">Guardar</button>
  </div>
</template>



<script>
import DomicilioFiscal from '@/components/FormularioReporte/DomicilioFiscal.vue';
import EstructurA from '@/components/FormularioReporte/EstructurA.vue';
import DatosGenerales from '@/components/FormularioReporte/DatosGenerales.vue';
import AntecedenteS from '@/components/FormularioReporte/AntecedenteS.vue';
import RegistrosOficiales from '@/components/FormularioReporte/RegistrosOficiales.vue';
import ActividadesOperaciones from '@/components/FormularioReporte/ActividadesOperaciones.vue';
import { jsPDF } from "jspdf";


export default {
  name: 'HomeView',
  components: {
    DomicilioFiscal,
    EstructurA,
    DatosGenerales,
    AntecedenteS,
    RegistrosOficiales,
    ActividadesOperaciones
},
  data: function () {
    return {
      num_telefono: [""],
      sociedad_privada: false, 
      nacimiento: "",
      form_counter: 0
    }
  },
  methods: {
    edad: function(){
      let cumple = new Date(this.nacimiento);
      let diferencia = Date.now() - cumple;
      //let anios = new Date(diferencia);
      return  Math.floor(diferencia/1000/60/60/24/365);
    },
    print_obj: function(){
      console.log(this.$store.state.report_form);
      const doc = new jsPDF();
      var logo = "reports_assets/logo.png";
      doc.addImage(logo, 'PNG', 10, 4, 60, 30);
      var address_str = "Calle 27 No. 283, Col. Jardines de Santa Clara, C.P. 55120, Ecatepec, Edo de México. Tel.- 55 + 5775 – 9254 www.verumexico.com.mx"
      doc.setFontSize(8);
      doc.text(30, 33, address_str);
      let y_pos = 50;
      const report_form = this.$store.state.report_form;
      doc.setFontSize(18);
      Object.keys(report_form).forEach(function (key){
        console.log(key);
        doc.text(10, y_pos, `${key}: ${report_form[key]}`);
        y_pos += 10;
      });
      doc.save("reporte_empresa.pdf");
    }
  }
}
</script>
