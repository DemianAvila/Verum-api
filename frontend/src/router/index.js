import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "@/views/LoginView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/forgot_pass",
    name: "forgot_pass",
    component: () =>
      import("@/views/ForgetPassView.vue")
  },
  {
    path: "/definitive_message",
    name: "definitive_message",
    component: () =>
      import("@/views/DefinitiveMessageView.vue")
  },
  /*{
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(// webpackChunkName: "about" // "../views/AboutView.vue"),
  },*/
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
