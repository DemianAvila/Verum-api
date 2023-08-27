import { createStore } from "vuex";
import components_info from "@/store/show_components/components_info.js"
import login_structure from "@/store/show_components/login_structure.js"

export default createStore({
  state: {
    components_info: components_info,
    login_structure: login_structure
  },
  getters: {},
  mutations: {},
  actions: {},
  modules: {},
});
