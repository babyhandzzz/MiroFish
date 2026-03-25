<template>
  <router-view />
</template>

<script setup>
// Use Vue Router to manage pages
</script>

<style>
/* Global style reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: 'Inter', 'Space Grotesk', 'Noto Sans SC', system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #0A0A0A;
  background-color: #ffffff;
}

/* Scrollbar styles */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #C8CDD5;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #6B7280;
}

/* Global button styles */
button {
  font-family: inherit;
}
</style>
