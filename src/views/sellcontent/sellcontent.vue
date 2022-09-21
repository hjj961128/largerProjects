<template>
  <div class="mian-body">
    <div class="main-left">
      <div class="left-top">
        <div class="left-top-left">
          <div class="left-one">
            <div class="left-one-img">
              <img src="../../assets/box_1_1.png" alt="" />
              <div class="left-one-text">实时负荷</div>
            </div>
            <div class="left-text">{{ leftNum }}</div>
          </div>
          <div class="left-two">
            <div class="left-two-img">
              <img src="../../assets/box_1_2.png" alt="" />
              <div class="left-two-text">机组功率</div>
            </div>
            <div class="left-text">{{ rightNum }}</div>
          </div>
        </div>
        <div class="left-top-center">
          <div class="left-top-center-text">原煤量</div>
          <div class="cityGreenLand-charts" id="cityGreenLand-charts"></div>
        </div>
        <div class="left-top-right">
          <div id="industrialIncrease"></div>
        </div>
      </div>
      <div class="left-footer">
        <div class="left-footer-left">
          <div id="biao4"></div>
        </div>
        <div class="left-footer-center">
          <div id="biao5"></div>
        </div>
        <div class="left-footer-right">
          <div id="biao6"></div>
        </div>
      </div>
    </div>
    <!-- 中间部分 -->
    <div class="main-center">
      <div class="main-center1">12121</div>
      <div class="main-center2">7898</div>
    </div>
    <!-- 右边部分 -->
    <div class="main-right">
      <div class="main-right-left">
        <div class="main-right-left-top">
          <div class="main-right-left-text1">80</div>
          <div class="main-right-left-text2">
            80 <span class="wan">万</span>
          </div>
          <div class="main-right-left-text3">
            80 <span class="wan">万</span>
          </div>
          <div class="main-right-left-text4">
            80 <span class="wan">万</span>
          </div>
          <div class="main-right-left-text5">
            80 <span class="wan">万</span>
          </div>
          <div class="main-right-left-text6">
            80 <span class="wan">万</span>
          </div>
        </div>
        <div class="main-right-left-footer">
          <div class="footer-one" id="xindian1"></div>
          <div class="footer-two"></div>
          <div class="footer-three"></div>
          <div class="footer-four"></div>
        </div>
      </div>
      <div class="main-right-right"></div>
    </div>
  </div>
</template>
  
<script>
import * as echarts from "echarts";
import "echarts-gl";
export default {
  name: "sellcontent",
  components: {},
  data() {
    return {
      leftNum: 777777,
      rightNum: 9999,
      optionData: [
        {
          name: "巨化集团",
          value: 444,
          itemStyle: {
            color: "#22c4ff",
          },
        },
        {
          name: "台塑集团",
          value: 666,
          itemStyle: {
            color: "#f8b551",
          },
        },
        {
          name: "华润集团",
          value: 632,
          itemStyle: {
            color: "#005aff",
          },
        },
        {
          name: "华电集团",
          value: 435,
          itemStyle: {
            color: "#775afd",
          },
        },
        {
          name: "大唐集团",
          value: 412,
          itemStyle: {
            color: "#aff",
          },
        },
        {
          name: "华能集团",
          value: 411,
          itemStyle: {
            color: "#212aff",
          },
        },
        {
          name: "国能集团",
          value: 432,
          itemStyle: {
            color: "#098aff",
          },
        },
        {
          name: "浙能集团",
          value: 423,
          itemStyle: {
            color: "#657aff",
          },
        },
      ],
      statusChart: null,
      option: {},
    };
  },
  created() {},
  mounted() {
    this.$nextTick(function () {
      this.init();
      this.getOption();
      this.getOption4();
      this.getOption5();
      this.getOption6();
      this.getOption7();
    });
  },
  methods: {
    init() {
      //构建3d饼状图
      let myChart = echarts.init(
        document.getElementById("cityGreenLand-charts")
      );
      // 传入数据生成 option
      this.option = this.getPie3D(this.optionData, 0.8);
      myChart.setOption(this.option);
      //是否需要label指引线，如果要就添加一个透明的2d饼状图并调整角度使得labelLine和3d的饼状图对齐，并再次setOption
      this.option.series.push({
        name: "pie2d",
        type: "pie",
        labelLine: {
          length: 20,
          length2: 20,
        },
        startAngle: -55, //起始角度，支持范围[0, 360]。
        clockwise: false, //饼图的扇区是否是顺时针排布。上述这两项配置主要是为了对齐3d的样式
        radius: ["50%", "40%"],
        center: ["50%", "50%"],
        data: this.optionData,
        itemStyle: {
          opacity: 0,
        },
      });
      myChart.setOption(this.option);
      this.bindListen(myChart);
    },
    getPie3D(pieData, internalDiameterRatio, opacity = 0.8) {
      //internalDiameterRatio:透明的空心占比
      let that = this;
      let series = [];
      let sumValue = 0;
      let startValue = 0;
      let endValue = 0;
      let legendData = [];
      let legendBfb = [];
      let k = 1 - internalDiameterRatio;
      pieData.sort((a, b) => {
        return b.value - a.value;
      });
      // 为每一个饼图数据，生成一个 series-surface 配置
      for (let i = 0; i < pieData.length; i++) {
        sumValue += pieData[i].value;
        let seriesItem = {
          name:
            typeof pieData[i].name === "undefined"
              ? `series${i}`
              : pieData[i].name,
          type: "surface",
          parametric: true,
          wireframe: {
            show: false,
          },
          pieData: pieData[i],
          pieStatus: {
            selected: false,
            hovered: false,
            k: k,
          },
          center: ["50%", "50%"],
        };
        if (typeof pieData[i].itemStyle !== "undefined") {
          const itemStyle = {};
          itemStyle.color =
            typeof pieData[i].itemStyle.color !== "undefined"
              ? pieData[i].itemStyle.color
              : opacity;
          itemStyle.opacity =
            typeof pieData[i].itemStyle.opacity !== "undefined"
              ? pieData[i].itemStyle.opacity
              : opacity;
          seriesItem.itemStyle = itemStyle;
        }
        series.push(seriesItem);
      }

      // 使用上一次遍历时，计算出的数据和 sumValue，调用 getParametricEquation 函数，
      // 向每个 series-surface 传入不同的参数方程 series-surface.parametricEquation，也就是实现每一个扇形。
      legendData = [];
      legendBfb = [];
      for (let i = 0; i < series.length; i++) {
        endValue = startValue + series[i].pieData.value;
        series[i].pieData.startRatio = startValue / sumValue;
        series[i].pieData.endRatio = endValue / sumValue;
        series[i].parametricEquation = this.getParametricEquation(
          series[i].pieData.startRatio,
          series[i].pieData.endRatio,
          false,
          false,
          k,
          series[i].pieData.value
        );
        startValue = endValue;
        let bfb = that.fomatFloat(series[i].pieData.value / sumValue, 4);
        legendData.push({
          name: series[i].name,
          value: bfb,
        });
        legendBfb.push({
          name: series[i].name,
          value: bfb,
        });
      }
      let boxHeight = this.getHeight3D(series, 25); //通过传参设定3d饼/环的高度，26代表26px
      // 准备待返回的配置项，把准备好的 legendData、series 传入。
      let option = {
        // legend: {
        // 	data: legendData,
        // 	orient: 'horizontal',
        // 	left: 10,
        // 	top: 10,
        // 	itemGap: 10,
        // 	textStyle: {
        // 		color: '#000',
        // 	},
        // 	show: true,
        // 	icon: "circle",
        // 	formatter: function(param) {
        // 		let item = legendBfb.filter(item => item.name == param)[0];
        // 		let bfs = that.fomatFloat(item.value * 100, 2) + "%";
        // 		return `${item.name}  ${bfs}`;
        // 	}
        // },
        labelLine: {
          show: true,
          length: 40, // 设置指示线的长度
          lineStyle: {
            color: "#878B8F",
            opacity: 0.7,
          },
        },
        label: {
          show: true,
          position: "outside",
          rich: {
            b: {
              color: "#999",
              fontSize: 14,
              lineHeight: -30,
            },
            c: {
              fontSize: 16,
              lineHeight: 30,
              color: "#72F4FA",
              fontWeight: 700,
            },
          },
          textStyle: {
            color: "#72F4FA",
          },
          formatter: "{b|{b} \n}{c|{c}}{b|}",
        },
        tooltip: {
          formatter: (params) => {
            if (
              params.seriesName !== "mouseoutSeries" &&
              params.seriesName !== "pie2d"
            ) {
              let bfb = (
                (option.series[params.seriesIndex].pieData.endRatio -
                  option.series[params.seriesIndex].pieData.startRatio) *
                100
              ).toFixed(2);
              return (
                `${params.seriesName}<br/>` +
                `<span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:${params.color};"></span>` +
                `${bfb}%`
              );
            }
          },
        },
        xAxis3D: {
          min: -1,
          max: 1,
        },
        yAxis3D: {
          min: -1,
          max: 1,
        },
        zAxis3D: {
          min: -1,
          max: 1,
        },
        grid3D: {
          show: false,
          boxHeight: boxHeight, //圆环的高度
          viewControl: {
            //3d效果可以放大、旋转等，请自己去查看官方配置
            alpha: 40, //角度
            distance: 300, //调整视角到主体的距离，类似调整zoom
            rotateSensitivity: 0, //设置为0无法旋转
            zoomSensitivity: 0, //设置为0无法缩放
            panSensitivity: 0, //设置为0无法平移
            autoRotate: false, //自动旋转
          },
        },
        series: series,
      };
      return option;
    },
    //获取3d丙图的最高扇区的高度
    getHeight3D(series, height) {
      series.sort((a, b) => {
        return b.pieData.value - a.pieData.value;
      });
      return (height * 25) / series[0].pieData.value;
    },

    // 生成扇形的曲面参数方程，用于 series-surface.parametricEquation
    getParametricEquation(startRatio, endRatio, isSelected, isHovered, k, h) {
      // 计算
      let midRatio = (startRatio + endRatio) / 2;
      let startRadian = startRatio * Math.PI * 2;
      let endRadian = endRatio * Math.PI * 2;
      let midRadian = midRatio * Math.PI * 2;
      // 如果只有一个扇形，则不实现选中效果。
      if (startRatio === 0 && endRatio === 1) {
        isSelected = false;
      }
      // 通过扇形内径/外径的值，换算出辅助参数 k（默认值 1/3）
      k = typeof k !== "undefined" ? k : 1 / 3;
      // 计算选中效果分别在 x 轴、y 轴方向上的位移（未选中，则位移均为 0）
      let offsetX = isSelected ? Math.cos(midRadian) * 0.1 : 0;
      let offsetY = isSelected ? Math.sin(midRadian) * 0.1 : 0;
      // 计算高亮效果的放大比例（未高亮，则比例为 1）
      let hoverRate = isHovered ? 1.05 : 1;
      // 返回曲面参数方程
      return {
        u: {
          min: -Math.PI,
          max: Math.PI * 3,
          step: Math.PI / 32,
        },
        v: {
          min: 0,
          max: Math.PI * 2,
          step: Math.PI / 20,
        },
        x: function (u, v) {
          if (u < startRadian) {
            return (
              offsetX +
              Math.cos(startRadian) * (1 + Math.cos(v) * k) * hoverRate
            );
          }
          if (u > endRadian) {
            return (
              offsetX + Math.cos(endRadian) * (1 + Math.cos(v) * k) * hoverRate
            );
          }
          return offsetX + Math.cos(u) * (1 + Math.cos(v) * k) * hoverRate;
        },
        y: function (u, v) {
          if (u < startRadian) {
            return (
              offsetY +
              Math.sin(startRadian) * (1 + Math.cos(v) * k) * hoverRate
            );
          }
          if (u > endRadian) {
            return (
              offsetY + Math.sin(endRadian) * (1 + Math.cos(v) * k) * hoverRate
            );
          }
          return offsetY + Math.sin(u) * (1 + Math.cos(v) * k) * hoverRate;
        },
        z: function (u, v) {
          if (u < -Math.PI * 0.5) {
            return Math.sin(u);
          }
          if (u > Math.PI * 2.5) {
            return Math.sin(u) * h * 0.1;
          }
          return Math.sin(v) > 0 ? 1 * h * 0.1 : -1;
        },
      };
    },

    fomatFloat(num, n) {
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

    bindListen(myChart) {
      // 监听鼠标事件，实现饼图选中效果（单选），近似实现高亮（放大）效果。
      let that = this;
      let selectedIndex = "";
      let hoveredIndex = "";
      // 监听点击事件，实现选中效果（单选）
      myChart.on("click", function (params) {
        // 从 option.series 中读取重新渲染扇形所需的参数，将是否选中取反。
        let isSelected =
          !that.option.series[params.seriesIndex].pieStatus.selected;
        let isHovered =
          that.option.series[params.seriesIndex].pieStatus.hovered;
        let k = that.option.series[params.seriesIndex].pieStatus.k;
        let startRatio =
          that.option.series[params.seriesIndex].pieData.startRatio;
        let endRatio = that.option.series[params.seriesIndex].pieData.endRatio;
        // 如果之前选中过其他扇形，将其取消选中（对 option 更新）
        if (selectedIndex !== "" && selectedIndex !== params.seriesIndex) {
          that.option.series[selectedIndex].parametricEquation =
            that.getParametricEquation(
              that.option.series[selectedIndex].pieData.startRatio,
              that.option.series[selectedIndex].pieData.endRatio,
              false,
              false,
              k,
              that.option.series[selectedIndex].pieData.value
            );
          that.option.series[selectedIndex].pieStatus.selected = false;
        }
        // 对当前点击的扇形，执行选中/取消选中操作（对 option 更新）
        that.option.series[params.seriesIndex].parametricEquation =
          that.getParametricEquation(
            startRatio,
            endRatio,
            isSelected,
            isHovered,
            k,
            that.option.series[params.seriesIndex].pieData.value
          );
        that.option.series[params.seriesIndex].pieStatus.selected = isSelected;
        // 如果本次是选中操作，记录上次选中的扇形对应的系列号 seriesIndex
        isSelected ? (selectedIndex = params.seriesIndex) : null;
        // 使用更新后的 option，渲染图表
        myChart.setOption(that.option);
      });
      // 监听 mouseover，近似实现高亮（放大）效果
      myChart.on("mouseover", function (params) {
        // 准备重新渲染扇形所需的参数
        let isSelected;
        let isHovered;
        let startRatio;
        let endRatio;
        let k;
        // 如果触发 mouseover 的扇形当前已高亮，则不做操作
        if (hoveredIndex === params.seriesIndex) {
          return;
          // 否则进行高亮及必要的取消高亮操作
        } else {
          // 如果当前有高亮的扇形，取消其高亮状态（对 option 更新）
          if (hoveredIndex !== "") {
            // 从 option.series 中读取重新渲染扇形所需的参数，将是否高亮设置为 false。
            isSelected = that.option.series[hoveredIndex].pieStatus.selected;
            isHovered = false;
            startRatio = that.option.series[hoveredIndex].pieData.startRatio;
            endRatio = that.option.series[hoveredIndex].pieData.endRatio;
            k = that.option.series[hoveredIndex].pieStatus.k;
            // 对当前点击的扇形，执行取消高亮操作（对 option 更新）
            that.option.series[hoveredIndex].parametricEquation =
              that.getParametricEquation(
                startRatio,
                endRatio,
                isSelected,
                isHovered,
                k,
                that.option.series[hoveredIndex].pieData.value
              );
            that.option.series[hoveredIndex].pieStatus.hovered = isHovered;
            // 将此前记录的上次选中的扇形对应的系列号 seriesIndex 清空
            hoveredIndex = "";
          }
          // 如果触发 mouseover 的扇形不是透明圆环，将其高亮（对 option 更新）
          if (
            params.seriesName !== "mouseoutSeries" &&
            params.seriesName !== "pie2d"
          ) {
            // 从 option.series 中读取重新渲染扇形所需的参数，将是否高亮设置为 true。
            isSelected =
              that.option.series[params.seriesIndex].pieStatus.selected;
            isHovered = true;
            startRatio =
              that.option.series[params.seriesIndex].pieData.startRatio;
            endRatio = that.option.series[params.seriesIndex].pieData.endRatio;
            k = that.option.series[params.seriesIndex].pieStatus.k;
            // 对当前点击的扇形，执行高亮操作（对 option 更新）
            that.option.series[params.seriesIndex].parametricEquation =
              that.getParametricEquation(
                startRatio,
                endRatio,
                isSelected,
                isHovered,
                k,
                that.option.series[params.seriesIndex].pieData.value + 5
              );
            that.option.series[params.seriesIndex].pieStatus.hovered =
              isHovered;
            // 记录上次高亮的扇形对应的系列号 seriesIndex
            hoveredIndex = params.seriesIndex;
          }
          // 使用更新后的 option，渲染图表
          myChart.setOption(that.option);
        }
      });
      // 修正取消高亮失败的 bug
      myChart.on("globalout", function () {
        // 准备重新渲染扇形所需的参数
        let isSelected;
        let isHovered;
        let startRatio;
        let endRatio;
        let k;
        if (hoveredIndex !== "") {
          // 从 option.series 中读取重新渲染扇形所需的参数，将是否高亮设置为 true。
          isSelected = that.option.series[hoveredIndex].pieStatus.selected;
          isHovered = false;
          k = that.option.series[hoveredIndex].pieStatus.k;
          startRatio = that.option.series[hoveredIndex].pieData.startRatio;
          endRatio = that.option.series[hoveredIndex].pieData.endRatio;
          // 对当前点击的扇形，执行取消高亮操作（对 option 更新）
          that.option.series[hoveredIndex].parametricEquation =
            that.getParametricEquation(
              startRatio,
              endRatio,
              isSelected,
              isHovered,
              k,
              that.option.series[hoveredIndex].pieData.value
            );
          that.option.series[hoveredIndex].pieStatus.hovered = isHovered;
          // 将此前记录的上次选中的扇形对应的系列号 seriesIndex 清空
          hoveredIndex = "";
        }
        // 使用更新后的 option，渲染图表
        myChart.setOption(that.option);
      });
    },

    /* 初始化生成柱状图 */
    getOption() {
      let myChart = echarts.init(document.getElementById("industrialIncrease"));
      this.option1 = {
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        grid: {
          top: "10%",
          left: "10%",
          right: "10%",
          bottom: "10%",
          containLabel: true,
        },
        xAxis: {
          show: true,
          axisLabel: {
            color: "#999", // x轴字颜色
            formatter: "{value}",
            show: true,
          },
          splitLine: { show: false },
          axisLine: {
            show: true,
          },
        },
        yAxis: {
          type: "category",
          inverse: true, // 倒叙
          // lineHeight: 80,
          axisLabel: {
            color: "#999 ",
            opacity: 0.8,
            fontFamily: "PingFangSC-Regular",
            fontSize: 14,
            formatter: (val) => {
              return `${val}`;
            },
          },
          axisLine: {
            show: false, // 轴线
          },
          axisTick: {
            show: false, // 刻度线
          },
          data: [
            "浙能",
            "国能",
            "华能",
            "大唐",
            "华电",
            "华润",
            "台塑",
            "巨华",
          ],
        },
        series: [
          {
            name: "Echarts",
            type: "bar",
            barWidth: 10,
            showBackground: true,
            barMaxWidth: 20,
            barMinWidth: 5,
            label: {
              show: true,
              position: "top",
              textStyle: {
                fontSize: 14,
                color: "#72F4FA",
                fontWeight: 700,
                fontFamily: "FusiBold",
              },
            },
            itemStyle: {
              normal: {
                barBorderRadius: [0, 10, 10, 0],
                color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [
                  { offset: 0, color: "#5CFC40" },
                  { offset: 1, color: "#00CBFB" },
                ]),
                borderWidth: 1,
                borderColor: "#333",
                borderGap: 3,
                lineDash: [5, 1],
              },
            },
            data: [1345, 4332, 4211, 4351, 5135, 5133, 5613, 3530],
          },
        ],
      };
      myChart.setOption(this.option1);
    },

    // 3d柱状图
    getOption4() {
      //初始化echarts
      let myChart = echarts.init(document.getElementById("biao4"));

      let num = ["31", "44", "21", "35", "76", "31", "65", "53"];
      let xData = [
        "浙江",
        "华能",
        "华能",
        "啊啊",
        "撒地方",
        "三啊",
        "大师答",
        "大师答",
      ];
      var colors = [
        {
          type: "linear",
          x: 0,
          x2: 1,
          y: 0,
          y2: 0,
          colorStops: [
            {
              offset: 0,
              color: "##52D2D8",
            },
            {
              offset: 1,
              color: "##1F8AAC",
            },
          ],
        },
        {
          type: "linear",
          x: 0,
          x2: 0,
          y: 0,
          y2: 1,
          colorStops: [
            {
              offset: 0,
              color: "#52D2D8",
            },
            {
              offset: 1,
              color: "#1F8AAC",
            },
          ],
        },
      ];
      var barWidth = 18; // 柱子宽度
      // 绘制图表
      this.option4 = {
        title: {
          text: "锅炉热效率",
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
            name: "2020",
            type: "bar",
            barGap: "14%",
            barWidth: 18,
            label: {
              normal: {
                show: true,
                position: "top",
                textStyle: {
                  fontSize: 14,
                  color: "#72F4FA",
                  fontWeight: 700,
                  fontFamily: "FusiBold",
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
            data: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            symbol: "diamond",
            symbolOffset: ["0%", "50%"],
            symbolSize: [barWidth, 10],
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
            symbolSize: [barWidth, (10 * (barWidth - 1)) / barWidth],
            itemStyle: {
              normal: {
                borderColor: "#1F8AAC",
                borderWidth: 1,
                color: "#1F8AAC",
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
          data: xData,
          offset: 6,
          axisLine: { show: false, lineStyle: { color: " #CCCCCC" } },
          axisTick: {
            alignWithLabel: true,
          },
          axisLabel: {
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
          name: "(%)",
          nameTextStyle: {
            align: "right",
            color: "#999",
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
      myChart.setOption(this.option4);
    },

    // 折线面积图
    getOption5() {
      let myChart = echarts.init(document.getElementById("biao5"));
      this.option5 = {
        title: {
          text: "汽轮机热耗率kJ/kWh",
          textStyle: {
            //主标题的属性
            color: "#fff", //颜色
            fontSize: 14, //大小
            fontWeight: 400,
            fontFamily: "PingFangSC-Regular",
          },
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            label: {
              backgroundColor: "#6a7985",
            },
          },
        },
        color: ["#482CFB", "#01F0FF"],
        legend: {
          data: ["2021", "2022"],
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
            boundaryGap: false,
            data: [
              "浙能",
              "国能",
              "华能",
              "大唐",
              "华电",
              "华润",
              "台塑",
              "巨华",
            ],
            offset: 6,
            axisLine: { lineStyle: { color: " #CCCCCC" } },
            axisTick: {
              alignWithLabel: true,
            },
            axisLabel: {
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
            nameTextStyle: {
              align: "right",
              color: "#999",
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
        ],
        series: [
          {
            name: "2021",
            data: [320, 282, 491, 134, 590, 330, 110, 110],
            type: "line",
            lineStyle: {
              color: "#482CFB",
            },
            connectNulls: true,
            symbol: "none",
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: "#3A80EB",
                  opacity: 0.1,
                },
                {
                  offset: 1,
                  color: "#3A80EB",
                  opacity: 0.2,
                },
              ]),
            },
          },
          {
            name: "2022",
            data: [220, 182, 191, 234, 290, 330, 310, 210],
            type: "line",
            lineStyle: {
              color: "#01F0FF",
            },
            connectNulls: true,
            symbol: "none",
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: "#3A80EB",
                  opacity: 0,
                },
                {
                  offset: 1,
                  color: "#3A80EB",
                  opacity: 0,
                },
              ]),
            },
          },
        ],
      };
      this.option5 && myChart.setOption(this.option5);
    },

    // 正负条形图
    getOption6() {
      let myChart = echarts.init(document.getElementById("biao6"), "dark");
      this.option6 = {
        backgroundColor: "", //设置无背景色
        title: {
          text: "(集团)",
          textStyle: {
            //主标题的属性
            color: "#fff", //颜色
            fontSize: 14, //大小
            fontWeight: 400,
            fontFamily: "PingFangSC-Regular",
          },
        },
        legend: {
          x: "right", // 水平居右
          icon: "rect", // 图例icon为方块
          itemHeight: 10, // 图例icon高度
          itemWidth: 10, // 图例icon宽度
          textStyle: {
            color: "#fff", // 图例文字颜色
          },
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "shadow", // 默认为直线，可选为：'line' | 'shadow',
            label: {
              backgroundColor: "#6a7985",
            },
          },
          formatter: (params) => {
            if (!params.length) return "";
            let s = params[0].axisValueLabel + "<br/>";
            for (const iterator of params) {
              // 如果是负数则反转
              let d = iterator.data < 0 ? -iterator.data : iterator.data;
              s += iterator.marker + iterator.seriesName + "：" + d + "<br/>";
            }
            return s;
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
            type: "value",
            axisLine: { show: false, lineStyle: { color: " #CCCCCC" } },
            axisTick: {
              show: false,
            },
            splitLine: { show: false },
            axisLabel: {
              formatter: (value) => {
                // 负数取反 显示的就是正数了
                if (value < 0) return -value;
                else return value;
              },
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
            type: "category",
            axisTick: {
              show: false,
              lineStyle: { color: "#666" },
            },
            axisLabel: {
              textStyle: {
                color: "#999",
                fontSize: 14,
              },
            },
            data: [
              "浙能",
              "国能",
              "华能",
              "大唐",
              "华电",
              "华润",
              "台塑",
              "巨华",
            ],
          },
        ],
        series: [
          {
            name: "2021",
            type: "bar",
            stack: "总量",
            showBackground: true,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
            },
            barWidth: 18,
            label: {
              show: true,
              position: "top",
              textStyle: {
                fontSize: 14,
                color: "#72F4FA",
                fontWeight: 700,
                fontFamily: "FusiBold",
              },
            },
            barWidth: 9,
            data: [320, 302, 341, 374, 390, 450, 420, 90],
            itemStyle: {
              normal: {
                barBorderRadius: [0, 10, 10, 0],
                color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [
                  { offset: 0, color: "#00FFCC" },
                  { offset: 1, color: "#143259" },
                ]),
              },
            },
          },
          {
            name: "2020",
            type: "bar",
            stack: "总量",
            barWidth: 18,
            label: {
              show: true,
              position: "top",
              textStyle: {
                fontSize: 14,
                color: "#72F4FA",
                fontWeight: 700,
                fontFamily: "FusiBold",
              },
              formatter: (value) => {
                // 值都是负数的 所以需要取反一下
                return -value.data;
              },
            },
            data: [-120, -132, -101, -134, -190, -230, -210, -100],
            itemStyle: {
              normal: {
                barBorderRadius: [10, 0, 0, 10],
                color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [
                  { offset: 0, color: "#143259" },
                  { offset: 1, color: "#006FFF" },
                ]),
              },
            },
          },
        ],
      };
      this.option6 && myChart.setOption(this.option6);
    },
    // 心电图1
    getOption7() {
      var myChart1 = echarts.init(document.getElementById("xindian1"), "dark");
      let base = +new Date(1968, 9, 3);
      let oneDay = 24 * 3600 * 1000;
      let date = [];
      let data = [Math.random() * 300];
      for (let i = 1; i < 20000; i++) {
        var now = new Date((base += oneDay));
        date.push(
          [now.getFullYear(), now.getMonth() + 1, now.getDate()].join("/")
        );
        data.push(Math.round((Math.random() - 0.5) * 20 + data[i - 1]));
      }
      this.option7 = {
        backgroundColor: "", //设置无背景色
        tooltip: {
          trigger: "axis",
          position: function (pt) {
            return [pt[0], "10%"];
          },
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: "none",
            },
            restore: { show: false },
            saveAsImage: { show: false },
          },
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: date,
        },
        yAxis: {
          type: "value",
          boundaryGap: [0, "100%"],
        },
        dataZoom: [
          {
            type: "inside",
            start: 0,
            end: 10,
          },
          {
            start: 0,
            end: 10,
          },
        ],
        series: [
          {
            name: "Fake Data",
            type: "line",
            symbol: "none",
            sampling: "lttb",
            itemStyle: {
              color: "rgb(255, 70, 131)",
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: "rgb(255, 158, 68)",
                },
                {
                  offset: 1,
                  color: "rgb(255, 70, 131)",
                },
              ]),
            },
            data: data,
          },
        ],
      };
      this.option7 && myChart1.setOption(this.option7);
    },
  },
};
</script>
<style scoped lang='less'>
.mian-body {
  margin-top: 80px;
  margin-left: 45px;
  .main-left {
    float: left;
    margin-right: 50px;
    width: 1280px;
    .left-top {
      width: 1280px;
      .left-top-left {
        float: left;
        width: 415px;
        margin-right: 17px;
        .left-one {
          width: 50%;
          height: 350px;
          float: left;
          .left-one-img {
            width: 100%;
            height: 177px;
            position: relative;
            top: 50px;
            // left: 25px;
          }
          .left-one-text {
            width: 60px;
            height: 25px;
            font-family: PingFang-SC-Semibold;
            font-size: 14px;
            color: #f5f7fd;
            line-height: 25px;
            font-weight: 600;
            position: absolute;
            top: 115px;
            left: 75px;
          }
          .left-text {
            margin-top: 80px;
            font-family: FusiBold;
            font-size: 30px;
            color: #3df4ff;
            letter-spacing: 1.88px;
            text-align: center;
            line-height: 24px;
            font-weight: 700;
          }
        }
        .left-two {
          width: 50%;
          height: 350px;
          float: right;
          .left-two-img {
            width: 100%;
            height: 177px;
            position: relative;
            top: 50px;
            // left: 25px;
          }
          .left-two-text {
            width: 60px;
            height: 25px;
            font-family: PingFang-SC-Semibold;
            font-size: 14px;
            color: #f5f7fd;
            line-height: 25px;
            font-weight: 600;
            position: absolute;
            top: 115px;
            left: 80px;
          }
          .left-text {
            margin-top: 80px;
            font-family: FusiBold;
            font-size: 30px;
            color: #3df4ff;
            letter-spacing: 1.88px;
            text-align: center;
            line-height: 24px;
            font-weight: 700;
          }
        }
      }
      .left-top-center {
        float: left;
        margin-right: 20px;
        width: 414px;
        height: 350px;
        position: relative;
        .cityGreenLand-charts {
          height: 350px;
          width: 100%;
        }
        .left-top-center-text {
          position: absolute;
          top: 155px;
          left: 185px;
          font-family: AlibabaPuHuiTi-Bold;
          font-size: 16px;
          color: #ffffff;
          letter-spacing: 1px;
          font-weight: 700;
        }
      }
      .left-top-right {
        float: right;
        // display: inline-block;
        width: 414px;
        height: 350px;
        #industrialIncrease {
          height: 100%;
          width: 100%;
        }
      }
    }

    .left-footer {
      width: 1285px;
      margin-top: 80px;
      .left-footer-left {
        float: left;
        width: 415px;
        height: 350px;
        margin-right: 20px;
        margin-top: 100px;
        #biao4 {
          width: 100%;
          height: 100%;
        }
      }
      .left-footer-center {
        float: left;
        margin-right: 25px;
        width: 415px;
        height: 350px;
        margin-top: 100px;
        #biao5 {
          width: 100%;
          height: 100%;
        }
      }
      .left-footer-right {
        float: right;
        width: 410px;
        height: 350px;
        margin-top: 100px;
        #biao6 {
          width: 100%;
          height: 100%;
        }
      }
    }
  }
  .main-center {
    float: left;
    width: 800px;
    height: 100px;
    text-align: left;
    padding-top: 30px;
    .main-center1,
    .main-center2 {
      float: left;
      width: 280px;
      padding-left: 120px;
      font-size: 60px;
      font-family: YouYuan;
      font-weight: 700;
      background-image: -webkit-linear-gradient(
        152deg,
        #ffffff 0%,
        #98d0f3 100%
      );
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
  }
  .main-right {
    float: right;
    width: 1280px;
    height: 824px;
    margin-right: 50px;
    .main-right-left {
      float: left;
      width: 825px;
      height: 100%;
      .main-right-left-top {
        width: 825px;
        height: 225px;
        position: relative;
        .main-right-left-text1 {
          margin-left: 155px;
          margin-top: 25px;
          width: 60px;
          height: 20px;
          font-family: FusiBold;
          font-size: 20px;
          color: #3df4ff;
          letter-spacing: 1px;
          line-height: 20px;
          font-weight: 700;
          text-align: center;
        }
        .main-right-left-text2,
        .main-right-left-text3,
        .main-right-left-text4,
        .main-right-left-text5,
        .main-right-left-text6 {
          position: absolute;
          font-family: FusiBold;
          font-size: 20px;
          color: #f7f388;
          letter-spacing: 1px;
          text-align: center;
          line-height: 20px;
          font-weight: 700;
          .wan {
            font-family: PingFang-SC-Bold;
            font-size: 12px;
            color: #f7f388;
            letter-spacing: 0;
            text-align: center;
            line-height: 12px;
            font-weight: 700;
          }
        }
        .main-right-left-text2 {
          top: 70px;
          right: 690px;
        }
        .main-right-left-text3 {
          top: 115px;
          right: 690px;
        }
        .main-right-left-text4 {
          top: 160px;
          right: 690px;
        }
        .main-right-left-text5 {
          top: 61px;
          left: 710px;
        }
        .main-right-left-text6 {
          top: 138px;
          left: 720px;
        }
      }
      .main-right-left-footer {
        width: 100%;
        height: 500px;
        margin-top: 80px;
        .footer-one,
        .footer-two,
        .footer-three,
        .footer-four {
          width: 390px;
          height: 210px;
          background-color: #fff;
        }
        .footer-one,
        .footer-three {
          float: left;
        }
        .footer-two,
        .footer-four {
          float: right;
        }
        .footer-three,
        .footer-four {
          margin-top: 85px;
        }
      }
    }
    .main-right-right {
      float: right;
      width: 425px;
      height: 50px;
      background-color: rgb(238, 255, 192);
    }
  }
}
</style>