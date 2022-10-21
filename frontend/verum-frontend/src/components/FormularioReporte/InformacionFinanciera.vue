<template>
  <div class="w-full h-full flex flex-col overflow-y-scroll">
    <div class="w-full h-[10%]">
      <h1 class="text-3xl p-3 font-bold">Información financiera</h1>
    </div>
    <div class="w-[48%] h-[90%] overflow-y-auto">
      <div class="p-3">
        <p>
          Sube tu archivo excel
        </p>
        <input
          class="bg-blue-200 w-full py-1 rounded-lg"
          type="file"
          ref="file"
          @change="read_file()"
        />
      </div>
    </div>
  </div>
</template>

<script>

import readXlsxFile from 'read-excel-file';
export default {
  name: "InformacionFinanciera",
  methods:{
    read_file: function(){
      let file = this.$refs.file;
      readXlsxFile(file.files[0]).then((rows) =>{
        console.log(rows);
        this.$store.state.report_form.xlsx = rows
      }
      );
      
    }
  }
}
</script>
