<template>
  <div class="main-body">
    <iframe
      src="http://10.136.211.125:8080/jndpportal/browseTdrmjzjnjpybb.xhtml"
      id="frames"
      frameborder="0"
      sandbox="allow-forms allow-scripts allow-same-origin allow-popups"
      style="height: 100%; width: 100%"
    ></iframe>
    <!-- <view>
      <web-view :src="url_"></web-view>
    </view> -->
  </div>
</template>
<script>
export default {
  data() {
    return {
      url_: "http://10.136.211.125:8080/jndpportal/browseTdrmjzjnjpybb.xhtml",
    };
  },

  onLoad() {
    console.log("agree");
  },
  onShow() {},
  methods: {
    // open(){
    //   window.location.href = 'http://www.baidu.com'
    // }
  },
  created() {
    // this.open()
  },
};
</script>
<style  scoped lang='less'>
.main-body {
  height: 914px;
  background-color: #fff;
}
</style>