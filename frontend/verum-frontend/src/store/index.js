import { createStore } from "vuex";

export default createStore({
  state: {
    show_navmenu: false,
    form_counter: {
      selector: 0,
      types:{
        persona_fisica:{
          menus: [
            {
              name: "Datos generales",
              index: 0
            },
            {
              name: "Estructura",
              index: 1
            },
            {
              name: "Datos generales del principal",
              index: 2
            },
            {
              name: "Antecedentes",
              index: 3
            },
            {
              name: "Registros oficiales",
              index: 4
            },
            {
              name: "Actividades Operacionales",
              index: 5
            },
            {
              name: "Infraestructura",
              index: 6
            },
            {
              name: "Referencias comerciales",
              index: 7
            },
            {
              name: "Información financiera",
              index: 8
            }
          ]
        }    
      }
    },
    report_form: {
      phones: [],
      comercial_references: [{}],
      financial_info: {
        assets: [{}],
        passives: [{}]
      },
    },
  },
  getters: {},
  mutations: {},
  actions: {},
  modules: {},
});
