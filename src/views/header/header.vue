<template>
  <div class="header">
    <div class="tab-list">
      <div class="one">首页</div>
      <div class="two">煤量总控</div>
      <div class="three">
        全网机组可调出力
      </div>
      <div class="four">环保总控</div>
    </div>
    <div class="header-time">
        <div class="time-fen">{{shifenmiao}}</div>
        <div class="time-zhou">
            <div>{{nowWeek}}</div>
            <div> {{nian}}</div>
        </div>
    </div>
    <!-- <span class="header-time">{{ time }}</span> -->
  </div>
</template>
  <script>
export default {
  data() {
    return {
      nian: "0000-00-00",
      shifenmiao: "0:0:0",
      nowWeek:'星期一',// 本周周几
    };
  },
  mounted() {
    this.currentTime();
  },
  methods: {
    //   时间
    currentTime() {
      setInterval(this.getTime, 500);
    },
    getTime() {
        let weeks = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']

        let wk = new Date().getDay()
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
          this.nian = yy + "-" + mm + "-" + dd
		let week = weeks[wk]
		this.nowWeek = week
      this.time = 
        yy + "-" + mm + "-" + dd + "-" + hh + ":" + mf + ":" + ss;
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
    margin-right: 40px;
    .time-fen{
        float: left;
        font-size: 30px;
        line-height: 100%;
        margin-right: 10px;
        margin-top: 10px;
    }
    .time-zhou{
        float: right;
        text-align: left;
    }
  }
  .tab-list{
    float: left;
    background-color: #fff;
    width: 35%;
    .one,.two,.three,.four{
      display: inline-block;
      background-color: pink;
      width: 25%;
      text-align: center;

    }
  }

}
</style>