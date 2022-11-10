<template>
  <div>
    <mark
  style="position:fixed;top:0;bottom:0;left:0;right:0;background:rgba(0,0,0,0);z-index:999;"
  v-show="showSeason"
  @click.stop="showSeason=false"
></mark>
<el-input placeholder="请选择季度" class="input-q" v-model="showValue" style="width:138px;" @focus="showSeason=true">
  <i slot="prefix" class="el-input__icon el-icon-date"></i>
</el-input>
<el-card
  class="box-card"
  style="width:322px;padding: 0 3px 20px;margin-top:10px;;z-index:9999"
  v-show="showSeason"
>
  <div slot="header" class="clearfix" style="text-align:center;padding:0">
    <button
      type="button"
      aria-label="前一年"
      class="el-picker-panel__icon-btn el-date-picker__prev-btn el-icon-d-arrow-left"
      @click="prev"
    ></button>
    <span role="button" class="el-date-picker__header-label">{{year}}年</span>
    <button
      type="button"
      aria-label="后一年"
      @click="next"
      class="el-picker-panel__icon-btn el-date-picker__next-btn el-icon-d-arrow-right"
    ></button>
  </div>
  <div class="text item" style="text-align:center;">
    <el-button
      size="medium"
      style="width:40%;float:left;"
      @click="selectSeason(0)"
    >第一季度</el-button>
  </div>
  <div class="text item" style="text-align:center;">
    <el-button
      size="medium"
      style="float:right;width:40%;"
      @click="selectSeason(1)"
    >第二季度</el-button>
  </div>
  <div class="text item" style="text-align:center;">
    <el-button
      size="medium"
      style="width:40%;float:left;"
      @click="selectSeason(2)"
    >第三季度</el-button>
    
  </div>
  <div class="text item" style="text-align:center;">
    <el-button
      size="medium"
      style="float:right;width:40%;"
      @click="selectSeason(3)"
    >第四季度</el-button>
  </div>
</el-card>
</div>
</template>
<script>
/**
 * @file:  View 组件 季节选择控件
 * @author: v_zhuchun
 * @date: 2019-05-23
 * @description: UI组件  可选择季节
 * @api: valueArr : 季度value defalut['01-03', '04-06', '07-09', '10-12'] 默认值待设置
 */
export default {
  props: {
    valueArr: {
      default: () => {
        return ['01-03', '04-06', '07-09', '10-12']
      },
      type: Array
    },
    getValue: {
      default: () => {},
      type: Function
    },
    defaultValue: {
      default: '',
      type: String
    }
  },
  data() {
    return {
      showSeason: false,
      season: '',
      year: new Date().getFullYear(),
      showValue: ''
    }
  },
  created() {
    if (this.defaultValue) {
      let value = this.defaultValue
      let arr = value.split('-')
      this.year = arr[0].slice(0, 4)
      let str = arr[0].slice(4, 6) + '-' + arr[1].slice(4, 6)
      let arrAll = this.valueArr
      this.showValue = `${this.year}年${arrAll.indexOf(str) + 1}季度`
    }
  },
  watch: {
    defaultValue: function(value, oldValue) {
      let arr = value.split('-')
      this.year = arr[0].slice(0, 4)
      let str = arr[0].slice(4, 6) + '-' + arr[1].slice(4, 6)
      let arrAll = this.valueArr
      this.showValue = `${this.year}年${arrAll.indexOf(str) + 1}季度`
    }
  },
  methods: {
    one() {
      this.showSeason = false
    },
    prev() {
      this.year = this.year * 1 - 1
    },
    next() {
      this.year = this.year * 1 + 1
    },
    selectSeason(i) {
      let that = this
      that.season = (i + 1)
      let arr = that.valueArr[i].split('-')
      that.getValue(that.year + arr[0] + '-' + that.year + arr[1])
      that.showSeason = false
      this.showValue = `${this.year}年${this.season}季度`
      let chuancan = this.year + '-' + this.season
      this.$emit('getValue', chuancan)
    }
  }
}
</script>
<style scoped lang='less'>
.input-q{
  position: relative;
}
.box-card{
  position: absolute;
}

.el-input {
  color: #fff;
}
.el-card.is-always-shadow,
.el-card.is-hover-shadow:focus,
.el-card.is-hover-shadow:hover {
  background: #0d1a28;
  box-shadow: inset 0px -2px 7px 0px rgba(2, 69, 147, 1);
  border-radius: 2px;
  border: none;
}
::v-deep .el-card__header {
  margin: 12px 12px 0px;
  padding: 0px 0px 12px;
}
::v-deep .el-button {
  border: none;
  background-color: #0d1a28;
  color: #fff;
}
::v-deep .el-button:hover {
  border: none;
  background-color: #0d1a28;
  color: #00faf9 !important;
}
::v-deep .el-button + .el-button {
  border: none;
  background-color: #0d1a28;
  color: #fff;
}
</style>