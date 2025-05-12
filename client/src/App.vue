<template>
  <header class="bg-blue-700 shadow-md p-6">
    <div class="flex items-center justify-between">
      <h1 class="text-3xl font-bold text-white tracking-wide">
        📚 Library Management System
      </h1>

      <nav class="flex gap-6">
        <RouterLink :class="navLinkClass('/')" to="/"> Books </RouterLink>
        <RouterLink
          :class="navLinkClass('/borrow-transaction')"
          to="/borrow-transaction"
        >
          Borrow
        </RouterLink>
      </nav>
    </div>
  </header>

  <main class="bg-gray-50 min-h-screen p-6">
    <RouterView />
  </main>
</template>

<script setup>
import { useRoute } from "vue-router";
const route = useRoute();

const navLinkClass = (path) => [
  "px-4 py-2 text-sm font-medium rounded-md transition-all duration-200",
  route.path === path
    ? "bg-white text-blue-700 font-semibold shadow-lg"
    : "text-white hover:bg-blue-600 hover:text-blue-200 hover:shadow-md",
];
</script>

<style scoped>
/* Custom styling for main container */
header {
  border-bottom: 2px solid #e0e7ff;
}

nav a {
  transition: background-color 0.3s, color 0.3s;
}

nav a:hover {
  background-color: #2563eb; /* Tailwind's blue-600 */
  color: white;
}
</style>
