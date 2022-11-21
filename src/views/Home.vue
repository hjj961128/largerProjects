<template>
  <div class="home" style="height: 100%; width: 100%">
    <!-- 头部区域 -->
    <div class="body-header-div">
      <sellheader @pageNum="pageNum"></sellheader>
    </div>
    <!-- 数据展示区域 -->
    <div class="body-content">
      <sellcontent v-if="pagenumber == '1'"></sellcontent>
      <pageTwo v-if="pagenumber == '2'"></pageTwo>
      <pageThree v-if="pagenumber == '3'"></pageThree>
      <pageFour v-if="pagenumber == '4'"></pageFour>
      <pageFive v-if="pagenumber == '5'"></pageFive>
      <pageSix v-if="pagenumber == '6'"></pageSix>
    </div>
  </div>
</template>

<script>
import sellheader from "./header/header.vue";
import sellcontent from "./sellcontent/sellcontent.vue";
import pageTwo from "./pageTwo/pageTwo.vue";
import pageThree from "./pageThree/pageThree.vue";
import pageFour from "./pageFour/pageFour.vue";
import pageFive from "./pageFive/pageFive.vue";
import pageSix from "./pageSix/pageSix.vue";

export default {
  name: "Home",
  components: {
    sellheader,
    sellcontent,
    pageTwo,
    pageThree,
    pageFour,
    pageFive,
    pageSix
  },
  data() {
    return {
      pagenumber: "1",
    };
  },
  methods: {
    pageNum(val) {
      this.pagenumber = val;
    },
  },
};
</script>
<style scoped lang="less">
.body-header-div {
  width: 100%;
  height: 95px;
  margin: auto;
  display: flex;
  flex-direction: row;
  // padding-top: 25px;
}
.body-content {
  height: 915px;
  width: 3584px;
  // margin-top: 15px;
}
</style>
