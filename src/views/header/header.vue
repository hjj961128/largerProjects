<template>
  <div class="header">
    <div class="tab-list">
      <div class="one" @click="goOne('1')">
        <img v-if="yemian == '1'" src="../../assets/shouye2.png" alt="" />
        <img v-else src="../../assets/shouye1.png" alt="" />
      </div>
      <div class="two" @click="goOne('2')">
        <img v-if="yemian == '2'" src="../../assets/meikong2.png" alt="">
        <img v-else src="../../assets/meikong1.png" alt="">
      </div>
      <div class="three" @click="goOne('3')">
        <img v-if="yemian == '3'" src="../../assets/jizu2.png" alt="">
        <img v-else src="../../assets/jizu1.png" alt="">
      </div>
      <div class="four" @click="goOne('4')">
        <img v-if="yemian == '4'" src="../../assets/huanbao2.png" alt="">
        <img v-else src="../../assets/huanbao1.png" alt="">
      </div>
      <div class="six" @click="goOne('6')">
        <img v-if="yemian == '6'" src="../../assets/nenghao2.png" alt="">
        <img v-else src="../../assets/nenghao1.png" alt="">
      </div>
      <div class="five" @click="goOne('5')">
        <img v-if="yemian == '5'" src="../../assets/ceshi2.png" alt="">
        <img v-else src="../../assets/ceshi1.png" alt="">
      </div>
    </div>
    <div class="header-time">
      <div class="time-fen">{{ shifenmiao }}</div>
      <div class="time-zhou">
        <div>{{ nowWeek }}</div>
        <div>{{ nian }}</div>
      </div>
    </div>
  </div>
</template>
  <script>
export default {
  data() {
    return {
      yemian: '1',
      nian: "0000-00-00",
      shifenmiao: "0:0:0",
      nowWeek: "星期一", // 本周周几
    };
  },
  mounted() {
    this.currentTime();
  },
  methods: {
    goOne(val){
      this.yemian = val
      this.$emit('pageNum',val)
      this.shouye = !this.shouye

    },
    //   时间
    currentTime() {
      setInterval(this.getTime, 500);
    },
    getTime() {
      let weeks = [
        "星期日",
        "星期一",
        "星期二",
        "星期三",
        "星期四",
        "星期五",
        "星期六",
      ];

      let wk = new Date().getDay();
      let yy = new Date().getFullYear();
      let mm = new Date().getMonth() + 1;
      let dd = new Date().getDate();
      let hh = new Date().getHours();
      let mf =
        new Date().getMinutes() < 10
          ? "0" + new Date().getMinutes()
          : new Date().getMinutes();
      let ss =
        new Date().getSeconds() < 10
          ? "0" + new Date().getSeconds()
          : new Date().getSeconds();
      this.shifenmiao = hh + ":" + mf + ":" + ss;
      this.nian = yy + "-" + mm + "-" + dd;
      let week = weeks[wk];
      this.nowWeek = week;
      this.time = yy + "-" + mm + "-" + dd + "-" + hh + ":" + mf + ":" + ss;
    },
  },
};
</script>
  
<style scoped lang='less'>
.header {
  width: 100%;
  height: 100%;
  .header-time {
    margin-top: 50px;
    float: right;
    color: #fff;
    height: 50px;
    margin-right: 70px;
    .time-fen {
      float: left;
      font-size: 30px;
      line-height: 100%;
      margin-right: 10px;
      margin-top: 10px;
    }
    .time-zhou {
      float: right;
      text-align: left;
    }
  }
  .tab-list {
    float: left;
    width: 1418px;
    margin-top: 35px;
    margin-left: 953px;
    .one,
    .two,
    .three,
    .four,.five,.six {
      display: inline-block;
      width: 228px;
      height: 54px;
      margin-right: 10px;
      line-height: 54px;
      text-align: center;
      img {
        width: 100%;
        height: 100%;
      }
    }
    .five {
      margin-right: 0px;
    }
  }
}
</style>