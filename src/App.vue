<template>
  <router-view />
</template>

<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  height: 1024px;
  width: 3584px;
}
body {
  margin: 0;
  height: 1024px;
  width: 3584px;
  background-image: url("./assets/bg.png");
  background-repeat: no-repeat;
  background-size: 3584px,1024px;
}
html {
  height: 1024px;
  width: 100%;
  background-color: #282c34;
}
</style>
