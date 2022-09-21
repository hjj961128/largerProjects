<template>
  <div class="home" style="height: 100%; width: 100%">
    <!-- 头部区域 -->
    <div class="body-header-div">
      <sellheader></sellheader>
    </div>
    <!-- 数据展示区域 -->
    <div class="body-content">
      <sellcontent></sellcontent>
    </div>
  </div>
</template>

<script>
import sellheader from './header/header.vue'
import sellcontent from './sellcontent/sellcontent.vue'

export default {
  name: 'Home',
  components: {
    sellheader,
    sellcontent
  },
}
</script>
<style scoped lang="less">
.body-header-div{
  width: 100%;
  height: 95px;
  margin: auto;
  display: flex;
  flex-direction: row;
}
.body-content{
  height: 69%;
  margin-left: 10px;
  margin-right: 10px;
}
</style>
