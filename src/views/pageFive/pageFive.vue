<template>
  <div class="main-body">
    <div class="top-search">
      <el-form :model="formInline" class="demo-form-inline">
        <el-form-item>
          电厂：
          <div class="search-list">
            <el-select
              v-model="formInline.dianJ"
              placeholder="电厂"
              :popper-append-to-body="false"
            >
              <el-option
                v-for="item in formInline.conditionList"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </div>
          <div class="btn1" @click="getPointValue">
            <img src="../../assets/btn1.png" alt="" />
          </div>
          <div class="btn2" @click="clickBtn2">
            <img src="../../assets/btn2.png" alt="" />
          </div>
        </el-form-item>
      </el-form>
    </div>
    <div class="footer">
      <div class="table">
        <div class="titleaa">{{ title }}</div>
        <el-table
          :data="tableData.slice((currentPage - 1) * pageSize,currentPage * pageSize)"
          :max-height="690"
          style="width: 100%"
        >
          <el-table-column
            v-for="(item, index) in tableTitle"
            :key="index"
            :label="item"
            header-align="center"
            :width="(item =='单位'||item =='U1'||item =='U2'||item =='U3'||item =='U4')?'100':''"
          >
            <template slot-scope="scope" style="text-align: center">
              <span :style="((/^[0-9]+.?[0-9]*$/.test(tableData.slice((currentPage - 1) * pageSize,currentPage * pageSize)[scope.$index][index])) || (/^[0-9]+.?[0-9]*$/.test(-tableData.slice((currentPage - 1) * pageSize,currentPage * pageSize)[scope.$index][index])))?'font-weight:900':'font-weight:300'">{{tableData.length > 0 ? tableData.slice((currentPage - 1) * pageSize,currentPage * pageSize)[scope.$index][index] : ""
              }}</span>
            </template>
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
</template>
<script>
export default {
  data() {
    return {
      formInline: {
        conditionList: [],
        dianJ: "HRCN",
      },
      tableData: [],
      // 默认显示第几页
      currentPage: 1,
      // 总条数，根据接口获取数据长度(注意：这里不能为空)
      totalCount: 1,
      // 个数选择器（可修改）
      pageSize: 8,
      title: "",
      tableTitle: [],
    };
  },
  mounted() {
    this.$nextTick(function () {
      this.getPointSelectCondition();
      this.getPointValue();
      let timeTicket;
      clearInterval(timeTicket);
      timeTicket = window.setInterval(() => {
        this.getPointValue();
      }, 60000);
    })
  },
  methods: {
    clickBtn2(){
        this.formInline.dianJ = 'HRCN'
        this.getPointValue()
    },
    // 显示第几页
    handleCurrentChange(val) {
      // 改变默认的页数
      this.currentPage = val;
    },
    getPointSelectCondition() {
      this.$http({
        method: "get",
        url: `jndpportal/wbjk/getPointSelectCondition.xhtml`,
      }).then((res) => {
        if (res.data[0].res == "success") {
          this.formInline.conditionList = res.data[0].data[0].conditionList;
          console.log(this.formInline.conditionList);
        }
      });
    },
    getPointValue() {
      this.title = ''
      this.tableTitle = []
      this.tableData = []
      let param = {
        id: this.formInline.dianJ,
      };
      this.$http({
        method: "get",
        url: `jndpportal/wbjk/getPointValue.xhtml`,
        params: param,
      })
        .then((res) => {
          if (res.data[0].res == "success") {
            this.title = res.data[0].data[0].TITLE;
            this.tableTitle = res.data[0].data[0].tableTitle;
            this.tableData = res.data[0].data[0].valueList;
            
          }
        })
        .catch((err) => {
          this.$message("查询测点展示接口报错");
        });
    },
  },
};
</script>
<style scoped lang='less'>
@import url("./pageFive.less");
</style>