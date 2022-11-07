<template>
  <div class="main-page">
    <div class="top-search">
      <el-form :model="formInline" class="demo-form-inline">
        <el-form-item>
          <div class="search-list">
            <el-checkbox @change="changeHz" v-model="formInline.checked"
              >汇总</el-checkbox
            >
          </div>
          省份：
          <div class="search-list">浙江省</div>
          集团：
          <div class="search-list">
            <el-select
              v-model="formInline.groupName"
              placeholder="请选择"
              :popper-append-to-body="false"
              @change="getFactoryList"
            >
              <el-option label="所有集团" value="所有集团"></el-option>
              <el-option
                v-for="item in formInline.groupList"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </div>
          电厂：
          <div class="search-list">
            <el-select
              v-model="formInline.factoryName"
              placeholder="请选择"
              :popper-append-to-body="false"
              @change="getJzList"
            >
              <el-option label="所有电厂" value="所有电厂"></el-option>
              <el-option
                v-for="item in formInline.factoryList"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </div>
          机组：
          <div class="search-list">
            <el-select
              v-model="formInline.jzName"
              placeholder="请选择"
              :popper-append-to-body="false"
            >
              <el-option label="所有机组" value="所有机组"></el-option>
              <el-option
                v-for="item in formInline.jzList"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </div>
          报表：
          <div class="search-list">
            <el-select
              v-model="formInline.baobiaoName"
              placeholder="请选择"
              :popper-append-to-body="false"
            >
              <el-option
                v-for="item in formInline.baobiao"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </div>
          <span v-if="formInline.baobiaoName == '1'"> 年份： </span>
          <span v-if="formInline.baobiaoName == '2'">季度：</span>
          <span v-if="formInline.baobiaoName == '3'">月份：</span>

          <!-- <span v-if="formInline.baobiaoName == '1'"> 年份： </span> -->
          <div class="search-list">
            <el-date-picker
              v-if="formInline.baobiaoName == '1'"
              v-model="formInline.choiceyear"
              type="year"
              placeholder="选择年"
              popper-class="date-style"
            >
            </el-date-picker>
            <quarter
              v-model="formInline.jidu"
              @getValue="getValue"
              v-if="formInline.baobiaoName == '2'"
            ></quarter>
            <el-date-picker
              v-if="formInline.baobiaoName == '3'"
              v-model="formInline.months"
              type="month"
              placeholder="选择月"
            >
            </el-date-picker>
          </div>
          <div class="btn1" @click="getCoalStat">
            <img src="../../assets/btn1.png" alt="" />
          </div>
          <div class="btn2" @click="clickBtn2">
            <img src="../../assets/btn2.png" alt="" />
          </div>
        </el-form-item>
      </el-form>
    </div>
    <div class="footer">
      <div class="footer-left">
        <div class="top-left">
          <div id="myChart1"></div>
        </div>
        <div class="top-right">
          <div id="myChart2"></div>
        </div>
        <div class="footer-one">
          <div class="myChart3-left">
            <div class="title">2022原煤量</div>
            <img src="../../assets/chart@4x.png" alt="" />
            <div id="myChart3"></div>
          </div>
        </div>
        <div class="footer-two">
          <div class="myChart3-left">
            <div class="title">2022机端 发电量</div>
            <img src="../../assets/chart@4x.png" alt="" />
            <div id="myChart4"></div>
          </div>
        </div>
      </div>
      <div class="footer-right">
        <div class="table">
          <el-table
            :data="
              tableData.slice(
                (currentPage - 1) * pageSize,
                currentPage * pageSize
              )
            "
            style="width: 100%"
          >
            <el-table-column label="序号" align="center">
              <template slot-scope="scope">
                {{ scope.$index + 1 }}
              </template>
            </el-table-column>
            <el-table-column label="集团" align="center">
              <template slot-scope="scope">
                <div
                  style="
                    width: 172px;
                    height: 26px;
                    background: rgb(16, 42, 64);
                    border-radius: 4.4px;
                  "
                >
                  {{ scope.row.groupName }}
                </div>
              </template>
            </el-table-column>
            <el-table-column prop="factoryName" label="电厂名称" align="center">
            </el-table-column>
            <el-table-column prop="crewName" label="机组名称" align="center">
            </el-table-column>
            <el-table-column prop="index" label="原煤量" align="center">
            </el-table-column>
            <el-table-column prop="terminal" label="机端发电量" align="center">
            </el-table-column>
          </el-table>
          <el-pagination
            style="float: right"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-size="pageSize"
            layout="total, prev, pager, next"
            :total="tableData.length"
          >
          </el-pagination>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import * as echarts from "echarts";
import quarter from "../../components/quarter.vue";
export default {
  components: {
    quarter,
  },
  data() {
    return {
      // 默认显示第几页
      currentPage: 1,
      // 总条数，根据接口获取数据长度(注意：这里不能为空)
      totalCount: 1,
      // 个数选择器（可修改）
      pageSize: 11,
      // 默认每页显示的条数（可修改）
      formInline: {
        checked: true,
        province: "zhejiang",
        groupList: [],
        factoryList: [],
        jzList: [],
        jidus: [
          {
            value: "1",
            label: "第一季度",
          },
          {
            value: "2",
            label: "第二季度",
          },
          {
            value: "3",
            label: "第三季度",
          },
          {
            value: "4",
            label: "第四季度",
          },
        ],

        baobiao: [
          {
            value: "1",
            label: "年报",
          },
          {
            value: "2",
            label: "季报",
          },
          {
            value: "3",
            label: "月报",
          },
        ],
        groupName: "所有集团",
        factoryName: "所有电厂",
        jzName: "所有机组",
        baobiaoName: "1",
        choiceyear: "",
        jidu: "第一季度",
        months: "",
      },
      coalStatList: [],
      tableData: [],
      aa: [
        { name: "浙能", id: "sasa" },
        { name: "华电", id: "sasa" },
        { name: "国能", id: "sasa" },
        { name: "华润", id: "sasa" },
        { name: "华润", id: "sasa" },
        { name: "华润", id: "sasa" },
        { name: "华润", id: "sasa" },
        { name: "华润", id: "sasa" },
      ],
    };
  },
  mounted() {
    this.$nextTick(function () {
      this.getGroupList();
      this.getFactoryList();
      this.getJzList();
      this.getCoalStat();
      //   let timeTicket;
      //   clearInterval(timeTicket);
      //   timeTicket = window.setInterval(() => {
      //     this.getCoalStat();
      //   }, 60000);
    });
  },
  methods: {
    //获取季度子组件传回的数据
    getValue(val) {
      console.log(val);
      this.formInline.jidu = val;
    },
    fomatFloat(num, n) {
      console.log(num, n);
      var f = parseFloat(num);
      if (isNaN(f)) {
        return false;
      }
      f = Math.round(num * Math.pow(10, n)) / Math.pow(10, n); // n 幂
      var s = f.toString();
      var rs = s.indexOf(".");
      //判定如果是整数，增加小数点再补0
      if (rs < 0) {
        rs = s.length;
        s += ".";
      }
      while (s.length <= rs + n) {
        s += "0";
      }
      return s;
    },
    // 显示第几页
    handleCurrentChange(val) {
      // 改变默认的页数
      this.currentPage = val;
    },
    // 重置
    clickBtn2() {
      this.formInline.groupName = "所有集团";
      this.formInline.factoryName = "所有电厂";
      this.formInline.jzName = "所有机组";
      this.formInline.baobiaoName = "年报";
      this.formInline.choiceyear = "";
      this.formInline.jidu = "第一季度";
      this.formInline.months = "";
    },
    changeHz(val) {
      this.formInline.checked = val;
      console.log(this.formInline.checked);
      if (val) {
        this.formInline.groupName = "所有集团";
        this.formInline.factoryName = "所有电厂";
        this.formInline.jzName = "所有机组";
      }
    },
    getGroupList() {
      this.$http({
        method: "get",
        url: `/jndpportal/wbjk/getGroupList.xhtml`,
      })
        .then((res) => {
          if (res.data[0].res == "success") {
            this.formInline.groupList = res.data[0].data;
          }
        })
        .catch((err) => {
          this.$message("查询集团列表接口报错");
        });
    },
    getFactoryList(val) {
      let param = {
        groupid: this.formInline.groupName == "所有集团" ? "" : val,
      };
      this.$http({
        method: "get",
        url: `jndpportal/wbjk/getFactoryList.xhtml`,
        params: param,
      })
        .then((res) => {
          if (res.data[0].res == "success") {
            this.formInline.factoryList = res.data[0].data;
          }
        })
        .catch((err) => {
          this.$message("查询集团列表接口报错");
        });
    },
    getJzList(val) {
      let param = {
        factoryid: this.formInline.factoryName == "所有机组" ? "" : val,
      };
      this.$http({
        method: "get",
        url: `jndpportal/wbjk/getJzList.xhtml`,
        params: param,
      })
        .then((res) => {
          if (res.data[0].res == "success") {
            this.formInline.jzList = res.data[0].data;
          }
        })
        .catch((err) => {
          this.$message("查询集团列表接口报错");
        });
    },
    getCoalStat() {
      //初始化echarts
      let myChart1 = echarts.init(document.getElementById("myChart1"), "dark");
      let myChart2 = echarts.init(document.getElementById("myChart2"), "dark");
      let myChart3 = echarts.init(document.getElementById("myChart3"), "dark");
      let myChart4 = echarts.init(document.getElementById("myChart4"), "dark");
      let year = "";
      let months = "";
      let quarter = "";
      if (this.formInline.choiceyear) {
        if (this.formInline.baobiaoName == "1") {
          year = this.formInline.choiceyear.getFullYear();
        } else {
          year = "";
        }
      } else {
        year = "";
      }
      if (this.formInline.months) {
        if (this.formInline.baobiaoName == "3") {
          let yy = this.formInline.months.getFullYear();
          let mm =
            this.formInline.months.getMonth() + 1 < 10
              ? "0" + (this.formInline.months.getMonth() + 1)
              : this.formInline.months.getMonth() + 1;
          months = yy + "-" + mm;
        } else {
          months = "";
        }
      } else {
        months = "";
      }
      if (this.formInline.jidu) {
        if (this.formInline.baobiaoName == "2") {
          quarter =
            this.formInline.jidu == "第一季度" ? "" : this.formInline.jidu;
        } else {
          quarter = "";
        }
      } else {
        quarter = "";
      }

      let param = {
        allCheck: this.formInline.checked ? "1" : "0",
        groupid:
          this.formInline.groupName == "所有集团"
            ? ""
            : this.formInline.groupName,
        factoryid:
          this.formInline.factoryName == "所有电厂"
            ? ""
            : this.formInline.factoryName,
        jzbh:
          this.formInline.jzName == "所有机组" ? "" : this.formInline.jzName,
        bblx:
          this.formInline.baobiaoName == "年报"
            ? "1"
            : this.formInline.baobiaoName,
        year: year,
        quarter: quarter,
        month: months,
      };
      this.$http({
        method: "get",
        url: `jndpportal/wbjk/getCoalStat.xhtml`,
        params: param,
      })
        .then((res) => {
          if (res.data[0].res == "success") {
            this.coalStatList = res.data[0].data[0];
            this.tableData = this.coalStatList.MLZKLIST;
            let jTName = [];
            let valueNew = [];
            let valueOld = [];
            let jTName2 = [];
            let valueNew2 = [];
            let valueOld2 = [];
            let data3 = [];
            let data4 = [];
            this.coalStatList.YMLSTATLIST.map((item, index) => {
              jTName.push(item.name);
              valueNew.push(item.valueNew);
              valueOld.push(item.valueOld);
              data3.push({ value: item.valueNew, name: item.name });
            });

            this.option1 = {
              backgroundColor: "", //设置无背景色
              tooltip: {
                trigger: "axis",
                axisPointer: {
                  type: "shadow",
                },
              },
              legend: {
                data: ["去年", "当年"],
                x: "right", // 水平居右
                icon: "rect", // 图例icon为方块
                itemHeight: 10, // 图例icon高度
                itemWidth: 10, // 图例icon宽度
                textStyle: {
                  color: "#fff", // 图例文字颜色
                },
              },
              grid: {
                left: "3%",
                right: "4%",
                bottom: "3%",
                containLabel: true,
              },
              xAxis: [
                {
                  type: "category",
                  data: jTName,
                  offset: 6,
                  axisLine: {
                    show: false,
                    lineStyle: {
                      color: "rgb(31,43,58)", //刻度线的颜色
                    },
                  },
                  axisTick: {
                    show: false, // 刻度线
                  },
                  axisLabel: {
                    show: true,
                    interval: 0,
                    // rotate: 20,
                    textStyle: {
                      color: "#999",
                      fontStyle: "normal",
                      fontFamily: "微软雅黑",
                      fontSize: 13,
                      margin: 10,
                    },
                  },
                },
              ],
              yAxis: [
                {
                  type: "value",
                  axisLine: {
                    show: true, // 轴线
                    lineStyle: {
                      color: "rgb(52,61,74)", //刻度线的颜色
                    },
                  },
                  splitLine: {
                    show: true,
                    lineStyle: {
                      color: "rgb(31,43,58)", //刻度线的颜色
                    },
                  },
                  axisTick: {
                    show: false, // 刻度线
                  },
                  axisLabel: {
                    color: "#999", // y轴字颜色
                  },
                },
              ],
              series: [
                {
                  name: "去年",
                  type: "bar",
                  barWidth: 20,
                  label: {
                    show: false,
                    position: "top",
                    textStyle: {
                      fontSize: 14,
                      color: "#fff",
                      fontFamily: "FusiBold",
                    },
                  },
                  itemStyle: {
                    normal: {
                      color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [
                        { offset: 1, color: "#52D898 " },
                        { offset: 0, color: "#00B455" },
                      ]),
                    },
                  },
                  data: valueOld,
                },
                {
                  name: "当年",
                  type: "bar",
                  barWidth: 20,
                  label: {
                    show: false,
                    position: "top",
                    textStyle: {
                      fontSize: 14,
                      color: "#fff",
                      fontFamily: "FusiBold",
                    },
                  },
                  itemStyle: {
                    normal: {
                      color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [
                        { offset: 1, color: "#52D2D8 " },
                        { offset: 0, color: "#1F8AAC" },
                      ]),
                    },
                  },
                  data: valueNew,
                },
                {
                  name: "去年",
                  type: "pictorialBar",
                  barWidth: 20,
                  symbol: "diamond",
                  symbolPosition: "start",
                  symbolOffset: ["-65%", "50%"],
                  symbolSize: [20, 10],
                  zlevel: 2,
                  itemStyle: {
                    normal: {
                      color: "#26FF9D",
                      barBorderRadius: 0,
                    },
                  },
                  data: [2, 2, 2, 2, 2, 2, 2],
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: "去年",
                  type: "pictorialBar",
                  barWidth: 20,
                  symbol: "diamond",
                  symbolOffset: ["-65%", "-50%"],
                  symbolPosition: "end",
                  symbolSize: [20, 10],
                  zlevel: 2,
                  itemStyle: {
                    normal: {
                      color: "#26FF9D",
                      barBorderRadius: 0,
                    },
                  },
                  data: valueOld,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: "当年",
                  type: "pictorialBar",
                  barWidth: 20,
                  symbol: "diamond",
                  symbolPosition: "start",
                  symbolOffset: ["65%", "50%"],
                  symbolSize: [20, 10],
                  zlevel: 2,
                  itemStyle: {
                    normal: {
                      color: "#00F6FF",
                      barBorderRadius: 0,
                    },
                  },
                  data: [2, 2, 2, 2, 2, 2, 2],
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: "当年",
                  type: "pictorialBar",
                  barWidth: 20,
                  symbol: "diamond",
                  symbolOffset: ["65%", "-50%"],
                  symbolPosition: "end",
                  symbolSize: [20, 10],
                  zlevel: 2,
                  itemStyle: {
                    normal: {
                      color: "#00F6FF",
                      barBorderRadius: 0,
                    },
                  },
                  data: valueNew,
                  tooltip: {
                    show: false,
                  },
                },
              ],
            };

            this.coalStatList.JDFDLSTATLIST.map((item, index) => {
              jTName2.push(item.name);
              valueNew2.push(item.valueNew);
              valueOld2.push(item.valueOld);
              data4.push({ value: item.valueNew, name: item.name });
            });

            this.option2 = {
              backgroundColor: "", //设置无背景色

              tooltip: {
                trigger: "axis",
                axisPointer: {
                  type: "shadow",
                },
              },
              color: ["rgb(105,227,212)", "rgb(208,247,85)"],
              legend: {
                data: ["去年", "当年"],

                x: "right", // 水平居右
                icon: "rect", // 图例icon为方块
                itemHeight: 10, // 图例icon高度
                itemWidth: 10, // 图例icon宽度
                textStyle: {
                  color: "#fff", // 图例文字颜色
                },
              },
              toolbox: {
                feature: {
                  dataZoom: {
                    show: false,
                  },
                  restore: { show: false },
                  saveAsImage: { show: false },
                },
              },
              grid: {
                left: "3%",
                right: "4%",
                bottom: "3%",
                containLabel: true,
              },
              xAxis: [
                {
                  type: "category",
                  boundaryGap: ["0.1", "0.1"],
                  axisLabel: {
                    color: "#fff", // x轴字颜色
                    show: true,
                    // fontSize: 11,
                  },
                  splitLine: { show: false },
                  axisTick: {
                    show: false, // 刻度线
                  },
                  axisLine: {
                    show: false,
                    lineStyle: {
                      color: "rgb(31,43,58)", //刻度线的颜色
                    },
                  },
                  data: jTName2,
                },
              ],
              yAxis: {
                type: "value",
                boundaryGap: [0, "100%"],
                axisLine: {
                  show: true, // 轴线
                  lineStyle: {
                    color: "rgb(52,61,74)", //刻度线的颜色
                  },
                },
                splitLine: {
                  show: true,
                  lineStyle: {
                    color: "rgb(31,43,58)", //刻度线的颜色
                  },
                },
                axisTick: {
                  show: false, // 刻度线
                },
                axisLabel: {
                  color: "#999", // y轴字颜色
                  // fontSize: 11,
                },
              },
              series: [
                {
                  name: "去年",
                  type: "line",
                  stack: "Total",
                  lineStyle: {
                    color: "rgb(105,227,212)",
                    width: 3,
                  },
                  label: {
                    show: false,
                    position: "bottom",
                    textStyle: {
                      fontSize: 14,
                      color: "#fff",
                      fontFamily: "FusiBold",
                    },
                  },
                  areaStyle: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                      {
                        offset: 0,
                        color: "rgb(33,68,92)",
                        opacity: 0.1,
                      },
                      {
                        offset: 1,
                        color: "rgb(27,40,56)",
                        opacity: 0.1,
                      },
                    ]),
                  },
                  emphasis: {
                    focus: "series",
                  },
                  data: valueOld2,
                },
                {
                  name: "当年",
                  type: "line",
                  stack: "Total",
                  lineStyle: {
                    color: "rgb(208,247,85)",
                    width: 3,
                  },
                  label: {
                    show: false,
                    textStyle: {
                      fontSize: 14,
                      color: "#fff",
                      fontFamily: "FusiBold",
                    },
                    position: "top",
                  },
                  areaStyle: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                      {
                        offset: 0,
                        color: "rgb(46,96,77)",
                        opacity: 0,
                      },
                      {
                        offset: 1,
                        color: "rgb(27,40,56)",
                        opacity: 0,
                      },
                    ]),
                  },
                  emphasis: {
                    focus: "series",
                  },
                  data: valueNew2,
                },
              ],
            };
            let name1 = data3.slice(0, data3.length / 2);
            let name2 = data3.slice(data3.length / 2, data3.length);

            this.option3 = {
              backgroundColor: "", //设置无背景色
              tooltip: {
                show: false,
              },
              legend: [
                {
                  x: "right", // 水平居右
                  icon: "rect", // 图例icon为方块
                  orient: "vertical",
                  x: 500, //水平位置
                  y: 40, //竖直位置
                  itemHeight: 10, // 图例icon高度
                  itemWidth: 10, // 图例icon宽度
                  itemGap: 40,
                  textStyle: {
                    color: "#fff", // 图例文字颜色
                  },
                  data:name1,
                  formatter: function (name) {
                    var data = name1;
                    var total = 0;
                    var tarValue;
                    for (var i = 0, l = data.length; i < l; i++) {
                      total += data[i].value * 1;
                      if (data[i].name == name) {
                        tarValue = data[i].value;
                      }
                    }
                    var p = ((tarValue / total) * 100).toFixed(2);
                    return name + " " + " " + p + "%";
                  },
                },
                {
                  x: "right", // 水平居右
                  icon: "rect", // 图例icon为方块
                  orient: "vertical",
                  x: 650, //水平位置
                  y: 40, //竖直位置
                  itemHeight: 10, // 图例icon高度
                  itemWidth: 10, // 图例icon宽度
                  itemGap: 40,
                  textStyle: {
                    color: "#fff", // 图例文字颜色
                  },
                  data:name2,
                  formatter: function (name) {
                    var data = name2;
                    var total = 0;
                    var tarValue;
                    for (var i = 0, l = data.length; i < l; i++) {
                      total += data[i].value * 1;
                      if (data[i].name == name) {
                        tarValue = data[i].value;
                      }
                    }
                    var p = ((tarValue / total) * 100).toFixed(2);
                    return name + " " + " " + p + "%";
                  },
                },
              ],
              series: [
                {
                  name: "Access From",
                  type: "pie",
                  radius: ["40%", "60%"],
                  center: ["36%", "50%"],
                  data: data3,
                  itemStyle: {
                    normal: {
                      //这里是重点
                      color: function (params) {
                        var colorList = [
                          "#00f0ff",
                          "#00c5ff",
                          "#3c85f3",
                          "#0059ff",
                          "#472afa",
                          "#7262fd",
                          "#8b14e7",
                          "#be46f8",
                        ];
                        return colorList[params.dataIndex % colorList.length];
                      },
                    },
                  },
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
            let name3 = data3.slice(0, data3.length / 2);
            let name4 = data3.slice(data3.length / 2, data3.length);
            this.option4 = {
              backgroundColor: "", //设置无背景色
              tooltip: {
                trigger: "item",
              },
              legend: [
                {
                  x: "right", // 水平居右
                  icon: "rect", // 图例icon为方块
                  orient: "vertical",
                  x: 500, //水平位置
                  y: 40, //竖直位置
                  itemHeight: 10, // 图例icon高度
                  itemWidth: 10, // 图例icon宽度
                  itemGap: 40,
                  textStyle: {
                    color: "#fff", // 图例文字颜色
                  },
                  data:name3,
                  formatter: function (name) {
                    var data = name3;
                    var total = 0;
                    var tarValue;
                    for (var i = 0, l = data.length; i < l; i++) {
                      total += data[i].value * 1;
                      if (data[i].name == name) {
                        tarValue = data[i].value;
                      }
                    }
                    var p = ((tarValue / total) * 100).toFixed(2);
                    return name + " " + " " + p + "%";
                  },
                },
                {
                  x: "right", // 水平居右
                  icon: "rect", // 图例icon为方块
                  orient: "vertical",
                  x: 650, //水平位置
                  y: 40, //竖直位置
                  itemHeight: 10, // 图例icon高度
                  itemWidth: 10, // 图例icon宽度
                  itemGap: 40,
                  textStyle: {
                    color: "#fff", // 图例文字颜色
                  },
                  data:name4,
                  formatter: function (name) {
                    var data = name4;
                    var total = 0;
                    var tarValue;
                    for (var i = 0, l = data.length; i < l; i++) {
                      total += data[i].value * 1;
                      if (data[i].name == name) {
                        tarValue = data[i].value;
                      }
                    }
                    var p = ((tarValue / total) * 100).toFixed(2);
                    return name + " " + " " + p + "%";
                  },
                },
              ],
              series: [
                {
                  name: "Access From",
                  type: "pie",
                  radius: ["40%", "60%"],
                  center: ["36%", "50%"],
                  itemStyle: {
                    normal: {
                      //这里是重点
                      color: function (params) {
                        var colorList = [
                          "#00f0ff",
                          "#00c5ff",
                          "#3c85f3",
                          "#0059ff",
                          "#472afa",
                          "#7262fd",
                          "#8b14e7",
                          "#be46f8",
                        ];
                        return colorList[params.dataIndex % colorList.length];
                      },
                    },
                  },
                  data: data4,
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                  },
                },
              ],
            };
            myChart1.setOption(this.option1);
            myChart2.setOption(this.option2);
            myChart3.setOption(this.option3);
            myChart4.setOption(this.option4);
          }
        })
        .catch((err) => {
          this.$message("查询统计接口报错");
        });
    },
  },
};
</script>
<style scoped lang='less'>
@import url("./psgeTwo.less");
</style>