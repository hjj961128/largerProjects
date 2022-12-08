<template>
  <div class="main-body">
    <div class="top-search">
      <el-form :model="formInline" class="demo-form-inline">
        <el-form-item>
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
              <el-option v-if="formInline.factoryList.length > 1" label="所有电厂" value="所有电厂"></el-option>
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
              <el-option v-if="formInline.jzList.length > 1" label="所有机组" value="所有机组"></el-option>
              <el-option
                v-for="item in formInline.jzList"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              >
              </el-option>
            </el-select>
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
      <div class="top1">
        <div class="titleaa">{{TITLE1}}</div>
        <div id="myChart1"></div>
      </div>
      <div class="top2">
        <div class="titleaa">{{TITLE2}}</div>
        <div id="myChart2"></div>
      </div>
      <div class="top3">
        <div class="titleaa">{{TITLE3}}</div>
        <div id="myChart3"></div>
      </div>
      <div class="top4">
        <div class="titleaa">{{TITLE4}}</div>
        <div id="myChart4"></div>
      </div>
      <div class="footer1">
        <div class="titleaa">{{TITLE5}}</div>
        <div class="title">{{PIETITLE1}}</div>
        <div id="myChart5"></div>
      </div>
      <div class="footer2">
        <div class="titleaa">{{TITLE6}}</div>
        <div class="title">{{ PIETITLE2 }}</div>
        <div id="myChart6"></div>
      </div>
      <div class="footer3">
        <div class="titleaa">{{TITLE7}}</div>
        <div class="title">{{ PIETITLE3 }}</div>
        <div id="myChart7"></div>
      </div>
      <div class="footer4">
        <div class="titleaa" style="margin-bottom:10px">{{TABLETITLE}}</div>
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
            <el-table-column label="序号"  prop="num" align="center">
            </el-table-column>
            <!-- <el-table-column prop="dates" label="时间" align="center">
            </el-table-column> -->
            <el-table-column label="集团名称" width="88" align="center">
              <template slot-scope="scope">
                <div
                  style="width: 80px;
                    height: 26px;
                    text-align: center;
                    line-height:26px;
                    background: rgb(16, 42, 64);border-radius: 5px;
                  "
                >
                  {{ scope.row.groupName }}
                </div>
              </template>
            </el-table-column>
            <el-table-column prop="factoryName" width="113px" label="电厂名称" align="center">
            </el-table-column>
            <el-table-column
              prop="crewName"
              width="100"
              label="机组名称"
              align="center"
            >
            </el-table-column>
            <el-table-column prop="clsx" label="出力上限" align="center">
            </el-table-column>
            <el-table-column prop="clxx" label="出力下限" align="center">
            </el-table-column>
            <el-table-column prop="sscl" label="实时出力" align="center">
            </el-table-column>
            <el-table-column prop="clsxyl" label="出力上限裕量" align="center">
            </el-table-column>
            <el-table-column prop="clxxyl" label="出力下限裕量" align="center">
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
</template>
<script>
import * as echarts from "echarts";
export default {
  data() {
    return {
      TITLE1: '',
      TITLE2: '',
      TITLE3: '',
      TITLE4: '',
      TITLE5: '',
      TITLE6: '',
      TITLE7: '',
      PIETITLE1: '',
      PIETITLE2: '',
      PIETITLE3: '',
      TABLETITLE: '',
      // 默认显示第几页
      currentPage: 1,
      // 总条数，根据接口获取数据长度(注意：这里不能为空)
      totalCount: 1,
      // 个数选择器（可修改）
      pageSize: 5,
      // 默认每页显示的条数（可修改）
      tableData: [],
      coalStatList: [], // 接口返回数据
      formInline: {
        province: "zhejiang",
        groupList: [],
        factoryList: [],
        jzList: [],
        groupName: "所有集团",
        factoryName: "所有电厂",
        jzName: "所有机组",
      },
    };
  },
  mounted() {
    this.$nextTick(function () {
      // 集团
      this.getGroupList()
      // 电厂
      this.getFactoryList();
      // 机组
      this.getJzList();
      this.getCoalStat();
    });
  },
  methods: {
    // 集团
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
    },
    getFactoryList(val) {
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
            if(this.formInline.factoryList.length == 1){
              this.formInline.factoryName = this.formInline.factoryList[0].id
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
            if(this.formInline.jzList.length == 1){
              this.formInline.jzName = this.formInline.jzList[0].id
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
      let myChart5 = echarts.init(document.getElementById("myChart5"), "dark", {
        devicePixelRatio: 2.5,
      });
      let myChart6 = echarts.init(document.getElementById("myChart6"), "dark", {
        devicePixelRatio: 2.5,
      });
      let myChart7 = echarts.init(document.getElementById("myChart7"), "dark", {
        devicePixelRatio: 2.5,
      });
      let param = {
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
      };
      this.$http({
        method: "get",
        url: `jndpportal/wbjk/getKtclStat.xhtml`,
        params: param,
      })
        .then((res) => {
          if (res.data[0].res == "success") {
            this.coalStatList = res.data[0].data[0];
            this.TITLE1 = this.coalStatList.TITLE1;
            this.TITLE2 = this.coalStatList.TITLE2;
            this.TITLE3 = this.coalStatList.TITLE3;
            this.TITLE4 = this.coalStatList.TITLE4;
            this.TITLE5 = this.coalStatList.TITLE5;
            this.TITLE6 = this.coalStatList.TITLE6;
            this.TITLE7 = this.coalStatList.TITLE7;
            this.PIETITLE1 = this.coalStatList.PIETITLE1
            this.PIETITLE2 = this.coalStatList.PIETITLE2
            this.PIETITLE3 = this.coalStatList.PIETITLE3
            this.TABLETITLE = this.coalStatList.TABLETITLE

            this.tableData = this.coalStatList.KTCLLIST;
            let qiannian = this.coalStatList.LASTYEARTAG.toString();
            let dangnian = this.coalStatList.YEARTAG.toString();
            let legendDate = [];
            legendDate.push(qiannian, dangnian);
            // let legendDate = ['2021','2022']
            // 实时出力
            let dibu = [];
            let jTName = [];
            let valueNew = [];
            let valueOld = [];
            let data4 = [];
            this.coalStatList.SSCLLIST.map((item, index) => {
              jTName.push(item.name);
              valueNew.push(item.valueNew);
              valueOld.push(item.valueOld);
              dibu.push(2);
              data4.push({ value: item.valueNew, name: item.name });
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
                bottom: "10%",
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

            let name1 = data4.slice(0, data4.length / 2);
            let name2 = data4.slice(data4.length / 2, data4.length);

            this.option5 = {
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
                  data: name1,
                  formatter: function (name) {
                    var data = name1;
                    var total = 0;
                    var tarValue;
                    for (var i = 0, l = data4.length; i < l; i++) {
                      total += data4[i].value * 1;
                      if (data4[i].name == name) {
                        tarValue = data4[i].value;
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
                  data: name2,
                  formatter: function (name) {
                    var data = name2;
                    var total = 0;
                    var tarValue;
                    for (var i = 0, l = data4.length; i < l; i++) {
                      total += data4[i].value * 1;
                      if (data4[i].name == name) {
                        tarValue = data4[i].value;
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
                  center: ["35%", "50%"],
                  data: data4,
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

            // 上限裕量 SXYLLIST
            let dibu2 = [];
            let jTName2 = [];
            let valueNew2 = [];
            let valueOld2 = [];
            let data5 = [];
            this.coalStatList.SXYLLIST.map((item, index) => {
              jTName2.push(item.name);
              valueNew2.push(item.valueNew);
              valueOld2.push(item.valueOld);
              dibu2.push(2);
              data5.push({ value: item.valueNew, name: item.name });
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
                bottom: "10%",
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

            let name3 = data5.slice(0, data5.length / 2);
            let name4 = data5.slice(data5.length / 2, data5.length);

            this.option6 = {
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
                  data: name3,
                  formatter: function (name) {
                    var data = name3;
                    var total = 0;
                    var tarValue;
                    for (var i = 0, l = data5.length; i < l; i++) {
                      total += data5[i].value * 1;
                      if (data5[i].name == name) {
                        tarValue = data5[i].value;
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
                  data: name4,
                  formatter: function (name) {
                    var data = name4;
                    var total = 0;
                    var tarValue;
                    for (var i = 0, l = data5.length; i < l; i++) {
                      total += data5[i].value * 1;
                      if (data5[i].name == name) {
                        tarValue = data5[i].value;
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
                  center: ["35%", "50%"],
                  data: data5,
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

            // 下限裕量数据列表 XXYLLIST
            let dibu3 = [];
            let jTName3 = [];
            let valueNew3 = [];
            let valueOld3 = [];
            let data7 = [];
            this.coalStatList.XXYLLIST.map((item, index) => {
              jTName3.push(item.name);
              valueNew3.push(item.valueNew);
              valueOld3.push(item.valueOld);
              dibu3.push(2);
              data7.push({ value: item.valueNew, name: item.name });
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
                bottom: "10%",
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

            let name5 = data7.slice(0, data7.length / 2);
            let name6 = data7.slice(data7.length / 2, data7.length);

            this.option7 = {
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
                  data: name5,
                  formatter: function (name) {
                    var data = name5;
                    var total = 0;
                    var tarValue;
                    for (var i = 0, l = data7.length; i < l; i++) {
                      total += data7[i].value * 1;
                      if (data7[i].name == name) {
                        tarValue = data7[i].value;
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
                  data: name6,
                  formatter: function (name) {
                    var data = name6;
                    var total = 0;
                    var tarValue;
                    for (var i = 0, l = data7.length; i < l; i++) {
                      total += data7[i].value * 1;
                      if (data7[i].name == name) {
                        tarValue = data7[i].value;
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
                  center: ["35%", "50%"],
                  data: data7,
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

            let jTName4 = [];
            let clsx4 = [];
            let clxx4 = [];
            let sscl4 = [];
            this.coalStatList.CLDBLIST.map((item, index) => {
              jTName4.push(item.name);
              clsx4.push(item.clsx);
              clxx4.push(item.clxx);
              sscl4.push(item.sscl);
            });

            this.option4 = {
              backgroundColor: "", //设置无背景色
              title: {
                left: "20px",
                textStyle: { fontSize: 15 },
              },
              color: ["#26FF9D", "#1AE36E", "#00B455"],
              tooltip: { trigger: "axis" },
              legend: {
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
                bottom: "10%",
                containLabel: true,
              },
              xAxis: {
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
              yAxis: {
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
              series: [
                {
                  name: "出力上限",
                  type: "bar",
                  barGap: "-100%",
                  barWidth: 45,
                  data: clsx4,
                  itemStyle: {
                    normal: {
                      color: "#26FF9D",
                    },
                  },
                },
                {
                  name: "实时出力",
                  barWidth: 45,
                  type: "bar",
                  data: sscl4,
                  itemStyle: {
                    normal: {
                      color: "#1AE36E",
                    },
                  },
                },
                {
                  name: "出力下限",
                  barWidth: 45,
                  type: "bar",
                  // stack: "出力",
                  data: clxx4,
                  itemStyle: {
                    normal: {
                      color: "#00B455",
                    },
                  },
                },
              ],
            };

            myChart1.setOption(this.option1);
            myChart2.setOption(this.option2);
            myChart3.setOption(this.option3);
            myChart4.setOption(this.option4);
            myChart5.setOption(this.option5);
            myChart6.setOption(this.option6);
            myChart7.setOption(this.option7);
          }
        })
        .catch((err) => {
          this.$message("出力查询接口报错");
        });
    },
  },
};
</script>
<style scoped lang='less'>
@import url("./pageThree.less");
</style>