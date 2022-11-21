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
              <el-option
                v-if="formInline.factoryList.length > 1"
                label="所有电厂"
                value="所有电厂"
              ></el-option>
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
              <el-option
                v-if="formInline.jzList.length > 1"
                label="所有机组"
                value="所有机组"
              ></el-option>
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
          <span v-if="formInline.baobiaoName == '2'"> 季度： </span>
          <span v-if="formInline.baobiaoName == '3'"> 月份： </span>

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
        <div class="top1">
          <div class="titleaa">机组运行时间</div>
          <div id="myChart1"></div>
        </div>
        <div class="top2">
          <div class="titleaa">氮氧化物排放量</div>
          <div id="myChart2"></div>
        </div>
        <div class="top3">
          <div class="titleaa">二氧化硫排放量</div>
          <div id="myChart3"></div>
        </div>
        <div class="top4">
          <div class="titleaa">烟尘排放量</div>
          <div id="myChart4"></div>
        </div>
      </div>
      <div class="footer-right">
        <div class="table">
          <div class="titleaa">污染排放</div>
          <div class="tabel-body">
            <el-table
              :data="
                tableData.slice(
                  (currentPage - 1) * pageSize,
                  currentPage * pageSize
                )
              "
              max-height="680"
              style="width: 100%"
            >
              <el-table-column
                label="序号"
                width="53"
                prop="num"
                align="center"
              >
              </el-table-column>
              <el-table-column prop="dates" label="时间" align="center">
              </el-table-column>
              <el-table-column label="集团" width="120px" align="center">
                <template slot-scope="scope">
                  <div
                    style="
                      width: 110px;
                      height: 26px;
                      text-align: center;
                      background: rgb(16, 42, 64);
                      border-radius: 4.4px;
                    "
                  >
                    {{ scope.row.groupName }}
                  </div>
                </template>
              </el-table-column>
              <el-table-column
                prop="factoryName"
                label="电厂名称"
                align="center"
              >
              </el-table-column>
              <el-table-column
                prop="crewName"
                width="100"
                label="机组名称"
                align="center"
              >
              </el-table-column>
              <el-table-column prop="fdl" label="发电量" align="center">
              </el-table-column>
              <el-table-column prop="runTime" label="运行时间" align="center">
              </el-table-column>
              <el-table-column
                prop="noxPfl"
                label="氮氧化物排放量"
                align="center"
              >
              </el-table-column>
              <el-table-column
                prop="so2Pfl"
                label="二氧化硫排放量"
                align="center"
              >
              </el-table-column>
              <el-table-column prop="dustPfl" label="烟尘排放量" align="center">
              </el-table-column>
              <el-table-column label="氮氧化物浓度" align="center">
                <el-table-column
                  prop="noxNd"
                  label="浓度(mg/m3)"
                  align="center"
                >
                </el-table-column>
                <el-table-column
                  prop="noxCb1byn"
                  label="1倍以内超标时间(小时)"
                  align="center"
                >
                </el-table-column>
                <el-table-column
                  prop="noxCb1bys"
                  label="1倍以上超标时间(小时)"
                  align="center"
                >
                </el-table-column>
              </el-table-column>

              <el-table-column label="二氧化硫浓度" align="center">
                <el-table-column
                  prop="so2Nd"
                  label="浓度(mg/m3)"
                  align="center"
                >
                </el-table-column>
                <el-table-column
                  prop="so2Cb1byn"
                  label="1倍以内超标时间(小时)"
                  align="center"
                >
                </el-table-column>
                <el-table-column
                  prop="so2Cb1bys"
                  label="二氧化硫超标一倍以上"
                  align="center"
                >
                </el-table-column>
              </el-table-column>

              <el-table-column label="烟尘浓度" align="center">
                <el-table-column
                  prop="dustNd"
                  label="浓度(mg/m3)"
                  align="center"
                >
                </el-table-column>
                <el-table-column
                  prop="dustCb1byn"
                  label="1倍以内超标时间(小时)"
                  align="center"
                >
                </el-table-column>
                <el-table-column
                  prop="dustCb1bys"
                  label="1倍以上超标时间(小时)"
                  align="center"
                >
                </el-table-column>
              </el-table-column>
            </el-table>
            <el-pagination
              style="float: right; margin-top: 10px"
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
      titleTime: "2022年",
      // 默认显示第几页
      currentPage: 1,
      // 总条数，根据接口获取数据长度(注意：这里不能为空)
      totalCount: 1,
      // 个数选择器（可修改）
      pageSize: 8,
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
        this.factoryList = [];
        this.formInline.jzName = "所有机组";
        this.formInline.jzList = [];
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
      this.formInline.checked =
        this.formInline.groupName == "所有集团" ? true : false;
      this.formInline.factoryName = "所有电厂";
      this.factoryList = [];
      this.formInline.jzName = "所有机组";
      this.formInline.jzList = [];

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
            if (this.formInline.factoryList.length == 1) {
              this.formInline.factoryName = this.formInline.factoryList[0].id;
            }
          }
        })
        .catch((err) => {
          this.$message("查询集团列表接口报错");
        });
    },
    getJzList(val) {
      if (this.formInline.factoryName == "所有电厂") {
        if (this.formInline.groupName == "所有集团") {
          this.formInline.checked = true;
        }
      }
      // this.formInline.checked = this.formInline.factoryName == "所有电厂" ? true:false
      this.formInline.jzName = "所有机组";
      this.formInline.jzList = [];
      let param = {
        factoryid: this.formInline.factoryName == "所有电厂" ? "" : val,
      };
      this.$http({
        method: "get",
        url: `jndpportal/wbjk/getJzList.xhtml`,
        params: param,
      })
        .then((res) => {
          if (res.data[0].res == "success") {
            this.formInline.jzList = res.data[0].data;
            if (this.formInline.jzList.length == 1) {
              this.formInline.jzName = this.formInline.jzList[0].id;
            }
          }
        })
        .catch((err) => {
          this.$message("查询集团列表接口报错");
        });
    },
    getCoalStat() {
      this.currentPage = 1;
      this.tableData = [];

      //初始化echarts
      let myChart1 = echarts.init(document.getElementById("myChart1"), "dark", {
        devicePixelRatio: 2.5,
      });
      let myChart2 = echarts.init(document.getElementById("myChart2"), "dark", {
        devicePixelRatio: 2.5,
      });
      let myChart3 = echarts.init(document.getElementById("myChart3"), "dark", {
        devicePixelRatio: 2.5,
      });
      let myChart4 = echarts.init(document.getElementById("myChart4"), "dark", {
        devicePixelRatio: 2.5,
      });
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
        url: `jndpportal/wbjk/getHbzkStat.xhtml`,
        params: param,
      })
        .then((res) => {
          if (res.data[0].res == "success") {
            this.coalStatList = res.data[0].data[0];
            // 右侧表格数据
            this.tableData = this.coalStatList.HBZKLIST;

            this.titleTime = this.coalStatList.TITLETIME;
            let qiannian = this.coalStatList.LASTYEARTAG.toString();
            let dangnian = this.coalStatList.YEARTAG.toString();
            let dibu = [];
            let jTName = [];
            let valueNew = [];
            let valueOld = [];
            let dibu2 = [];
            let jTName2 = [];
            let valueNew2 = [];
            let valueOld2 = [];
            let dibu3 = [];
            let jTName3 = [];
            let valueNew3 = [];
            let valueOld3 = [];
            let dibu4 = [];
            let jTName4 = [];
            let valueNew4 = [];
            let valueOld4 = [];
            let legendDate = [];
            legendDate.push(qiannian, dangnian);
            // 表1数据
            this.coalStatList.RUNTIMELIST.map((item, index) => {
              jTName.push(item.name);
              valueNew.push(item.valueNew);
              valueOld.push(item.valueOld);
              dibu.push(2);
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
                data: legendDate,
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
                top: "10%",
                bottom: "20%",
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
                    textStyle: {
                      color: "#999",
                      fontStyle: "normal",
                      fontFamily: "微软雅黑",
                      fontSize: 11,
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
                  name: legendDate[0],
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
                  name: legendDate[1],
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
                  name: legendDate[0],
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
                  data: dibu,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: legendDate[0],
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
                  name: legendDate[1],
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
                  data: dibu,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: legendDate[1],
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

            this.coalStatList.NOXLIST.map((item, index) => {
              jTName2.push(item.name);
              valueNew2.push(item.valueNew);
              valueOld2.push(item.valueOld);
              dibu2.push(2);
            });
            this.option2 = {
              backgroundColor: "", //设置无背景色
              tooltip: {
                trigger: "axis",
                axisPointer: {
                  type: "shadow",
                },
              },
              legend: {
                data: legendDate,
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
                top: "10%",
                bottom: "20%",
                containLabel: true,
              },
              xAxis: [
                {
                  type: "category",
                  data: jTName2,
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
                    textStyle: {
                      color: "#999",
                      fontStyle: "normal",
                      fontFamily: "微软雅黑",
                      fontSize: 11,
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
                  name: legendDate[0],
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
                  data: valueOld2,
                },
                {
                  name: legendDate[1],
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
                  data: valueNew2,
                },
                {
                  name: legendDate[0], //底部
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
                  data: dibu2,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: legendDate[0],
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
                  data: valueOld2,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: legendDate[1],
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
                  data: dibu2,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: legendDate[1],
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
                  data: valueNew2,
                  tooltip: {
                    show: false,
                  },
                },
              ],
            };

            this.coalStatList.SO2LIST.map((item, index) => {
              jTName3.push(item.name);
              valueNew3.push(item.valueNew);
              valueOld3.push(item.valueOld);
              dibu3.push(2);
            });

            this.option3 = {
              backgroundColor: "", //设置无背景色
              tooltip: {
                trigger: "axis",
                axisPointer: {
                  type: "shadow",
                },
              },
              legend: {
                data: legendDate,
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
                top: "10%",
                bottom: "20%",
                containLabel: true,
              },
              xAxis: [
                {
                  type: "category",
                  data: jTName3,
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
                    textStyle: {
                      color: "#999",
                      fontStyle: "normal",
                      fontFamily: "微软雅黑",
                      fontSize: 11,
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
                  name: legendDate[0],
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
                  data: valueOld3,
                },
                {
                  name: legendDate[1],
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
                  data: valueNew3,
                },
                {
                  name: legendDate[0], //底部
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
                  data: dibu3,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: legendDate[0],
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
                  data: valueOld3,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: legendDate[1],
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
                  data: dibu3,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: legendDate[1],
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
                  data: valueNew3,
                  tooltip: {
                    show: false,
                  },
                },
              ],
            };

            this.coalStatList.DUSTLIST.map((item, index) => {
              jTName4.push(item.name);
              valueNew4.push(item.valueNew);
              valueOld4.push(item.valueOld);
              dibu4.push(2);
            });

            this.option4 = {
              backgroundColor: "", //设置无背景色
              tooltip: {
                trigger: "axis",
                axisPointer: {
                  type: "shadow",
                },
              },
              legend: {
                data: legendDate,
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
                top: "10%",
                bottom: "20%",
                containLabel: true,
              },
              xAxis: [
                {
                  type: "category",
                  data: jTName4,
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
                    textStyle: {
                      color: "#999",
                      fontStyle: "normal",
                      fontFamily: "微软雅黑",
                      fontSize: 11,
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
                  name: legendDate[0],
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
                  data: valueOld4,
                },
                {
                  name: legendDate[1],
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
                  data: valueNew4,
                },
                {
                  name: legendDate[0], //底部
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
                  data: dibu4,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: legendDate[0],
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
                  data: valueOld4,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: legendDate[1],
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
                  data: dibu4,
                  tooltip: {
                    show: false,
                  },
                },
                {
                  name: legendDate[1],
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
                  data: valueNew4,
                  tooltip: {
                    show: false,
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
@import url("./pageFour.less");
</style>