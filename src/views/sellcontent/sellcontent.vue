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
            <div class="left-text">{{ SSFH }}</div>
          </div>
          <div class="left-two">
            <div class="left-two-img">
              <img src="../../assets/box_1_2.png" alt="" />
              <div class="left-two-text">机组功率</div>
            </div>
            <div class="left-text">{{ JZGL }}</div>
          </div>
        </div>
        <div class="left-top-center">
          <div class="left-top-center-text">原煤量</div>
          <img src="../../assets/pie.png" alt="" />
          <div class="juhua1">巨化集团</div>
          <div class="juhua">{{ juhua }}%</div>
          <div class="taisu1">台塑集团</div>
          <div class="taisu">{{ taisu }}%</div>
          <div class="huarun1">华润集团</div>
          <div class="huarun">{{ huarun }}%</div>
          <div class="huadian1">华电集团</div>
          <div class="huadian">{{ huadian }}%</div>
          <div class="datang1">大唐集团</div>
          <div class="datang">{{ datang }}%</div>
          <div class="huaneng1">华能集团</div>
          <div class="huaneng">{{ huaneng }}%</div>
          <div class="guoneng1">国能集团</div>
          <div class="guoneng">{{ guoneng }}%</div>
          <div class="zheneng1">浙能集团</div>
          <div class="zheneng">{{ zheneng }}%</div>
          <!-- <div class="cityGreenLand-charts" id="cityGreenLand-charts"></div> -->
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
      <div class="main-center1">{{ SSFH }}</div>
      <div class="main-center2">{{ LJFD }}</div>
      <div class="imgs1" v-show="1 == currentIndex">
        <img src="../../assets/p5.png" alt="" />
      </div>
      <div class="imgs2" v-show="2 == currentIndex">
        <img src="../../assets/p1.png" alt="" />
      </div>
      <div class="imgs3" v-show="3 == currentIndex">
        <img src="../../assets/p2.png" alt="" />
      </div>
      <div class="imgs4" v-show="4 == currentIndex">
        <img src="../../assets/p5.png" alt="" />
      </div>
      <div class="imgs5" v-show="5 == currentIndex">
        <img src="../../assets/p3.png" alt="" />
      </div>
      <div class="imgs6" v-show="6 == currentIndex">
        <img src="../../assets/p3.png" alt="" />
      </div>
      <div class="imgs7" v-show="7 == currentIndex">
        <img src="../../assets/p5.png" alt="" />
      </div>
      <div class="imgs8" v-show="8 == currentIndex">
        <img src="../../assets/p6.png" alt="" />
      </div>
      <div class="imgs9" v-show="9 == currentIndex">
        <img src="../../assets/p4.png" alt="" />
      </div>
      <div class="imgs10" v-show="10 == currentIndex">
        <img src="../../assets/p3.png" alt="" />
      </div>
      <div class="imgs11" v-show="11 == currentIndex">
        <img src="../../assets/p3.png" alt="" />
      </div>
      <div class="imgs12" v-show="12 == currentIndex">
        <img src="../../assets/p2.png" alt="" />
      </div>
      <div class="imgs13" v-show="13 == currentIndex">
        <img src="../../assets/p1.png" alt="" />
      </div>
      <div class="imgs14" v-show="14 == currentIndex">
        <img src="../../assets/p6.png" alt="" />
      </div>
      <div class="imgs15" v-show="15 == currentIndex">
        <img src="../../assets/p6.png" alt="" />
      </div>
      <div class="imgs16" v-show="16 == currentIndex">
        <img src="../../assets/p1.png" alt="" />
      </div>
      <div class="imgs17" v-show="17 == currentIndex">
        <img src="../../assets/p1.png" alt="" />
      </div>
      <div class="imgs18" v-show="18 == currentIndex">
        <img src="../../assets/p1.png" alt="" />
      </div>
      <div class="imgs19" v-show="0 == currentIndex">
        <img src="../../assets/p2.png" alt="" />
      </div>
      <div class="biaoge1" v-show="1 == currentIndex">
        <div class="title">浙江浙能嘉华发电有限公司</div>
        <div class="title-de">
          浙江浙能嘉华发电有限公司是浙江省能源集团公司控股的特大型国有火电发电企业,负责嘉兴二期4台600
          MW机组 (已于2005年10月全部投产发电)和嘉兴三期2台1000
          MW机组(将在2011年全部投产发电)的生产
          、经营、建设工作。公司管理和经营的资产超过人民币150亿元。
        </div>
        <el-table
          :data="tableData1"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="115">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="205">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge2" v-show="2 == currentIndex">
        <div class="title">浙江浙能台州第二发电有限责任公司</div>
        <div class="title-de">浙江浙能台州第二发电有限责任公司</div>
        <el-table
          :data="tableData2"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="115">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="205">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge3" v-show="3 == currentIndex">
        <div class="title">浙江浙能北仑发电有限公司</div>
        <div class="title-de">
          浙江浙能北仑发电有限公司为北仑发电厂二期的业主，该公司的主要股东有浙江省能源集团有限公司（51%）、国电电力发展股份有限公司（49%）。二期4号机组装机容量60万千瓦，2000年7月投产发电。二期5号机组装机容量60万千瓦，2000年7月投产发电。二期3号机组装机容量60万千瓦，2000年9月投产发电。
        </div>
        <el-table
          :data="tableData3"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="58">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="80">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="75">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="200">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="150">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="150">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge4" v-show="4 == currentIndex">
        <div class="title">浙江浙能温州发电有限公司</div>
        <div class="title-de">
          被誉为“浙南明珠”的浙江浙能温州发电有限公司，公司前身为温州发电厂，于1990年5月成立，2000年4月18日改制为温州发电有限责任公司，2008年4月17日公司更名为浙江浙能温州发电有限公司。现装机容量为120万千瓦，一期工程两台13.5万千瓦燃煤机组，
          2010年8月8日一期2台机组停止发电，与电网解列，实施永久关停；二期、三期工程两台30万千瓦燃煤机组。目前公司四期工程两台66万千瓦燃煤机组已获国家发改委“路条”，四期建成后装机容量为252万千瓦。
        </div>
        <el-table
          :data="tableData4"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="48">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="70">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="75">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="200">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="150">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="150">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge5" v-show="5 == currentIndex">
        <div class="title">浙江浙能兰溪发电有限责任公司</div>
        <div class="title-de">
          浙江浙能兰溪发电有限责任公司位于浙江省金华兰溪市灵洞乡，距兰溪市中心约4.5公里，距金华市区约21公里，隶属于浙江省能源集团有限公司。公司建有一、二期共四台60万千瓦国产超临界燃煤机组，同步投产脱硫设施，具备再扩建条件。目前，公司总装机容量为240万千瓦，为浙江省最大的内陆绿色电厂。2003年6月筹建以来，公司逐步明确“把公司建设成为国内管理和经营最为精良的现代一流企业”作为企业愿景，树立“人本　科学　创新　一流”的核心理念，明晰公司的使命和发展战略，实现内部管理规范化、标准化、精细化，追求无边界化管理，争创最有价值的一流发电企业。
        </div>
        <el-table
          :data="tableData5"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="195">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="120">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="220">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge6" v-show="6 == currentIndex">
        <div class="title">浙江浙能乐清发电有限责任公司</div>
        <div class="title-de">
          浙能乐清发电有限责任公司位于浙江省东南部沿海地区温州乐清市虹桥镇，由浙江省能源集团公司控股，中国国电电力集团公司、温州能源投资有限公司、温州电力投资有限公司、华峰集团共同出资建设。距乐清市中心20公里，温州市区40公里，地理位置优越。公司于2003年7月开始筹建，2008年一期2台60万千瓦超临界燃煤机组投产发电，2010年二期2台66万千瓦超超临界燃煤机组投产发电，目前公司总装机容量达252万千瓦，年发电量可达135亿千瓦时,并留有扩建2台100万千瓦等级超超临界机组的余地。
        </div>
        <el-table
          :data="tableData6"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="58">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="80">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="75">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="155">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="150">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="150">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge7" v-show="7 == currentIndex">
        <div class="title">浙江浙能嘉兴发电有限公司</div>
        <div class="title-de">
          浙江浙能嘉兴发电有限责任公司，原为嘉兴发电有限责任公司，是国家一流火力发电企业，现有职工1100余人。嘉兴发电厂一期工程为2台300MW国产引进型燃煤机组，股东单位为浙江省能源集团有限公司(所占投资比例为70％)和浙江省电力公司(所占投资比例为30％)，注册资本为8．437亿人民币。
        </div>
        <el-table
          :data="tableData7"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="58">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="80">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="75">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="135">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="130">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="130">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge8" v-show="8 == currentIndex">
        <div class="title">浙江浙能绍兴滨海热电有限责任公司</div>
        <div class="title-de">
          浙江浙能绍兴滨海热电有限责任公司隶属于浙江省能源集团有限公司，地处以“人杰地灵”、“名人荟萃”而闻名的古越文化的发祥地--绍兴，地理位置优越，交通便利。公司前期2台125MW机组，第一期工程建设规模为2*30万千瓦燃煤热电机组，两台机组已分别于2011年6月和10月中旬正式投入商业运行，现为全国规模最大的热电机组；二期扩建4台5万抽背式热电机组方案已获批准，现已按要求开展前期工作。
        </div>
        <el-table
          :data="tableData8"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="165">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="170">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="170">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge9" v-show="9 == currentIndex">
        <div class="title">浙江东南发电股份有限公司（台州发电厂）</div>
        <div class="title-de">
          台州发电厂位于浙江省台州市椒江区前所街道，是国家大一型企业，全国一流火力发电厂，浙江省主力火力发电厂，装有2台300MW、2台330MW和6台135MW机组，总装机容量2070MW。台州发电厂坚持发展为第一要务，以创新谋求企业新发展，与时俱进、不断拼搏，实现了企业跨越式发展，整体实力显著增强。先后荣获了“全国电力系统一流企业”、“全国精神文明建设先进单位”、国电公司“双文明单位”、
          “全国绿化模范单位”等20多项省部级以上荣誉称号。
        </div>
        <el-table
          :data="tableData9"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="120">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="210">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge10" v-show="10 == currentIndex">
        <div class="title">浙江温州特鲁莱发电有限责任公司</div>
        <div class="title-de">
          位于浙江省温州市。华润电力持有其40%的权益。该公司现有两台300MW燃煤发电机组。机组由中国设备制造商提供，所发电力出售给华东电网公司下属的浙江省电网。燃煤来自中国市场。
        </div>
        <el-table
          :data="tableData10"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="120">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="210">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge11" v-show="11 == currentIndex">
        <div class="title">浙江浙能长兴发电有限责任公司</div>
        <div class="title-de">
          位于浙江省温州市。华润电力持有其40%的权益。该公司现有两台300MW燃煤发电机组。机组由中国设备制造商提供，所发电力出售给华东电网公司下属的浙江省电网。燃煤来自中国市场。
        </div>
        <el-table
          :data="tableData11"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="120">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="210">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge12" v-show="12 == currentIndex">
        <div class="title">浙江国华浙能发电有限公司</div>
        <div class="title-de">
          浙江国华宁海发电厂工程由神华能源股份有限公司与浙江省能源集团有限公司按6∶4的比例共同出资建设，浙江国华浙能发电有限公司负责电厂建设及运营。
          国华宁海电厂位于宁海县临港开发区，一期工程建设规模为4×600MW火力发电机组，同步建设四台机组脱硫和4#机脱硝装置，二期工程建设规模2×1000MW机组同步建成脱硫和脱硝装置，是浙江省“五大百亿”重点建设工程。
        </div>
        <el-table
          :data="tableData12"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="120">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="210">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge13" v-show="13 == currentIndex">
        <div class="title">神华国华（舟山）发电有限责任公司</div>
        <div class="title-de">
          神华国华舟山发电有限责任公司位于浙江省舟山市定海区白泉镇外山咀，距离市区16公里，厂区占地面积1451亩。公司作为“九五”期间省重点工程，始建于1996年，首台125MW机组于1997年11月正式投入商业运行，第二台135MW机组于2004年3月25日动态移交生产，第三台300MW机组于2010年10月投入生产。第二台30万千瓦机组续建项目已获国家发改委路条，项目前期工作正在积极推进。
        </div>
        <el-table
          :data="tableData13"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="120">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="210">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge14" v-show="14 == currentIndex">
        <div class="title">国电浙江北仑第一发电有限公司</div>
        <div class="title-de">
          国电北仑第一发电有限公司(以下简称北仑公司)位于浙江省宁波市北仑区。厂区东西长1200米，南北宽960米，占地1.1平方公里，南北走向一字排列5台60万千瓦发电机组，目前经由三条500千伏和三条220千伏高压输电线经绍兴和杭州瓶窑变和金华双龙变，与华东电网相连接。北仑发电厂是国家"七五"、"八五"、"九五"重点建设项目，是国家第一个利用世界银行贷款建设的火力发电厂，总装机容量300万千瓦。
        </div>
        <el-table
          :data="tableData14"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="120">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="210">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge15" v-show="15 == currentIndex">
        <div class="title">国电浙江北仑第三发电有限公司</div>
        <div class="title-de">
          国电浙江北仑第三发电有限公司成立于2006年12月，是由中国国电集团公司、浙江省能源集团有限公司、宁波开发投资集团有限公司共同出资建立，是目前全国最大火力发电厂之一。公司曾获“浙江省重点建设立功竞赛先进集体”、“宁波市重点工程先进集体”称号。三期工程还获“国家优质工程金奖”、“中国电力工程优质奖”、“中国电力行业优秀设计一等奖”和“浙江省减排优秀工程”等荣誉。
        </div>
        <el-table
          :data="tableData15"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="120">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="210">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge16" v-show="16 == currentIndex">
        <div class="title">浙江大唐国际乌沙山发电有限责任公司</div>
        <div class="title-de">
          浙江大唐国际乌沙山发电有限责任公司位于浙江省宁波市象山县西周镇。由大唐国际发电股份有限公司控股51%，一期工程建设四台60万千瓦国产超临界燃煤发电机组。该项目是浙江省五大百亿工程项目之一，也是全国第一个公开招标确定业主的项目，开创了中国电力建设模式的先河。工程采用先进的环保技术，采用低氮燃烧技术。废水循环利用实现“零排放”，为保护海洋生态环境，排水采取低潮位水下排放。
        </div>
        <el-table
          :data="tableData16"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="165">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="180">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="160">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>

      <div class="biaoge17" v-show="17 == currentIndex">
        <div class="title">华能国际电力股份有限公司（长兴电厂）</div>
        <div class="title-de">
          华能长兴电厂以“上大压小”方式建设两台66万千瓦超超临界机组，两台机组分别于2014年12月17日和29日通过168小时试运。电厂于2010年8月8日按照浙江省政府要求，对两台2×12.5万千瓦机组实施了关停，“上大压小”异地建设两台66万千瓦高效超超临界燃煤机组，坐落在长兴县吕山乡，占地550亩，并留有扩建余地。汽机入口蒸汽参数28MPa/600℃/620℃，为目前国内同类机组最高参数；实施100%汽动给水泵、汽动增压联合风机、增设蒸汽冷却器、数字总线等最新前沿技术；煤仓采用全封闭集束蜂窝型群仓方案，国内首创，占地面积小，由48个六边形筒仓组成，储煤量20万吨；采用“8”字形烟囱，外形独特；采用国际先进的低低温电除尘加高效脱硫除尘方案进行烟尘治理，污染物排放达到燃机排放标准：电除尘效率大于99.92%，烟尘排放浓度小于5mg/Nm3;脱硫效率达到98.7%，SO2排放小于35mg/Nm3;脱硝效率大于80%，NOx排放小于50mg/Nm3;按照“后工业化”设计理念，对厂区大体量的建构筑物（如汽机房、锅炉房、烟囱、冷却塔等）外形进行艺术化处理，与当地江南水乡的山水竹人文自然环境融为一体。
        </div>
        <el-table
          :data="tableData17"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="120">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="210">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>
      <div class="biaoge18" v-show="18 == currentIndex">
        <div class="title">华能国际电力股份有限公司玉环电厂</div>
        <div class="title-de">
          玉环电厂位于浙江省台州市玉环县，由华能国际电力股份有限公司全资建设，规划总装机600万千瓦，现运行有4台100万千瓦超超临界燃煤机组。玉环电厂是国家“863”计划中引进超超临界机组技术，逐步实现国产化的依托工程，于2004年6月开工，
          2006年11月实现了国内首台百万千瓦超超临界燃煤机组投产，2007年11月第四台投产，创造了“一年四投”的新纪录，被列入中国企业世界纪录。
        </div>
        <el-table
          :data="tableData18"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="120">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="210">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>
      <div class="biaoge19" v-show="0 == currentIndex">
        <div class="title">浙江国华浙能发电有限公司</div>
        <div class="title-de">
          浙江国华宁海发电厂工程由神华能源股份有限公司与浙江省能源集团有限公司按6∶4的比例共同出资建设，浙江国华浙能发电有限公司负责电厂建设及运营。
          国华宁海电厂位于宁海县临港开发区，一期工程建设规模为4×600MW火力发电机组，同步建设四台机组脱硫和4#机脱硝装置，二期工程建设规模2×1000MW机组同步建成脱硫和脱硝装置，是浙江省“五大百亿”重点建设工程。
        </div>
        <el-table
          :data="tableData19"
          style="width: 100%; color: #fff; font-weight: 200; font-size: 11px"
        >
          <el-table-column prop="mingcheng" label="名称" width="28">
          </el-table-column>
          <el-table-column prop="rongliang" label="容量(MW)" width="60">
          </el-table-column>
          <el-table-column prop="jizu" label="机组类型" width="55">
          </el-table-column>
          <el-table-column prop="shebei" label="锅炉燃气燃烧设备" width="185">
          </el-table-column>
          <el-table-column prop="qilun" label="汽轮机燃气轮机" width="120">
          </el-table-column>
          <el-table-column prop="fadian" label="发电机" width="210">
          </el-table-column>
          <el-table-column prop="bianya" label="主变压器"> </el-table-column>
        </el-table>
      </div>
    </div>
    <!-- 右边部分 -->
    <div class="main-right">
      <div class="main-right-left">
        <div class="main-right-left-top">
          <div class="main-right-left-text1">
            <span style="color: #fff; font-size: 14px">煤机 </span>
            {{ coalMachine }}
            <!-- <span style="color: #fff">运行 </span> {{ coalMachineFunction }} -->
          </div>
          <div class="main-right-left-text7">
            <span style="color: #fff; font-size: 14px">运行 </span>
            {{ coalMachineFunction }}
          </div>
          <div class="main-right-left-text2">
            {{ hpressure }}
          </div>
          <div class="zi2"><span class="wan" style="color: #f7f388;">台 </span><span>高压</span></div>
          <div class="main-right-left-text3">
           {{ chpressure }}
          </div>
          <div class="zi3"><span class="wan" style="color: #f7f388;">台 </span><span>超高压</span></div>
          <div class="main-right-left-text4">
          {{ cCritical }}
          </div>
          <div class="zi4"><span class="wan" style="color: #f7f388;">台 </span><span>亚临界</span></div>
          <div class="main-right-left-text5">
            {{ yCritical }}
          </div>
          <div class="zi5"><span class="wan" style="color: #f7f388;">台 </span><span>超临界</span></div>
          <div class="main-right-left-text6">
            {{ ccCritical }}
          </div>
          <div class="zi6"><span class="wan" style="color: #f7f388;">台 </span><span>超超临界</span></div>
        </div>
        <div class="main-right-left-footer">
          <div class="footer-one" id="xindian1"></div>
          <div class="footer-two" id="xindian2"></div>
          <div class="footer-three" id="xindian3"></div>
          <div class="footer-four" id="xindian4"></div>
        </div>
      </div>
      <div class="main-right-right">
        <div class="top">
          <div class="text1">
            <span style="color: #fff">煤机 </span> {{ gasMachine}}
            <!-- <span style="color: #fff"> 运行 </span>{{ gasMachineFunction }} -->
          </div>
          <div class="text2"><span style="color: #fff"> 运行 </span>{{ gasMachineFunction }}</div>
          <div class="text3">
            <span class="text11">{{ rqjz }}</span
            ><span class="tai">台</span>
          </div>
          <div class="text4">
            <span class="text11">{{ wnswzjz }}</span
            ><span class="tai">台</span>
          </div>
          <div class="text5">
            <span class="text11">{{ yrlyjz }}</span
            ><span class="tai">台</span>
          </div>
          <div class="text6">燃气机组</div>
          <div class="text7">污泥生物质机组</div>
          <div class="text8">余热利用机组</div>
        </div>
        <div class="center">
          <div id="duiji"></div>
        </div>
        <div class="scroll_table">
          <div class="table-footer" style="display: inline-block; width: 100%">
            <el-table
              class="tablea"
              stripe
              style="width: 375px; text-align: left"
            >
              <el-table-column label="电厂"> </el-table-column>
              <el-table-column label="机组"> </el-table-column>
              <el-table-column label="污染物"> </el-table-column>
              <el-table-column label="时段"> </el-table-column>
              <el-table-column label="倍数"> </el-table-column>
            </el-table>
            <div
              v-if="tableData.length <= 0"
              style="
                color: #fff;
                font-size: 18px;
                text-align: center;
                font-weight: 700;
                margin-top: 70px;
              "
            >
              无
            </div>
            <el-table
              :data="tableData"
              class="table_scroll"
              v-else-if="tableData.length <= 5"
            >
              <el-table-column prop="factoryName" label="电厂">
              </el-table-column>
              <el-table-column prop="crewName" label="机组"> </el-table-column>
              <el-table-column prop="contaminants" label="污染物">
              </el-table-column>
              <el-table-column prop="timeInterval" label="时段">
              </el-table-column>
              <el-table-column prop="multiple" label="倍数"> </el-table-column>
            </el-table>
            <vue-seamless-scroll
              :data="tableData"
              class="seamless-warp"
              style="width: 100%"
              :class-option="classOption"
              v-else-if="tableData.length > 5"
            >
              <el-table :data="tableData" class="table_scroll">
                <el-table-column prop="factoryName" label="电厂">
                </el-table-column>
                <el-table-column prop="crewName" label="机组">
                </el-table-column>
                <el-table-column prop="contaminants" label="污染物">
                </el-table-column>
                <el-table-column prop="timeInterval" label="时段">
                </el-table-column>
                <el-table-column prop="multiple" label="倍数">
                </el-table-column>
              </el-table>
            </vue-seamless-scroll>
          </div>
        </div>
      </div>
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
      tableData1: [
        {
          mingcheng: "#3",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "北京巴布科克威尔科克斯有限公司",
          qilun: "东方汽轮机有限公司",
          fadian: "东方电气集团东方发电机股份有限公司",
          bianya: "重庆ABB变压器有限公司",
        },
        {
          mingcheng: "#4",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "北京巴布科克威尔科克斯有限公司",
          qilun: "东方汽轮机有限公司",
          fadian: "东方电气集团东方发电机股份有限公司",
          bianya: "重庆ABB变压器有限公司",
        },
        {
          mingcheng: "#5",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "特变电工沈阳变压器集团有限公司",
        },
        {
          mingcheng: "#6",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "特变电工沈阳变压器集团有限公司",
        },
        {
          mingcheng: "#7",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#8",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
      ],
      tableData2: [
        {
          mingcheng: "#3",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "东方锅炉股份有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海电气集团股份有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#4",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "东方锅炉股份有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海电气集团股份有限公司",
          bianya: "常州东芝变压器有限公司",
        },
      ],
      tableData3: [
        {
          mingcheng: "#3",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "日本石川岛播磨重工业株式会社",
          qilun: "日本东芝公司",
          fadian: "日本东芝公司",
          bianya: "日本东芝公司",
        },
        {
          mingcheng: "#4",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "日本石川岛播磨重工业株式会社",
          qilun: "日本东芝公司",
          fadian: "日本东芝公司",
          bianya: "日本东芝公司",
        },
        {
          mingcheng: "#5",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "日本石川岛播磨重工业株式会社",
          qilun: "日本东芝公司",
          fadian: "日本东芝公司",
          bianya: "日本东芝公司",
        },
      ],
      tableData4: [
        {
          mingcheng: "#5",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#6",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#7",
          rongliang: "600",
          jizu: "超超临界",
          shebei: "北京巴布科克威尔科克斯有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海电气集团股份有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#8",
          rongliang: "600",
          jizu: "超超临界",
          shebei: "北京巴布科克威尔科克斯有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海电气集团股份有限公司",
          bianya: "常州东芝变压器有限公司",
        },
      ],
      tableData5: [
        {
          mingcheng: "#1",
          rongliang: "600",
          jizu: "超临界",
          shebei: "北京巴布科克威尔科克斯有限公司",
          qilun: "东方汽轮机有限公司",
          fadian: "东方电气集团东方发电机股份有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#2",
          rongliang: "600",
          jizu: "超临界",
          shebei: "北京巴布科克威尔科克斯有限公司",
          qilun: "东方汽轮机有限公司",
          fadian: "东方电气集团东方发电机股份有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#3",
          rongliang: "600",
          jizu: "超临界",
          shebei: "北京巴布科克威尔科克斯有限公司",
          qilun: "东方汽轮机有限公司",
          fadian: "东方电气集团东方发电机股份有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#4",
          rongliang: "600",
          jizu: "超临界",
          shebei: "北京巴布科克威尔科克斯有限公司",
          qilun: "东方汽轮机有限公司",
          fadian: "东方电气集团东方发电机股份有限公司",
          bianya: "常州东芝变压器有限公司",
        },
      ],
      tableData6: [
        {
          mingcheng: "#1",
          rongliang: "600",
          jizu: "超临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#2",
          rongliang: "600",
          jizu: "超临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#3",
          rongliang: "600",
          jizu: "超超临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#4",
          rongliang: "600",
          jizu: "超超临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
      ],
      tableData7: [
        {
          mingcheng: "#1",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "特变电工沈阳变压器集团有限公司",
        },
        {
          mingcheng: "#2",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "特变电工沈阳变压器集团有限公司",
        },
      ],
      tableData8: [
        {
          mingcheng: "#1",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "哈尔滨汽轮机厂有限责任公司",
          fadian: "哈尔滨电机厂有限责任公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#2",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "哈尔滨汽轮机厂有限责任公司",
          fadian: "哈尔滨电机厂有限责任公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#3",
          rongliang: "600",
          jizu: "高压",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "哈尔滨汽轮机厂有限责任公司",
          fadian: "哈尔滨电机厂有限责任公司",
          bianya: "特变电工沈阳变压器集团有限公司",
        },
        {
          mingcheng: "#4",
          rongliang: "600",
          jizu: "高压",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "哈尔滨汽轮机厂有限责任公司",
          fadian: "哈尔滨电机厂有限责任公司",
          bianya: "特变电工沈阳变压器集团有限公司",
        },
        {
          mingcheng: "#5",
          rongliang: "1000",
          jizu: "高压",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "哈尔滨汽轮机厂有限责任公司",
          fadian: "哈尔滨电机厂有限责任公司",
          bianya: "特变电工沈阳变压器集团有限公司",
        },
        {
          mingcheng: "#6",
          rongliang: "1000",
          jizu: "高压",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "哈尔滨汽轮机厂有限责任公司",
          fadian: "哈尔滨电机厂有限责任公司",
          bianya: "特变电工沈阳变压器集团有限公司",
        },
        {
          mingcheng: "#7",
          rongliang: "1000",
          jizu: "高压",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "哈尔滨汽轮机厂有限责任公司",
          fadian: "哈尔滨电机厂有限责任公司",
          bianya: "特变电工沈阳变压器集团有限公司",
        },
      ],
      tableData9: [
        {
          mingcheng: "#7",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "北京巴布科克威尔科克斯有限公司",
          qilun: "法国阿尔斯通公司",
          fadian: "北京重型电机厂",
          bianya: "保定天威变电气股份有限公司",
        },
        {
          mingcheng: "#8",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "北京巴布科克威尔科克斯有限公司",
          qilun: "法国阿尔斯通公司",
          fadian: "北京重型电机厂",
          bianya: "保定天威变电气股份有限公司",
        },
        {
          mingcheng: "#9",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "东方汽轮机有限公司",
          fadian: "东方电气集团东方发电机股份有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#10",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "东方汽轮机有限公司",
          fadian: "东方电气集团东方发电机股份有限公司",
          bianya: "常州东芝变压器有限公司",
        },
      ],
      tableData10: [
        {
          mingcheng: "#3",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
        {
          mingcheng: "#4",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
      ],
      tableData11: [
        {
          mingcheng: "#1",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "北京巴布科克威尔科克斯有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#2",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#3",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#4",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
      ],
      tableData12: [
        {
          mingcheng: "#1",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#2",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#3",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#4",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#5",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
        {
          mingcheng: "#6",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
      ],
      tableData13: [
        {
          mingcheng: "#3",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "特变电工衡阳变压器有限公司",
        },
        {
          mingcheng: "#4",
          rongliang: "300",
          jizu: "亚临界",
          shebei: "上海锅炉厂有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "特变电工衡阳变压器有限公司",
        },
      ],
      tableData14: [
        {
          mingcheng: "#1",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "美国燃烧工程公司",
          qilun: "日本东芝公司",
          fadian: "日本东芝公司",
          bianya: "常州东芝变压器有限公司",
        },
        {
          mingcheng: "#2",
          rongliang: "600",
          jizu: "亚临界",
          shebei: "加拿大BABCOCK-WILCOX公司",
          qilun: "法国阿尔斯通公司",
          fadian: "法国阿尔斯通公司",
          bianya: "法国阿尔斯通公司",
        },
      ],
      tableData15: [
        {
          mingcheng: "#6",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "东方锅炉股份有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
        {
          mingcheng: "#7",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "东方锅炉股份有限公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
      ],
      tableData16: [
        {
          mingcheng: "#1",
          rongliang: "600",
          jizu: "超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "哈尔滨汽轮机厂有限责任公司",
          fadian: "哈尔滨电机厂有限责任公司",
          bianya: "重庆ABB变压器有限公司",
        },
        {
          mingcheng: "#2",
          rongliang: "600",
          jizu: "超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "哈尔滨汽轮机厂有限责任公司",
          fadian: "哈尔滨电机厂有限责任公司",
          bianya: "重庆ABB变压器有限公司",
        },
        {
          mingcheng: "#3",
          rongliang: "600",
          jizu: "超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "哈尔滨汽轮机厂有限责任公司",
          fadian: "哈尔滨电机厂有限责任公司",
          bianya: "重庆ABB变压器有限公司",
        },
        {
          mingcheng: "#4",
          rongliang: "600",
          jizu: "超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "哈尔滨汽轮机厂有限责任公司",
          fadian: "哈尔滨电机厂有限责任公司",
          bianya: "重庆ABB变压器有限公司",
        },
      ],
      tableData17: [
        {
          mingcheng: "#1",
          rongliang: "600",
          jizu: "超超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海电气集团股份有限公司",
          bianya: "特变电工衡阳变压器有限公司",
        },
        {
          mingcheng: "#2",
          rongliang: "600",
          jizu: "超超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海电气集团股份有限公司",
          bianya: "特变电工衡阳变压器有限公司",
        },
      ],
      tableData18: [
        {
          mingcheng: "#1",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电机有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
        {
          mingcheng: "#2",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电机有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
        {
          mingcheng: "#3",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电机有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
        {
          mingcheng: "#4",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "哈尔滨锅炉厂有限责任公司",
          qilun: "上海汽轮机有限公司",
          fadian: "上海汽轮发电机有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
      ],
      tableData19: [
        {
          mingcheng: "#1",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "东方锅炉股份有限公司",
          qilun: "东方汽轮机有限公司",
          fadian: "东方电气集团东方发电机股份有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
        {
          mingcheng: "#2",
          rongliang: "1000",
          jizu: "超超临界",
          shebei: "东方锅炉股份有限公司",
          qilun: "东方汽轮机有限公司",
          fadian: "东方电气集团东方发电机股份有限公司",
          bianya: "保定天威变电气股份有限公司",
        },
      ],
      gasMachine: 0,
      gasMachineFunction: 0,
      rqjz: 0,
      wnswzjz: 0,
      yrlyjz: 0,
      SSFH: 0,
      JZGL: "",
      LJFD: "",
      jtmcName: [],
      mh1num: [],
      coalMachine: 0,
      coalMachineFunction: 0,
      critical: "",
      yCritical: 0,
      cCritical: 0,
      ccCritical: 0,
      hpressure: 0,
      chpressure: 0,
      optionData: [],
      statusChart: null,
      option: {},
      tableData: [],
      currentIndex: 1,
      juhua: 0,
      taisu: 0,
      huarun: 0,
      huadian: 0,
      datang: 0,
      huaneng: 0,
      guoneng: 0,
      zheneng: 0,
    };
  },
  created() {},
  mounted() {
    this.$nextTick(function () {
      this.getOption4();
      this.getOption7();
      let timeTicket;
      clearInterval(timeTicket);
      timeTicket = window.setInterval(() => {
        this.getOption4();
        this.getOption7();
      }, 60000);
      let count = 1;
      setInterval(() => {
        count++;
        this.currentIndex = count % 19;
      }, 5000);
    });
  },
  computed: {
    classOption() {
      return {
        step: 0.8, // 数值越大速度滚动越快
        limitMoveNum: this.tableData.length, // 开始无缝滚动的数据量 this.tableList
        hoverStop: true, // 是否开启鼠标悬停stop
        direction: 1, // 0向下 1向上 2向左 3向右
        openWatch: true, // 开启数据实时监控刷新dom
        singleHeight: 0, // 单步运动停止的高度(默认值0是无缝不停止的滚动) direction => 0/1
        singleWidth: 0, // 单步运动停止的宽度(默认值0是无缝不停止的滚动) direction => 2/3
        waitTime: 1000, // 单步运动停止的时间(默认值1000ms)
      };
    },
  },
  methods: {
    biao() {
      setInterval(() => {
        this.currentIndex++;
        console.log(this.currentIndex);
      }, 2000);
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
            typeof pieData[i].itemStyle[0].color !== "undefined"
              ? pieData[i].itemStyle[0].color
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
        // 		color: '#fff',
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
          // normal: {
          // show: true,
          // position: "inner",
          // rich: {
          //   b: {
          //     color: "#999",
          //     fontSize: 14,
          //     lineHeight: 30,
          //     height: 50,
          //   },
          //   c: {
          //     fontSize: 16,
          //     lineHeight: 30,
          //     height: 50,
          //     color: "#72F4FA",
          //     fontWeight: 700,
          //   },
          // },
          // textStyle: {
          //   color: "#72F4FA",
          //   fontSize: 14,
          // },
          // formatter: "{b|{b}}{c|{c}}{b|}",
          // },
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
            alpha: 50, //角度
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

    // 3d柱状图
    getOption4() {
      //初始化echarts
      let myChart1 = echarts.init(
        document.getElementById("industrialIncrease")
      );
      let myChart2 = echarts.init(document.getElementById("biao4"));
      let myChart5 = echarts.init(document.getElementById("biao5"));
      let myChart6 = echarts.init(document.getElementById("biao6"), "dark");
      //锅炉热效率
      let num = [];
      // 集团名称
      let xData = [];
      let xxData = [];
      let fxData = [];
      // 平均煤耗
      var mydata = [];
      var xxmydata = [];
      // 本日汽机热耗率
      var qjrhl1 = [];
      var qjrhl11 = [];
      // 去年同日汽机热耗率
      var qjrhl2 = [];
      var qjrhl22 = [];
      // 本日厂用电率
      var cydl1 = [];
      var fcydl1 = [];
      var fcydl2 = [];
      var fmydata = [];
      var fqjrhl1 = [];
      var fqjrhl2 = [];
      var fnum = [];
      // 去年厂用电率
      var cydl2 = [];
      this.$http({
        method: "get",
        url: `/jndpportal/wbjk/getSJGL.xhtml`,
      }).then((res) => {
        let result = res.data[0].data[0];
        this.SSFH = result.SSFH;
        this.JZGL = result.JZGL;
        this.LJFD = result.LJFD;
        this.optionData = result.YMLSTR;
        this.optionData.map((item, index) => {
          if (item.name == "巨化") {
            this.juhua = item.value;
          }
          if (item.name == "浙能") {
            this.zheneng = item.value;
          }
          if (item.name == "国能") {
            this.guoneng = item.value;
          }
          if (item.name == "华能") {
            this.huaneng = item.value;
          }
          if (item.name == "大唐") {
            this.datang = item.value;
          }
          if (item.name == "华电") {
            this.huadian = item.value;
          }
          if (item.name == "华润") {
            this.huarun = item.value;
          }
          if (item.name == "台塑") {
            this.taisu = item.value;
          }
          item.value = item.value;
        });
        // //构建3d饼状图
        // let myChart3d = echarts.init(
        //   document.getElementById("cityGreenLand-charts")
        // );
        // // 传入数据生成 option
        // this.option3d = this.getPie3D(this.optionData, 0.8);
        // myChart3d.setOption(this.option3d);
        // //是否需要label指引线，如果要就添加一个透明的2d饼状图并调整角度使得labelLine和3d的饼状图对齐，并再次setOption
        // this.option3d.series.push({
        //   name: "pie2d",
        //   type: "pie",
        //   labelLine: {
        //     normal: {
        //       length: 10,
        //       length2: 10,
        //     },
        //   },
        //   avoidLabelOverlap: true,
        //   label: {
        //     normal: {
        //       show: true,
        //       rich: {
        //         b: {
        //           color: "#999",
        //           fontSize: 11,
        //         },
        //         c: {
        //           fontSize: 11,
        //           color: "#72F4FA",
        //           fontWeight: 700,
        //         },
        //       },
        //       formatter: "{b|{b} }{c|{d}% \n}{b|}",
        //     },
        //   },
        //   startAngle: -55, //起始角度，支持范围[0, 360]。
        //   clockwise: false, //饼图的扇区是否是顺时针排布。上述这两项配置主要是为了对齐3d的样式
        //   radius: ["50%", "40%"],
        //   center: ["50%", "50%"],
        //   data: this.optionData,
        //   itemStyle: {
        //     opacity: 0,
        //   },
        // });
        // myChart3d.setOption(this.option3d);

        result.STATSTR.map((item, index) => {
          xData.push(item.jtmc);
          xxData.push(item.jtmc);
          num.push(item.value);
          mydata.push(item.mh1);
          xxmydata.push(item.mh1);
          qjrhl1.push(item.qjrhl1);
          qjrhl11.push(item.qjrhl1);
          qjrhl2.push(item.qjrhl2);
          qjrhl22.push(item.qjrhl2);
          cydl1.push(item.cydl1);
          cydl2.push(0 - item.cydl2);
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
        var barWidth = 18; // 柱子宽度
        // 绘制图表
        fxData = xData.reverse();
        fcydl1 = cydl1.reverse();
        fcydl2 = cydl2.reverse();
        fmydata = mydata.reverse();
        fqjrhl1 = qjrhl1.reverse();
        fqjrhl2 = qjrhl2.reverse();
        this.option4 = {
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
              name: "锅炉热效率",
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
              data: fnum,
              symbol: "diamond",
              symbolOffset: ["0%", "-50%"],
              symbolSize: [barWidth, (10 * (barWidth - 1)) / barWidth],
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
            name: "(%)",
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
        this.option1 = {
          tooltip: {
            trigger: "axis",
            axisPointer: {
              type: "shadow",
            },
            formatter: function (params) {
              let str = " ";
              str =
                '<div style="width:100%;padding:10px 15px 10px 15px;font-size:13px;box-sizing:border-box;border-radius:4px;position:relative;background:rgba(000,000,000,0.5)">' +
                "<div style='display:flex;align-items:center;'>" +
                params[0].name +
                "：" +
                params[0].value +
                "</div>" +
                "</div>";
              return str;
            },
          },
          grid: {
            top: "10%",
            left: "3%",
            right: "4%",
            bottom: "3%",
            containLabel: true,
          },
          xAxis: {
            show: true,
            axisLabel: {
              color: "#999", // x轴字颜色
              // fontSize: 11,
              show: true,
            },
            boundaryGap:['0%', '10%'],
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
            },
            axisLine: {
              show: false, // 轴线
            },
            axisTick: {
              show: false, // 刻度线
            },
            data: xxData,
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
                position: "right",
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
              data: xxmydata,
            },
          ],
        };
        this.option5 = {
          title: {
            // text: "汽轮机热耗率kJ/kWh",
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
          color: ["rgb(134,53,245)", "rgb(117,251,252)"],
          legend: {
            data: ["2021", "2022"],
            x: "right", // 水平居右
            icon: "rect", // 图例icon为方块
            itemHeight: 10, // 图例icon高度
            itemWidth: 10, // 图例icon宽度
            textStyle: {
              color: "#fff", // 图例文字颜色
              // fontSize: 11,
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
              data: xxData,
              offset: 6,
              axisLine: { lineStyle: { color: " #CCCCCC" } },
              axisTick: {
                alignWithLabel: true,
              },
              axisLabel: {
                interval: 0,
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
              data: qjrhl11,
              type: "line",
              lineStyle: {
                color: "rgb(134,53,245)",
              },
              connectNulls: true,
              symbol: "none",
              areaStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {
                    offset: 0,
                    color: "rgb(20,29,85)",
                    opacity: 0.1,
                  },
                  {
                    offset: 1,
                    color: "rgb(34,68,93)",
                    opacity: 0.1,
                  },
                ]),
              },
            },
            {
              name: "2022",
              data: qjrhl22,
              type: "line",
              lineStyle: {
                color: "rgb(117,251,252)",
              },
              connectNulls: true,
              symbol: "none",
              areaStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {
                    offset: 0,
                    color: "rgb(34,68,93)",
                    opacity: 0,
                  },
                  {
                    offset: 1,
                    color: "rgb(34,68,93)",
                    opacity: 0,
                  },
                ]),
              },
            },
          ],
        };
        this.option6 = {
          backgroundColor: "", //设置无背景色
          title: {
            // text: "(集团)",
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
              // fontSize: 11,
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
              boundaryGap:['10%', '10%'],
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
              data: fxData,
            },
          ],
          series: [
            {
              name: "2022",
              type: "bar",
              stack: "总量",
              barWidth: 10,
              label: {
                show: true,
                position: "left",
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
              data: fcydl2,
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
                position: "right",
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
                formatter: (value) => {
                  // 值都是负数的 所以需要取反一下
                  if (value.data == 0.0) {
                    value.data = 0;
                  }
                  return value.data;
                },
              },
              barWidth: 9,
              data: fcydl1,
              itemStyle: {
                normal: {
                  barBorderRadius: [0, 10, 10, 0],
                  color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [
                    { offset: 0, color: "#00FFCC" },
                    { offset: 1, color: "#143259" },
                  ]),
                },
              },
            }
          ],
        };
        myChart1.setOption(this.option1);
        myChart2.setOption(this.option4);
        myChart5.setOption(this.option5);
        myChart6.setOption(this.option6);
      });
    },
    // 心电图
    getOption7() {
      var myChart1 = echarts.init(document.getElementById("xindian1"), "dark");
      var myChart2 = echarts.init(document.getElementById("xindian2"), "dark");
      var myChart3 = echarts.init(document.getElementById("xindian3"), "dark");
      var myChart4 = echarts.init(document.getElementById("xindian4"), "dark");
      var myChart5 = echarts.init(document.getElementById("duiji"));
      let date7 = [];
      let noxpfl = [];
      let so2pfl = [];
      let dustpfl = [];
      let date8 = [];
      let noxpflname = [];
      let jituanName = [];

      let noxpfl1 = [];
      let noxpfl2 = [];
      let noxpfl3 = [];
      let noxpfl4 = [];
      let noxpfl5 = [];
      let noxpfl6 = [];
      let noxpfl7 = [];
      let noxpfl8 = [];
      let noxpfl9 = [];
      let noxpfl10 = [];
      let noxpfl11 = [];
      let noxpfl12 = [];
      let noxpfl13 = [];
      let noxpfl14 = [];
      let noxpfl15 = [];

      let so2pfl1 = [];
      let so2pfl2 = [];
      let so2pfl3 = [];
      let so2pfl4 = [];
      let so2pfl5 = [];
      let so2pfl6 = [];
      let so2pfl7 = [];
      let so2pfl8 = [];
      let so2pfl9 = [];
      let so2pfl10 = [];
      let so2pfl11 = [];
      let so2pfl12 = [];
      let so2pfl13 = [];
      let so2pfl14 = [];
      let so2pfl15 = [];

      let dustpfl1 = [];
      let dustpfl2 = [];
      let dustpfl3 = [];
      let dustpfl4 = [];
      let dustpfl5 = [];
      let dustpfl6 = [];
      let dustpfl7 = [];
      let dustpfl8 = [];
      let dustpfl9 = [];
      let dustpfl10 = [];
      let dustpfl11 = [];
      let dustpfl12 = [];
      let dustpfl13 = [];
      let dustpfl14 = [];
      let dustpfl15 = [];

      let aaa = [];
      this.$http({
        method: "get",
        url: `/jndpportal/wbjk/getStatRight.xhtml`,
      }).then((res) => {
        // console.log(res.data[0].data[0].JTPFLIST);
        if (res.data[0].res) {
          let resultRight = res.data[0].data[0];
          this.tableData = resultRight.WARNING;
          // 煤机数目
          this.coalMachine = resultRight.JZLX[0].coalMachine;
          // 煤机运行数目
          this.coalMachineFunction = resultRight.JZLX[0].coalMachineFunction;
          this.hpressure = resultRight.JZLX[0].hpressure;
          this.chpressure = resultRight.JZLX[0].chpressure;
          this.rqjz = resultRight.JZLX[0].rqjz;
          this.wnswzjz = resultRight.JZLX[0].wnswzjz;
          this.yrlyjz = resultRight.JZLX[0].yrlyjz;
          this.gasMachine = resultRight.JZLX[0].gasMachine;
          this.gasMachineFunction = resultRight.JZLX[0].gasMachineFunction;
          // 临界
          this.critical = resultRight.JZLX[0].critical;
          // 亚临界
          this.yCritical = resultRight.JZLX[0].yCritical;
          // 超临界
          this.cCritical = resultRight.JZLX[0].cCritical;
          // 超超临界
          this.ccCritical = resultRight.JZLX[0].ccCritical;
          resultRight.WRWPFLIST.map((item, index) => {
            date7.push(item.dates);
            noxpfl.push(Number(item.noxpfl));
            so2pfl.push(Number(item.so2pfl));
            dustpfl.push(Number(item.dustpfl));
          });
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
          resultRight.JTPFLIST.map((item2, index2) => {
            if (item2.JTMC == jituanName[0]) {
              noxpfl1.push(item2.noxpfl);
              so2pfl1.push(item2.so2pfl);
              dustpfl1.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[1]) {
              noxpfl2.push(item2.noxpfl);
              so2pfl2.push(item2.so2pfl);
              dustpfl2.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[2]) {
              noxpfl3.push(item2.noxpfl);
              so2pfl3.push(item2.so2pfl);
              dustpfl3.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[3]) {
              noxpfl4.push(item2.noxpfl);
              so2pfl4.push(item2.so2pfl);
              dustpfl4.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[4]) {
              noxpfl5.push(item2.noxpfl);
              so2pfl5.push(item2.so2pfl);
              dustpfl5.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[5]) {
              noxpfl6.push(item2.noxpfl);
              so2pfl6.push(item2.so2pfl);
              dustpfl6.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[6]) {
              noxpfl7.push(item2.noxpfl);
              so2pfl7.push(item2.so2pfl);
              dustpfl7.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[7]) {
              noxpfl8.push(item2.noxpfl);
              so2pfl8.push(item2.so2pfl);
              dustpfl8.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[8]) {
              noxpfl9.push(item2.noxpfl);
              so2pfl9.push(item2.so2pfl);
              dustpfl9.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[9]) {
              noxpfl10.push(item2.noxpfl);
              so2pfl10.push(item2.so2pfl);
              dustpfl10.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[10]) {
              noxpfl11.push(item2.noxpfl);
              so2pfl11.push(item2.so2pfl);
              dustpfl11.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[11]) {
              noxpfl12.push(item2.noxpfl);
              so2pfl12.push(item2.so2pfl);
              dustpfl12.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[12]) {
              noxpfl13.push(item2.noxpfl);
              so2pfl13.push(item2.so2pfl);
              dustpfl13.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[13]) {
              noxpfl14.push(item2.noxpfl);
              so2pfl14.push(item2.so2pfl);
              dustpfl14.push(item2.dustpfl);
            }
            if (item2.JTMC == jituanName[14]) {
              noxpfl15.push(item2.noxpfl);
              so2pfl15.push(item2.so2pfl);
              dustpfl15.push(item2.dustpfl);
            }
          });

          console.log(noxpfl15);
          console.log();

          // console.log(Object.keys(resultRight.TPFDATA[0]));

          Object.values(resultRight.TPFDATA[0]).map((item, index) => {
            aaa.push({
              name: Object.keys(resultRight.TPFDATA[0])[index],
              data: item,
            });
          });

          this.option7 = {
            backgroundColor: "", //设置无背景色
            tooltip: {
              show: true,
            },
            grid: {
              x: "12%", //x 偏移量
              y: "12%", // y 偏移量
              width: "80%", // 宽度
              height: "60%", // 高度
            },
            legend: {
              x: "right", // 水平居右
              icon: "rect", // 图例icon为方块
              itemHeight: 10, // 图例icon高度
              itemWidth: 10, // 图例icon宽度
              itemGap: 2,
              textStyle: {
                color: "#fff", // 图例文字颜色
                // fontSize: 8,
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
            xAxis: {
              type: "category",
              boundaryGap: false,
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
              data: date7,
            },
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
            dataZoom: [
              {
                type: "slider",
                show: true,
                // height: 12,
                start: 0,
                end: 100,
                borderGap: 0,
                borderColor: "rgb(14,27,65)", //滑动通道的边框颜色
                backgroundColor: "rgb(28,44,61)",
                dataBackground: {
                  lineStyle: {
                    color: "#Fff",
                    // fontSize: 11,
                  },
                },
              },
            ],
            series: [
              {
                name: "SO₂",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#51FDFF",
                },
                areaStyle: {
                  color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    {
                      offset: 0,
                      color: "#51FDFF",
                    },
                    {
                      offset: 1,
                      color: "#071A35",
                    },
                  ]),
                },
                data: so2pfl,
              },
              {
                name: "NOx",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#257BEC ",
                },
                areaStyle: {
                  color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    {
                      offset: 0,
                      color: "#257BEC",
                    },
                    {
                      offset: 1,
                      color: "#071A35",
                    },
                  ]),
                },
                data: noxpfl,
              },
              {
                name: "烟尘",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#1FF7AC",
                },
                areaStyle: {
                  color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    {
                      offset: 0,
                      color: "#1FF75F",
                    },
                    {
                      offset: 1,
                      color: "#071A35",
                    },
                  ]),
                },
                data: dustpfl,
              },
            ],
          };
          this.option7 && myChart1.setOption(this.option7);
          this.option8 = {
            backgroundColor: "", //设置无背景色
            tooltip: {
              show: true,
            },
            grid: {
              x: "12%", //x 偏移量
              y: "12%", // y 偏移量
              width: "80%", // 宽度
              height: "60%", // 高度
            },
            legend: {
              x: "right", // 水平居右
              icon: "rect", // 图例icon为方块
              itemHeight: 10, // 图例icon高度
              itemWidth: 10, // 图例icon宽度
              // itemGap: 2,
              textStyle: {
                color: "#fff", // 图例文字颜色
                // fontSize: 8,
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
            xAxis: {
              type: "category",
              boundaryGap: false,
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
              data: date8,
            },
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
            dataZoom: [
              {
                type: "slider",
                show: true,
                // height: 12,
                start: 0,
                end: 100,
                borderGap: 0,
                borderColor: "rgb(14,27,65)", //滑动通道的边框颜色
                backgroundColor: "rgb(28,44,61)",
                dataBackground: {
                  lineStyle: {
                    color: "#Fff",
                    // fontSize: 11,
                  },
                },
              },
            ],
            series: [
              {
                name: "浙能",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#31CE8B",
                },
                data: so2pfl1,
              },
              {
                name: "国能",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#6C92FF",
                },
                data: so2pfl2,
              },
              {
                name: "华能",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#19C7D0",
                },
                data: so2pfl3,
              },
              {
                name: "大唐",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#B87BFC",
                },
                data: so2pfl4,
              },
              {
                name: "华电",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#E2A467",
                },
                data: so2pfl5,
              },
              {
                name: "华润",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#B87BFC ",
                },
                data: so2pfl6,
              },
              {
                name: "台塑",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#2636E6",
                },
                data: so2pfl7,
              },
              {
                name: "巨化",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#ADFC7B",
                },
                data: so2pfl8,
              },
            ],
          };
          this.option8 && myChart2.setOption(this.option8);
          this.option9 = {
            backgroundColor: "", //设置无背景色
            tooltip: {
              show: true,
            },
            grid: {
              x: "12%", //x 偏移量
              y: "12%", // y 偏移量
              width: "80%", // 宽度
              height: "60%", // 高度
            },
            legend: {
              x: "right", // 水平居右
              icon: "rect", // 图例icon为方块
              itemHeight: 10, // 图例icon高度
              itemWidth: 10, // 图例icon宽度
              // itemGap: 2,
              textStyle: {
                color: "#fff", // 图例文字颜色
                // fontSize: 8,
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
            xAxis: {
              type: "category",
              boundaryGap: false,
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
              data: date8,
            },
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
            dataZoom: [
              {
                type: "slider",
                show: true,
                start: 0,
                // height: 12,
                end: 100,
                borderGap: 0,
                borderColor: "rgb(14,27,65)", //滑动通道的边框颜色
                backgroundColor: "rgb(28,44,61)",
                dataBackground: {
                  lineStyle: {
                    color: "#Fff",
                    // fontSize: 11,
                  },
                },
              },
            ],
            series: [
              {
                name: "浙能",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#31CE8B",
                },
                data: noxpfl1,
              },
              {
                name: "国能",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#6C92FF",
                },
                data: noxpfl2,
              },
              {
                name: "华能",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#19C7D0",
                },
                data: noxpfl3,
              },
              {
                name: "大唐",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#B87BFC",
                },
                data: noxpfl4,
              },
              {
                name: "华电",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#E2A467",
                },
                data: noxpfl5,
              },
              {
                name: "华润",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#B87BFC",
                },
                data: noxpfl6,
              },
              {
                name: "台塑",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#2636E6",
                },
                data: noxpfl7,
              },
              {
                name: "巨化",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#ADFC7B",
                },
                data: noxpfl8,
              },
            ],
          };
          this.option9 && myChart3.setOption(this.option9);
          this.option10 = {
            backgroundColor: "", //设置无背景色
            tooltip: {
              show: true,
            },
            grid: {
              x: "12%", //x 偏移量
              y: "12%", // y 偏移量
              width: "80%", // 宽度
              height: "60%", // 高度
            },
            legend: {
              x: "right", // 水平居右
              icon: "rect", // 图例icon为方块
              itemHeight: 10, // 图例icon高度
              itemWidth: 10, // 图例icon宽度
              // itemGap: 2,
              textStyle: {
                color: "#fff", // 图例文字颜色
                // fontSize: 8,
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
            xAxis: {
              type: "category",
              boundaryGap: false,
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
              data: date8,
            },
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
            dataZoom: [
              {
                type: "slider",
                show: true,
                // height: 12,
                start: 0,
                end: 100,
                borderGap: 0,
                borderColor: "rgb(14,27,65)", //滑动通道的边框颜色
                backgroundColor: "rgb(28,44,61)",
                dataBackground: {
                  lineStyle: {
                    color: "#Fff",
                    // fontSize: 11,
                  },
                },
              },
            ],
            series: [
              {
                name: "浙能",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#31CE8B",
                },
                data: dustpfl1,
              },
              {
                name: "国能",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#6C92FF",
                },
                data: dustpfl2,
              },
              {
                name: "华能",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#19C7D0",
                },
                data: dustpfl3,
              },
              {
                name: "大唐",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#B87BFC",
                },
                data: dustpfl4,
              },
              {
                name: "华电",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#E2A467",
                },
                data: dustpfl5,
              },
              {
                name: "华润",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#B87BFC",
                },
                data: dustpfl6,
              },
              {
                name: "台塑",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#2636E6",
                },
                data: dustpfl7,
              },
              {
                name: "巨化",
                type: "line",
                symbol: "none",
                sampling: "lttb",
                itemStyle: {
                  color: "#ADFC7B",
                },
                data: dustpfl8,
              },
            ],
          };
          this.option10 && myChart4.setOption(this.option10);
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
            itemHeight: 10, // 图例icon高度
            itemWidth: 10, // 图例icon宽度
            // itemGap: 2,
            // x: "right", // 水平居右
            top: "3%",
            // 禁止点击
            selectedMode: false,
          };
          // grid
          const grid = {
            left: "4%",
            right: "3%",
            bottom: "15%",
            containLabel: true,
          };

          // xAxis
          const xAxis = {
            axisTick: { show: false },
            axisLine: { show: false },
            axisLabel: {
              textStyle: {
                color: "#fff",
                // fontSize: 11,
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
                barWidth: 18,
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
                symbolSize: [18, 10],
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

          // 渲染
          const option11 = {
            tooltip,
            xAxis,
            yAxis,
            series,
            grid,
            legend,
            backgroundColor: "",
          };

          myChart5.setOption(option11);
        }
      });
    },
  },
};
</script>
<style scoped lang='less'>
@import url("./sellcontent.less");
</style>