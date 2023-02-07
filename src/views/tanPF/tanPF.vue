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

          <div class="btn1" @click="getTpfStat">
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
          <div class="titleaa">{{ TITLE1 }}</div>
          <div id="myChart1"></div>
        </div>
        <div class="top2">
          <div class="titleaa">{{ TITLE2 }}</div>
          <div id="myChart2"></div>
        </div>
      </div>
      <div class="footer-right">
        <div class="table">
          <div class="titleaa">{{ TABLETITLE }}</div>
          <div class="tabel-body">
            <el-table
              :data="
                tableData.slice(
                  (currentPage - 1) * pageSize,
                  currentPage * pageSize
                )
              "
              style="width: 100%"
            >
              <el-table-column
                label="序号"
                width="70"
                prop="num"
                align="center"
              >
              </el-table-column>
              <el-table-column label="集团名称" width="172px" align="center">
                <template slot-scope="scope">
                  <div
                    style="
                      width: 172px;
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
              <el-table-column prop="fh" label="实时负荷(MW)" align="center">
              </el-table-column>
              <el-table-column prop="tpf" label="碳排放量(t/h)" align="center">
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
export default {
  data() {
    return {
      TITLE1: "",
      TITLE2: "",
      TABLETITLE: "",
      tableData: [],
      // 默认显示第几页
      currentPage: 1,
      // 总条数，根据接口获取数据长度(注意：这里不能为空)
      totalCount: 1,
      // 个数选择器（可修改）
      pageSize: 10,
      formInline: {
        groupName: "所有集团",
        factoryName: "所有电厂",
        jzName: "所有机组",
        groupList: [],
        factoryList: [],
        jzList: [],
      },
    };
  },
  mounted() {
    this.$nextTick(function () {
      this.getGroupList();
      this.getFactoryList();
      this.getJzList();
      this.getTpfStat();
      this.getCoalStat();
    });
  },
  methods: {
    // 显示第几页
    handleCurrentChange(val) {
      // 改变默认的页数
      this.currentPage = val;
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
      //   this.formInline.checked =
      //     this.formInline.factoryName == "所有电厂" ? true : false;
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
    clickBtn2() {
      this.formInline.groupName = "所有集团";
      this.formInline.factoryName = "所有电厂";
      this.formInline.jzName = "所有机组";
    },
    getCoalStat() {
      var myChart1 = echarts.init(document.getElementById("myChart1"), {
        devicePixelRatio: 2.5,
      });
      let date8 = [];
      let aaa = [];
      let noxpflname = [];
      let jituanName = [];
      this.$http({
        method: "get",
        url: "/jndpportal/wbjk/getStatRight.xhtml",
      }).then((res) => {
        if (res.data[0].res) {
          let resultRight = res.data[0].data[0];
          resultRight.JTPFLIST.map((item, index) => {
            if (item.JTMC == "浙能") {
              date8.push(item.dates);
            }
            date8.map((item1, index) => {
              if (item1 == item.dates) {
                noxpflname.push(item.JTMC);
              }
            });
            // 集团名字
            jituanName = noxpflname.filter(function (item2, index2) {
              return noxpflname.indexOf(item2) === index2; // 因为indexOf 只能查找到第一个
            });
          });

          Object.values(resultRight.TPFDATA[0]).map((item, index) => {
            aaa.push({
              name: Object.keys(resultRight.TPFDATA[0])[index],
              data: item,
            });
          });
          // tooltip
          const dataArr = {
            xdata: date8,
            result: aaa,
          };
          const tooltip = { trigger: "axis" };

          // legend
          const legend = {
            data: dataArr.result.map((item) => item.name),
            textStyle: { color: "#fff" },
            x: "right", // 水平居右
            itemHeight: 20, // 图例icon高度
            itemWidth: 20, // 图例icon宽度
            // itemGap: 2,
            top: "3%",
            // 禁止点击
            selectedMode: false,
          };
          // grid
          const grid = {
            left: "4%",
            right: "3%",
            bottom: "10%",
            containLabel: true,
          };

          // xAxis
          const xAxis = {
            axisTick: { show: false },
            axisLine: { show: false },
            axisLabel: {
              textStyle: {
                color: "#fff",
              },
            },
            data: dataArr.xdata,
          };

          // yAxis
          const yAxis = [
            {
              splitLine: { lineStyle: { color: "rgba(255,255,255, .05)" } },
              axisLine: { show: false },
              axisLabel: { textStyle: { color: "#999" } },
            },
          ];

          // 循环生成每个头部菱形
          const diamondData = dataArr.result.reduce((pre, cur, index) => {
            pre[index] = cur.data.map(
              (el, id) => el + (pre[index - 1] ? pre[index - 1][id] : 0)
            );
            return pre;
          }, []);

          // 定义好颜色 color
          const color = [
            [
              { offset: 0, color: "#9EEEA6" },
              { offset: 0.5, color: "#9EEEA6" },
              { offset: 0.5, color: "#80F396 " },
              { offset: 1, color: "#80F396 " },
            ],
            [
              { offset: 0, color: "#7DBCF9" },
              { offset: 0.5, color: "#7DBCF9" },
              { offset: 0.5, color: "#6C92FF" },
              { offset: 1, color: "#6C92FF" },
            ],
            [
              { offset: 0, color: "#42DADD" },
              { offset: 0.5, color: "#42DADD" },
              { offset: 0.5, color: "#19C7D0" },
              { offset: 1, color: "#19C7D0" },
            ],
            [
              { offset: 0, color: "#EB9BE4" },
              { offset: 0.5, color: "#EB9BE4" },
              { offset: 0.5, color: "#B87BFC" },
              { offset: 1, color: "#B87BFC" },
            ],
            [
              { offset: 0, color: "#E2A467" },
              { offset: 0.5, color: "#E2A467" },
              { offset: 0.5, color: "#E2A467" },
              { offset: 1, color: "#E2A467" },
            ],
            [
              { offset: 0, color: "#B87BFC" },
              { offset: 0.5, color: "#B87BFC" },
              { offset: 0.5, color: "#482CFB" },
              { offset: 1, color: "#482CFB" },
            ],

            [
              { offset: 0, color: "#2636E6" },
              { offset: 0.5, color: "#2636E6" },
              { offset: 0.5, color: "#3A45FB" },
              { offset: 1, color: "#3A45FB" },
            ],

            [
              { offset: 0, color: "#ADFC7B" },
              { offset: 0.5, color: "#ADFC7B" },
              { offset: 0.5, color: "#EBE754" },
              { offset: 1, color: "#EBE754" },
            ],
          ];

          // 循环生成series配置
          let series = dataArr.result.reduce((p, c, i, array) => {
            p.push(
              {
                z: i + 1,
                stack: "总量",
                type: "bar",
                name: c.name,
                barGap: "-100%",
                barWidth: 30,
                data: c.data,
                itemStyle: {
                  color: {
                    type: "linear",
                    x: 0,
                    x2: 1,
                    y: 0,
                    y2: 0,
                    colorStops: color[i],
                  },
                },
              },
              {
                z: i + 10,
                type: "pictorialBar",
                symbolPosition: "end",
                symbol: "diamond",
                symbolOffset: [0, "-50%"],
                symbolSize: [30, 10],
                data: diamondData[i],
                itemStyle: {
                  color: {
                    type: "linear",
                    x: 0,
                    x2: 1,
                    y: 0,
                    y2: 0,
                    colorStops: color[i],
                  },
                },
                tooltip: { show: false },
              }
            );

            return p;
          }, []);
          const option1 = {
            tooltip,
            xAxis,
            yAxis,
            series,
            grid,
            legend,
            backgroundColor: "",
          };
          myChart1.setOption(option1);
        }
      });
    },
    getTpfStat() {
      this.tableData = [];
      let myChart2 = echarts.init(document.getElementById("myChart2"));
      let num = [];
      let xxData = [];
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
        url: `jndpportal/wbjk/getTpfStat.xhtml`,
        params: param,
      })
        .then((res) => {
          let result = res.data[0].data[0];
          this.TITLE1 = result.TITLE1;
          this.TITLE2 = result.TITLE2;
          this.TABLETITLE = result.TABLETITLE;

          this.tableData = result.TPFList;
          result.TPFREALTIMELIST.map((item, index) => {
            num.push(item.value);
            xxData.push(item.name);
          });

          var colors = [
            {
              type: "linear",
              x: 0,
              x2: 1,
              y: 0,
              y2: 0,
              colorStops: [
                { offset: 0, color: "rgb(107,190,197)" },
                { offset: 0.5, color: "rgb(107,190,197)" },
                { offset: 0.5, color: "rgb(60,126,157)" },
                { offset: 1, color: "rgb(60,126,157)" },
              ],
            },
            {
              type: "linear",
              x: 0,
              x2: 1,
              y: 0,
              y2: 0,
              colorStops: [
                { offset: 0, color: "rgb(107,190,197)" },
                { offset: 0.5, color: "rgb(107,190,197)" },
                { offset: 0.5, color: "rgb(60,126,157)" },
                { offset: 1, color: "rgb(60,126,157)" },
              ],
            },
          ];

          this.option2 = {
            title: {
              // text: "锅炉热效率",
              textStyle: {
                //主标题的属性
                color: "#fff", //颜色
                fontSize: 14, //大小
                fontWeight: 400,
                fontFamily: "PingFangSC-Regular",
              },
            },
            series: [
              {
                name: "实时碳排放",
                type: "bar",
                barGap: "14%",
                barWidth: 30,
                label: {
                  normal: {
                    show: true,
                    position: "top",
                    textStyle: {
                      fontSize: 14,
                      color: "#72F4FA",
                      fontWeight: 700,
                      fontFamily: "FusiBold",
                      lineHeight: 25,
                    },
                  },
                },
                itemStyle: {
                  normal: {
                    color: colors[1],
                    barBorderRadius: 0,
                  },
                },
                data: num,
              },
              {
                z: 2,
                name: "2020",
                type: "pictorialBar",
                symbol: "diamond",
                symbolOffset: ["0%", "50%"],
                symbolSize: [30, 10],
                itemStyle: {
                  normal: {
                    color: colors[1],
                  },
                },
              },
              {
                // 3d顶部
                z: 3,
                name: "2020",
                type: "pictorialBar",
                symbolPosition: "end",
                data: num,
                symbol: "diamond",
                symbolOffset: ["0%", "-50%"],
                symbolSize: [30, (10 * (30 - 1)) / 30],
                itemStyle: {
                  normal: {
                    color: "rgb(91,201,212)",
                  },
                },
              },
            ],
            tooltip: {
              trigger: "axis",
              axisPointer: {
                // 坐标轴指示器，坐标轴触发有效
                type: "shadow", // 默认为直线，可选为：'line' | 'shadow'
              },
              formatter: function (params) {
                var tipString = params[0].axisValue + "<br />";
                var key = "value";
                params.sort(function (obj1, obj2) {
                  var val1 = obj1[key];
                  var val2 = obj2[key];
                  if (val1 < val2) {
                    return 1;
                  } else if (val1 > val2) {
                    return -1;
                  } else {
                    return 0;
                  }
                });
                var indexColor;
                for (var i = 0, length = params.length; i < length; i++) {
                  if (params[i].componentSubType == "bar") {
                    indexColor = params[i + 1].color;
                    tipString +=
                      '<span style="display:inline-block;margin-right:5px;border-radius:10px;width:9px;height:9px;background:' +
                      indexColor +
                      '"></span>';
                    tipString +=
                      '<span data-type ="lineTip" data-val=' +
                      params[i].value +
                      ">" +
                      params[i].seriesName +
                      "：" +
                      params[i].value +
                      "</span><br />";
                  }
                }
                return tipString;
              },
            },
            grid: {
              left: "3%",
              right: "3%",
              bottom: "6%",
              top: "20%",
              containLabel: true,
            },
            xAxis: {
              type: "category",
              data: xxData,
              offset: 6,
              axisLine: { show: false, lineStyle: { color: " #CCCCCC" } },
              axisTick: {
                alignWithLabel: true,
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

            yAxis: {
              type: "value",
              //   name: "(%)",
              nameTextStyle: {
                align: "right",
                color: "#999",
                // fontSize: 11,
              },
              axisLine: {
                show: false,
                lineStyle: { color: "#666" },
              },
              axisTick: { show: false },
              splitLine: {
                show: true,
                lineStyle: { type: "dashed", color: "#666" },
              },
              axisLabel: {
                textStyle: {
                  color: "#999",
                  fontSize: 14,
                },
              },
            },
          };
          myChart2.setOption(this.option2);
        })
        .catch((err) => {
          this.$message("查询测点展示接口报错");
        });
    },
  },
};
</script>
<style scoped lang='less'>
@import url("./tanPF.less");
</style>