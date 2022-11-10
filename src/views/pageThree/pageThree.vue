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
        <div class="top1"></div>
        <div class="top2"></div>
        <div class="top3"></div>
        <div class="top4"></div>
        <div class="footer1"></div>
        <div class="footer2"></div>
        <div class="footer3"></div>
        <div class="footer4"></div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
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
    };
  },
  mounted() {},
  methods: {
    // 重置
    clickBtn2() {
      this.formInline.groupName = "所有集团";
      this.formInline.factoryName = "所有电厂";
      this.formInline.jzName = "所有机组";
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
          }
        })
        .catch((err) => {
          this.$message("查询集团列表接口报错");
        });
    },
    getJzList(val) {
      this.formInline.checked =
        this.formInline.factoryName == "所有电厂" ? true : false;
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
          }
        })
        .catch((err) => {
          this.$message("查询集团列表接口报错");
        });
    },
    getCoalStat() {},
  },
};
</script>
<style scoped lang='less'>
@import url("./pageThree.less");
</style>