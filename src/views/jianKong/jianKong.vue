<template>
  <div class="main-body">
    <div class="top-search">
      <el-form :model="formInline" class="demo-form-inline">
        <el-form-item>
          集团：
          <div class="search-list">
            <el-select
              v-model="formInline.groupName"
              placeholder="请选择"
              :popper-append-to-body="false"
              @change="getFactoryList"
            >
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
              @change="getOperationDiagram"
            >
              <el-option
                v-for="item in formInline.jzList"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </div>
          图表：
          <div class="search-list">
            <el-select
              v-model="formInline.tubiaoName"
              placeholder="请选择"
              :popper-append-to-body="false"
              @change="getOperationDiagram"
            >
              <el-option
                v-for="item in formInline.tubiaoList"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </div>

          <!-- <div class="btn1" @click="getOperationDiagram">
            <img src="../../assets/btn1.png" alt="" />
          </div> -->
          <!-- <div class="btn2" @click="clickBtn2">
            <img src="../../assets/btn2.png" alt="" />
          </div> -->
        </el-form-item>
      </el-form>
    </div>
    <div class="footer">
      <div class="footer-left">
        <div class="left-top">
          <div class="text1">
            <div
              class="text14dian1"
              @mouseenter="showtext1 = true"
              @mouseleave="showtext1 = false"
            >
              {{ text1 }}
            </div>
            <div class="kuang" v-show="showtext1">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text1desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text1name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text00 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text1time }}</span>
              </div>
            </div>
          </div>
          <div class="text2">
            <div
              class="text14dian1"
              @mouseenter="showtext2 = true"
              @mouseleave="showtext2 = false"
            >
              <span class="text">{{ text2 }}</span>
              <span class="danwei"> t/h</span>
            </div>
            <div class="kuang" v-show="showtext2">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text2desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text2name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text2 }} t/h</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text2time }}</span>
              </div>
            </div>
          </div>
          <div class="text3">
            <div
              class="text14dian1"
              @mouseenter="showtext3 = true"
              @mouseleave="showtext3 = false"
            >
              <span class="text">{{ text3 }}</span>
              <span class="danwei"> ℃</span>
            </div>
            <div class="kuang" v-show="showtext3">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text3desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text3name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text3 }} ℃</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text3time }}</span>
              </div>
            </div>
          </div>
          <div class="text4">
            <div
              class="text14dian1"
              @mouseenter="showtext4 = true"
              @mouseleave="showtext4 = false"
            >
              <span class="text">{{ text4 }}</span>
              <span class="danwei"> MPa</span>
            </div>
            <div class="kuang" v-show="showtext4">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text4desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text4name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text4 }} MPa</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text4time }}</span>
              </div>
            </div>
          </div>
          <div class="text5">
            <div
              class="text14dian1"
              @mouseenter="
                (showtext5 = true), (text6show = false), (text7show = false)
              "
              @mouseleave="
                (showtext5 = false), (text6show = true), (text7show = true)
              "
            >
              <span class="text">{{ text5 }}</span>
              <span class="danwei"> ℃</span>
            </div>

            <div class="kuang" v-show="showtext5" style="margin-left: -300px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text5desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text5name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text5 }} ℃</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text5time }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="left-center">
          <div class="text6" v-show="text6show">
            <div
              class="text14dian1"
              @mouseenter="showtext6 = true"
              @mouseleave="showtext6 = false"
            >
              <span class="text">{{ text6 }}</span>
              <span class="danwei"> mg/dNm3</span>
            </div>
            <div
              class="kuang"
              v-show="showtext6"
              style="margin-left: -200px; width: 550px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text6desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text6name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text6 }} mg/dNm3</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text6time }}</span>
              </div>
            </div>
          </div>
          <div class="text7" v-show="text7show">
            <div
              class="text14dian1"
              @mouseenter="
                (showtext7 = true),
                  (text10show = false),
                  (text11show = false),
                  (text13show = false)
              "
              @mouseleave="
                (showtext7 = false),
                  (text10show = true),
                  (text11show = true),
                  (text13show = true)
              "
            >
              <span class="text">{{ text7 }}</span>
              <span class="danwei"> mg/dNm3</span>
            </div>
            <div
              class="kuang"
              v-show="showtext7"
              style="margin-left: -200px; width: 550px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text7desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text7name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text7 }} mg/dNm3</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text7time }}</span>
              </div>
            </div>
          </div>
          <div class="text8">
            <div
              class="text14dian1"
              @mouseenter="
                (showtext8 = true),
                  (text10show = false),
                  (text11show = false),
                  (text13show = false)
              "
              @mouseleave="
                (showtext8 = false),
                  (text10show = true),
                  (text11show = true),
                  (text13show = true)
              "
            >
              <span class="text">{{ text8 }}</span>
              <span class="danwei"> mg/dNm3</span>
            </div>
            <div
              class="kuang"
              v-show="showtext8"
              style="margin-left: -200px; width: 550px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text8desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text8name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text8 }} mg/dNm3</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text8time }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="left-footer">
          <div class="text9">
            <div
              class="text14dian1"
              @mouseenter="showtext9 = true"
              @mouseleave="showtext9 = false"
            >
              <span class="text">{{ text9 }}</span>
              <span class="danwei"> t/h</span>
            </div>
            <div class="kuang" v-show="showtext9" style="margin-top: -280px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text9desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text9name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text9 }} t/h</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text9time }}</span>
              </div>
            </div>
          </div>
          <div class="text10" v-show="text10show">
            <div
              class="text14dian1"
              @mouseenter="showtext10 = true"
              @mouseleave="showtext10 = false"
            >
              <span class="text">{{ text10 }}</span>
              <span class="danwei"> t/h</span>
            </div>
            <div class="kuang" v-show="showtext10" style="margin-top: -280px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text10desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text10name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text10 }} t/h</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text10time }}</span>
              </div>
            </div>
          </div>
          <div class="text11" v-show="text11show">
            <div
              class="text14dian1"
              @mouseenter="showtext11 = true"
              @mouseleave="showtext11 = false"
            >
              <span class="text">{{ text11 }}</span
              ><span class="danwei">t/h</span>
            </div>
            <div class="kuang" v-show="showtext11" style="margin-top: -280px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text11desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text11name }} </span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text11 }} t/h</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text11time }}</span>
              </div>
            </div>
          </div>
          <div class="text12">
            <div
              class="text14dian1"
              @mouseenter="showtext12 = true"
              @mouseleave="showtext12 = false"
            >
              <span class="text">{{ text12 }}</span>
              <span class="danwei"> t/h</span>
            </div>
            <div class="kuang" v-show="showtext12" style="margin-top: -280px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text12desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text12name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text12 }} t/h</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text12time }}</span>
              </div>
            </div>
          </div>
          <div class="text13" v-show="text13show">
            <div
              class="text14dian1"
              @mouseenter="showtext13 = true"
              @mouseleave="showtext13 = false"
            >
              <span class="text">{{ text13 }}</span>
              <span class="danwei"> kPa</span>
            </div>
            <div class="kuang" v-show="showtext13" style="margin-top: -280px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text13desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text13name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text13 }} kPa</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text13time }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="footer-center">
        <div class="titleaa">{{ titlec }}</div>
        <div class="center1" v-show="tubiaoShow == '1'">
          <div class="text14">
            <div
              class="text14dian"
              @mouseenter="showtext14 = true"
              @mouseleave="showtext14 = false"
            ></div>
            <div class="kuang" v-show="showtext14">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text14desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text14name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text14 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text14time }}</span>
              </div>
            </div>
          </div>
          <div class="text15">
            <div
              class="text14dian"
              @mouseenter="showtext15 = true"
              @mouseleave="showtext15 = false"
            ></div>
            <div class="kuang" v-show="showtext15">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text15desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text15name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text15 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text15time }}</span>
              </div>
            </div>
          </div>
          <div class="text16">
            <div
              class="text14dian"
              @mouseenter="showtext16 = true"
              @mouseleave="showtext16 = false"
            ></div>
            <div class="kuang" v-show="showtext16">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text16desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text16name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text16 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text16time }}</span>
              </div>
            </div>
          </div>
          <div class="text17">
            <div
              class="text14dian"
              @mouseenter="showtext17 = true"
              @mouseleave="showtext17 = false"
            ></div>
            <div class="kuang" v-show="showtext17">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text17desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text17name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text17 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text17time }}</span>
              </div>
            </div>
          </div>
          <div class="text18">
            <div
              class="text14dian"
              @mouseenter="showtext18 = true"
              @mouseleave="showtext18 = false"
            ></div>
            <div class="kuang" v-show="showtext18" style="margin-top: -260px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text18desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text18name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text18 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text18time }}</span>
              </div>
            </div>
          </div>
          <div class="text19">
            <div
              class="text14dian"
              @mouseenter="showtext19 = true"
              @mouseleave="showtext19 = false"
            ></div>
            <div class="kuang" v-show="showtext19" style="margin-top: -260px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text19desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text19name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text19 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text19time }}</span>
              </div>
            </div>
          </div>

          <div class="text20">
            <div
              class="text14dian"
              @mouseenter="showtext20 = true"
              @mouseleave="showtext20 = false"
            ></div>
            <div class="kuang" v-show="showtext20">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text20desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text20name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text20 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text20time }}</span>
              </div>
            </div>
          </div>
          <div class="text21">
            <div
              class="text14dian"
              @mouseenter="showtext21 = true"
              @mouseleave="showtext21 = false"
            ></div>
            <div class="kuang" v-show="showtext21">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text21desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text21name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text21 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text21time }}</span>
              </div>
            </div>
          </div>
          <div class="text22">
            <div
              class="text14dian"
              @mouseenter="showtext22 = true"
              @mouseleave="showtext22 = false"
            ></div>
            <div class="kuang" v-show="showtext22">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text22desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text22name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text22 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text22time }}</span>
              </div>
            </div>
          </div>
          <div class="text23">
            <div
              class="text14dian"
              @mouseenter="showtext23 = true"
              @mouseleave="showtext23 = false"
            ></div>
            <div class="kuang" v-show="showtext23">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text23desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text23name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text23 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text23time }}</span>
              </div>
            </div>
          </div>
          <div class="text24">
            <div
              class="text14dian"
              @mouseenter="showtext24 = true"
              @mouseleave="showtext24 = false"
            ></div>
            <div class="kuang" v-show="showtext24">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text24desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text24name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text24 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text24time }}</span>
              </div>
            </div>
          </div>
          <div class="text25">
            <div
              class="text14dian"
              @mouseenter="showtext25 = true"
              @mouseleave="showtext25 = false"
            ></div>
            <div class="kuang" v-show="showtext25">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text25desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text25name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text25 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text25time }}</span>
              </div>
            </div>
          </div>
          <div class="text00">
            <div
              class="text00dian"
              @mouseenter="showtext00 = true"
              @mouseleave="showtext00 = false"
            ></div>
            <div class="kuang" v-show="showtext00">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text00desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text00name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text00 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text00time }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="center2" v-show="tubiaoShow == '2'">
          <div class="tit-bb tit-1">高加1#</div>
          <div class="tit-bb tit-2">高加2#</div>
          <div class="tit-bb tit-3">高加3#</div>
          <div class="tit-bb tit-4">低加5#</div>
          <div class="tit-bb tit-5">低加6#</div>
          <div class="tit-bb tit-6">低加7#</div>
          <div class="tit-bb tit-7">低加8#</div>
          <div class="text14">
            <div
              class="text14dian1"
              style="width: 150px"
              @mouseenter="showtext14 = true"
              @mouseleave="showtext14 = false"
            >
              {{ text14 }}
            </div>
            <div class="kuang" v-show="showtext14">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text14desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text14name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text14 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text14time }}</span>
              </div>
            </div>
          </div>
          <div class="text15">
            <div
              class="text14dian1"
              style="width: 150px"
              @mouseenter="showtext15 = true"
              @mouseleave="showtext15 = false"
            >
              {{ text15 }}
            </div>
            <div class="kuang" v-show="showtext15">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text15desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text15name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text15 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text15time }}</span>
              </div>
            </div>
          </div>
          <div class="text16">
            <div
              class="text14dian1"
              style="width: 150px"
              @mouseenter="showtext16 = true"
              @mouseleave="showtext16 = false"
            >
              {{ text16 }}
            </div>
            <div class="kuang" v-show="showtext16">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text16desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text16name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text16 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text16time }}</span>
              </div>
            </div>
          </div>
          <div class="text17">
            <div
              class="text14dian1"
              style="width: 150px"
              @mouseenter="showtext17 = true"
              @mouseleave="showtext17 = false"
            >
              {{ text17 }}
            </div>
            <div class="kuang" v-show="showtext17">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text17desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text17name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text17 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text17time }}</span>
              </div>
            </div>
          </div>
          <div class="text00">
            <div
              class="text14dian1"
              style="width: 200px"
              @mouseenter="showtext00 = true"
              @mouseleave="showtext00 = false"
            >
              {{ text00 }}
            </div>
            <div class="kuang" v-show="showtext00" style="margin-left: -300px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text00desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text00name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text00 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text00time }}</span>
              </div>
            </div>
          </div>
          <div class="text18">
            <div
              class="text14dian1"
              style="width: 200px; text-align: left"
              @mouseenter="showtext18 = true"
              @mouseleave="showtext18 = false"
            >
              {{ text18 }}
            </div>
            <div class="kuang" v-show="showtext18" style="margin-left: -300px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text18desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text18name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text18 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text18time }}</span>
              </div>
            </div>
          </div>
          <div class="text19">
            <div
              style="width: 200px"
              class="text14dian1"
              @mouseenter="showtext19 = true"
              @mouseleave="showtext19 = false"
            >
              {{ text19 }}
            </div>
            <div class="kuang" v-show="showtext19">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text19desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text19name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text19 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text19time }}</span>
              </div>
            </div>
          </div>

          <div class="text20">
            <div
              class="text14dian1"
              style="width: 200px"
              @mouseenter="showtext20 = true"
              @mouseleave="showtext20 = false"
            >
              {{ text20 }}
            </div>
            <div class="kuang" v-show="showtext20">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text20desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text20name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text20 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text20time }}</span>
              </div>
            </div>
          </div>
          <div class="text21">
            <div
              class="text14dian1"
              style="width: 100px"
              @mouseenter="showtext21 = true"
              @mouseleave="showtext21 = false"
            >
              {{ text21 }}
            </div>
            <div class="kuang" v-show="showtext21" style="margin-left: -400px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text21desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text21name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text21 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text21time }}</span>
              </div>
            </div>
          </div>
          <div class="text22">
            <div
              class="text14dian1"
              style="width: 100px"
              @mouseenter="showtext22 = true"
              @mouseleave="showtext22 = false"
            >
              {{ text22 }}
            </div>
            <div class="kuang" v-show="showtext22" style="margin-left: -400px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text22desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text22name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text22 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text22time }}</span>
              </div>
            </div>
          </div>
          <div class="text23">
            <div
              class="text14dian1"
              style="width: 100px"
              @mouseenter="showtext23 = true"
              @mouseleave="showtext23 = false"
            >
              {{ text23 }}
            </div>
            <div class="kuang" v-show="showtext23">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text23desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text23name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text23 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text23time }}</span>
              </div>
            </div>
          </div>
          <div class="text24">
            <div
              class="text14dian1"
              style="width: 100px"
              @mouseenter="
                (showtext24 = true),
                  (text44show = false),
                  (text45show = false),
                  (text46show = false)
              "
              @mouseleave="
                (showtext24 = false),
                  (text44show = true),
                  (text45show = true),
                  (text46show = true)
              "
            >
              {{ text24 }}
            </div>
            <div class="kuang" v-show="showtext24" style="margin-left: -100px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text24desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text24name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text24 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text24time }}</span>
              </div>
            </div>
          </div>
          <div class="text25">
            <div
              class="text14dian1"
              style="width: 100px"
              @mouseenter="showtext25 = true"
              @mouseleave="showtext25 = false"
            >
              {{ text25 }}
            </div>
            <div class="kuang" v-show="showtext25">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text25desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text25name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text25 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text25time }}</span>
              </div>
            </div>
          </div>
          <div class="text26">
            <div
              class="text14dian1"
              style="width: 100px"
              @mouseenter="
                (showtext26 = true),
                  (text44show = false),
                  (text45show = false),
                  (text46show = false)
              "
              @mouseleave="
                (showtext26 = false),
                  (text44show = true),
                  (text45show = true),
                  (text46show = true)
              "
            >
              {{ text26 }}
            </div>
            <div class="kuang" v-show="showtext26" style="margin-left: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text26desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text26name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text26 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text26time }}</span>
              </div>
            </div>
          </div>
          <div class="text27">
            <div
              class="text14dian1"
              style="width: 100px"
              @mouseenter="showtext27 = true"
              @mouseleave="showtext27 = false"
            >
              {{ text27 }}
            </div>
            <div class="kuang" v-show="showtext27">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text27desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text27name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text27 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text27time }}</span>
              </div>
            </div>
          </div>
          <div class="text28">
            <div
              class="text14dian1"
              style="width: 100px"
              @mouseenter="
                (showtext28 = true),
                  (text44show = false),
                  (text45show = false),
                  (text46show = false)
              "
              @mouseleave="
                (showtext28 = false),
                  (text44show = true),
                  (text45show = true),
                  (text46show = true)
              "
            >
              {{ text28 }}
            </div>
            <div class="kuang" v-show="showtext28" style="margin-left: -350px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text28desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text28name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text28 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text28time }}</span>
              </div>
            </div>
          </div>
          <div class="text29">
            <div
              class="text14dian1"
              style="width: 200px"
              @mouseenter="showtext29 = true"
              @mouseleave="showtext29 = false"
            >
              {{ text29 }}
            </div>
            <div
              class="kuang"
              v-show="showtext29"
              style="margin-top: -270px; margin-left: -50px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text29desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text29name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text29 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text29time }}</span>
              </div>
            </div>
          </div>
          <div class="text30">
            <div
              class="text14dian1"
              style="width: 200px"
              @mouseenter="showtext30 = true"
              @mouseleave="showtext30 = false"
            >
              {{ text30 }}
            </div>
            <div
              class="kuang"
              v-show="showtext30"
              style="margin-top: -270px; margin-left: -50px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text30desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text30name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text30 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text30time }}</span>
              </div>
            </div>
          </div>
          <div class="text31">
            <div
              class="text14dian1"
              style="width: 200px"
              @mouseenter="showtext31 = true"
              @mouseleave="showtext31 = false"
            >
              {{ text31 }}
            </div>
            <div class="kuang" v-show="showtext31">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text31desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text31name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text31 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text31time }}</span>
              </div>
            </div>
          </div>
          <div class="text32">
            <div
              class="text14dian1"
              style="width: 200px"
              @mouseenter="
                (showtext32 = true),
                  (text48show = false),
                  (text49show = false),
                  (text50show = false),
                  (text51show = false),
                  (text52show = false)
              "
              @mouseleave="
                (showtext32 = false),
                  (text48show = true),
                  (text49show = true),
                  (text50show = true),
                  (text51show = true),
                  (text52show = true)
              "
            >
              {{ text32 }}
            </div>
            <div class="kuang" v-show="showtext32">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text32desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text32name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text32 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text32time }}</span>
              </div>
            </div>
          </div>
          <div class="text33">
            <div
              class="text14dian1"
              style="width: 130px"
              @mouseenter="showtext33 = true"
              @mouseleave="showtext33 = false"
            >
              {{ text33 }}
            </div>
            <div class="kuang" v-show="showtext33">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text33desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text33name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text33 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text33time }}</span>
              </div>
            </div>
          </div>
          <div class="text34">
            <div
              class="text14dian1"
              style="width: 130px"
              @mouseenter="
                (showtext34 = true),
                  (text48show = false),
                  (text49show = false),
                  (text50show = false),
                  (text51show = false),
                  (text52show = false)
              "
              @mouseleave="
                (showtext34 = false),
                  (text48show = true),
                  (text49show = true),
                  (text50show = true),
                  (text51show = true),
                  (text52show = true)
              "
            >
              {{ text34 }}
            </div>
            <div class="kuang" v-show="showtext34">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text34desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text34name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text34 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text34time }}</span>
              </div>
            </div>
          </div>
          <div class="text35">
            <div
              class="text14dian1"
              style="width: 130px"
              @mouseenter="showtext35 = true"
              @mouseleave="showtext35 = false"
            >
              {{ text35 }}
            </div>
            <div class="kuang" v-show="showtext35">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text35desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text35name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text35 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text35time }}</span>
              </div>
            </div>
          </div>
          <div class="text36">
            <div
              class="text14dian1"
              style="width: 130px"
              @mouseenter="
                (showtext36 = true),
                  (text48show = false),
                  (text49show = false),
                  (text50show = false),
                  (text51show = false),
                  (text52show = false)
              "
              @mouseleave="
                (showtext36 = false),
                  (text48show = true),
                  (text49show = true),
                  (text50show = true),
                  (text51show = true),
                  (text52show = true)
              "
            >
              {{ text36 }}
            </div>
            <div class="kuang" v-show="showtext36">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text36desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text36name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text36 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text36time }}</span>
              </div>
            </div>
          </div>
          <div class="text37">
            <div
              class="text14dian1"
              style="width: 130px"
              @mouseenter="showtext37 = true"
              @mouseleave="showtext37 = false"
            >
              {{ text37 }}
            </div>
            <div class="kuang" v-show="showtext37" style="margin-left: -300px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text37desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text37name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text37 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text37time }}</span>
              </div>
            </div>
          </div>
          <div class="text38">
            <div
              class="text14dian1"
              style="width: 130px"
              @mouseenter="
                (showtext38 = true),
                  (text48show = false),
                  (text49show = false),
                  (text50show = false),
                  (text51show = false),
                  (text52show = false)
              "
              @mouseleave="
                (showtext38 = false),
                  (text48show = true),
                  (text49show = true),
                  (text50show = true),
                  (text51show = true),
                  (text52show = true)
              "
            >
              {{ text38 }}
            </div>
            <div class="kuang" v-show="showtext38" style="margin-left: -300px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text38desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text38name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text38 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text38time }}</span>
              </div>
            </div>
          </div>
          <div class="text39">
            <div
              class="text14dian1"
              style="width: 150px; height: 25px; text-align: left"
              @mouseenter="showtext39 = true"
              @mouseleave="showtext39 = false"
            >
              {{ text39 }}
            </div>
            <div class="kuang" v-show="showtext39" style="margin-left: -400px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text39desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text39name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text39 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text39time }}</span>
              </div>
            </div>
          </div>
          <div class="text40">
            <div
              class="text14dian1"
              style="width: 150px; height: 25px; text-align: left"
              @mouseenter="(showtext40 = true), (text41show = false)"
              @mouseleave="(showtext40 = false), (text41show = true)"
            >
              {{ text40 }}
            </div>
            <div class="kuang" v-show="showtext40" style="margin-left: -400px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text40desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text40name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text40 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text40time }}</span>
              </div>
            </div>
          </div>
          <div class="text41" v-show="text41show">
            <div
              class="text14dian1"
              style="width: 80px; text-align: left"
              @mouseenter="showtext41 = true"
              @mouseleave="showtext41 = false"
            >
              {{ text41 }}
            </div>
            <div
              class="kuang"
              v-show="showtext41"
              style="margin-top: -250px; margin-left: -400px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text41desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text41name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text41 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text41time }}</span>
              </div>
            </div>
          </div>
          <div class="text42" v-show="text42show">
            <div
              class="text14dian1"
              style="width: 130px; text-align: center"
              @mouseenter="showtext42 = true"
              @mouseleave="showtext42 = false"
            >
              {{ text42 }}
            </div>
            <div class="kuang" v-show="showtext42" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text42desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text42name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text42 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text42time }}</span>
              </div>
            </div>
          </div>
          <div class="text43">
            <div
              class="text14dian1"
              style="width: 130px; text-align: center"
              @mouseenter="showtext43 = true"
              @mouseleave="showtext43 = false"
            >
              {{ text43 }}
            </div>
            <div class="kuang" v-show="showtext43" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text43desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text43name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text43 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text43time }}</span>
              </div>
            </div>
          </div>
          <div class="text44" v-show="text44show">
            <div
              class="text14dian1"
              style="width: 130px; text-align: center"
              @mouseenter="showtext44 = true"
              @mouseleave="showtext44 = false"
            >
              {{ text44 }}
            </div>
            <div class="kuang" v-show="showtext44" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text44desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text44name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text44 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text44time }}</span>
              </div>
            </div>
          </div>
          <div class="text45" v-show="text45show">
            <div
              class="text14dian1"
              style="width: 130px; text-align: center"
              @mouseenter="showtext45 = true"
              @mouseleave="showtext45 = false"
            >
              {{ text45 }}
            </div>
            <div class="kuang" v-show="showtext45" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text45desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text45name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text45 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text45time }}</span>
              </div>
            </div>
          </div>
          <div class="text46" v-show="text46show">
            <div
              class="text14dian1"
              style="width: 130px; text-align: center"
              @mouseenter="showtext46 = true"
              @mouseleave="showtext46 = false"
            >
              {{ text46 }}
            </div>
            <div class="kuang" v-show="showtext46" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text46desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text46name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text46 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text46time }}</span>
              </div>
            </div>
          </div>
          <div class="text47">
            <div
              class="text14dian1"
              style="width: 130px; text-align: center"
              @mouseenter="(showtext47 = true), (text42show = false)"
              @mouseleave="(showtext47 = false), (text42show = true)"
            >
              {{ text47 }}
            </div>
            <div class="kuang" v-show="showtext47" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text47desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text47name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text47 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text47time }}</span>
              </div>
            </div>
          </div>
          <div class="text48" v-show="text48show">
            <div
              class="text14dian1"
              style="width: 130px; text-align: center"
              @mouseenter="showtext48 = true"
              @mouseleave="showtext48 = false"
            >
              {{ text48 }}
            </div>
            <div class="kuang" v-show="showtext48" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text48desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text48name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text48 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text48time }}</span>
              </div>
            </div>
          </div>
          <div class="text49" v-show="text49show">
            <div
              class="text14dian1"
              style="width: 130px; text-align: center"
              @mouseenter="showtext49 = true"
              @mouseleave="showtext49 = false"
            >
              {{ text49 }}
            </div>
            <div class="kuang" v-show="showtext49" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text49desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text49name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text49 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text49time }}</span>
              </div>
            </div>
          </div>
          <div class="text50" v-show="text50show">
            <div
              class="text14dian1"
              style="width: 130px; text-align: center"
              @mouseenter="showtext50 = true"
              @mouseleave="showtext50 = false"
            >
              {{ text50 }}
            </div>
            <div class="kuang" v-show="showtext50" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text50desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text50name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text50 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text50time }}</span>
              </div>
            </div>
          </div>
          <div class="text51" v-show="text51show">
            <div
              class="text14dian1"
              style="width: 130px; text-align: center"
              @mouseenter="showtext51 = true"
              @mouseleave="showtext51 = false"
            >
              {{ text51 }}
            </div>
            <div
              class="kuang"
              v-show="showtext51"
              style="margin-top: -250px; margin-left: -400px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text51desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text51name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text51 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text51time }}</span>
              </div>
            </div>
          </div>
          <div class="text52" v-show="text52show">
            <div
              class="text14dian1"
              @mouseenter="showtext52 = true"
              @mouseleave="showtext52 = false"
              style="width: 130px; text-align: center"
            >
              {{ text52 }}
            </div>
            <div
              class="kuang"
              v-show="showtext52"
              style="margin-top: -250px; margin-left: -400px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text52desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text52name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text52 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text52time }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="center3" v-show="tubiaoShow == '3'">
          <div class="text14">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext14 = true"
              @mouseleave="showtext14 = false"
            >
              {{ text14 }}
            </div>
            <div class="kuang" v-show="showtext14">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text14desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text14name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text14 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text14time }}</span>
              </div>
            </div>
          </div>
          <div class="text15">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext15 = true"
              @mouseleave="showtext15 = false"
            >
              {{ text15 }}
            </div>
            <div class="kuang" v-show="showtext15">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text15desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text15name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text15 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text15time }}</span>
              </div>
            </div>
          </div>
          <div class="text16">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="(showtext16 = true), (text19show = false)"
              @mouseleave="(showtext16 = false), (text19show = true)"
            >
              {{ text16 }}
            </div>
            <div class="kuang" v-show="showtext16" style="margin-left: -300px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text16desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text16name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text16 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text16time }}</span>
              </div>
            </div>
          </div>
          <div class="text17">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="(showtext17 = true), (text19show = false)"
              @mouseleave="(showtext17 = false), (text19show = true)"
            >
              {{ text17 }}
            </div>
            <div class="kuang" v-show="showtext17" style="margin-left: -450px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text17desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text17name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text17 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text17time }}</span>
              </div>
            </div>
          </div>
          <div class="text18">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext18 = true"
              @mouseleave="showtext18 = false"
            >
              {{ text18 }}
            </div>
            <div
              class="kuang"
              v-show="showtext18"
              style="margin-top: -270px; margin-left: -250px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text18desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text18name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text18 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text18time }}</span>
              </div>
            </div>
          </div>
          <div class="text19" v-show="text19show">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext19 = true"
              @mouseleave="showtext19 = false"
            >
              {{ text19 }}
            </div>
            <div
              class="kuang"
              v-show="showtext19"
              style="margin-top: -270px; margin-left: -250px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text19desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text19name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text19 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text19time }}</span>
              </div>
            </div>
          </div>

          <div class="text20">
            <div
              class="text14dian1"
              style="width: 200px; text-align: left"
              @mouseenter="showtext20 = true"
              @mouseleave="showtext20 = false"
            >
              {{ text20 }}
            </div>
            <div class="kuang" v-show="showtext20">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text20desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text20name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text20 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text20time }}</span>
              </div>
            </div>
          </div>
          <div class="text21">
            <div
              class="text14dian1"
              style="width: 200px; text-align: left"
              @mouseenter="showtext21 = true"
              @mouseleave="showtext21 = false"
            >
              {{ text21 }}
            </div>
            <div class="kuang" v-show="showtext21">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text21desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text21name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text21 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text21time }}</span>
              </div>
            </div>
          </div>
          <div class="text22">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext22 = true"
              @mouseleave="showtext22 = false"
            >
              {{ text22 }}
            </div>
            <div class="kuang" v-show="showtext22" style="margin-left: -200px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text22desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text22name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text22 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text22time }}</span>
              </div>
            </div>
          </div>
          <div class="text23">
            <div
              class="text14dian1"
              style="width: 150px; text-align: left"
              @mouseenter="showtext23 = true"
              @mouseleave="showtext23 = false"
            >
              {{ text23 }}
            </div>
            <div
              class="kuang"
              v-show="showtext23"
              style="margin-top: -250px; margin-left: -350px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text23desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text23name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text23 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text23time }}</span>
              </div>
            </div>
          </div>
          <div class="text24">
            <div
              class="text14dian1"
              style="width: 200px; text-align: left"
              @mouseenter="showtext24 = true"
              @mouseleave="showtext24 = false"
            >
              {{ text24 }}
            </div>
            <div
              class="kuang"
              v-show="showtext24"
              style="
                margin-top: -250px;
                margin-left: -350px;
                margin-right: 100px;
              "
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text24desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text24name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text24 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text24time }}</span>
              </div>
            </div>
          </div>
          <div class="text25">
            <div
              class="text14dian1"
              style="width: 150px; text-align: left"
              @mouseenter="showtext25 = true"
              @mouseleave="showtext25 = false"
            >
              {{ text25 }}
            </div>
            <div
              class="kuang"
              v-show="showtext25"
              style="margin-left: -320px; margin-right: 100px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text25desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text25name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text25 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text25time }}</span>
              </div>
            </div>
          </div>
          <div class="text26">
            <div
              class="text14dian1"
              style="width: 150px"
              @mouseenter="showtext26 = true"
              @mouseleave="showtext26 = false"
            >
              {{ text26 }}
            </div>
            <div
              class="kuang"
              v-show="showtext26"
              style="margin-left: -300px; margin-top: -250px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text26desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text26name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text26 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text26time }}</span>
              </div>
            </div>
          </div>
          <div class="text27">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext27 = true"
              @mouseleave="showtext27 = false"
            >
              {{ text27 }}
            </div>
            <div
              class="kuang"
              v-show="showtext27"
              style="margin-left: -350px; margin-top: -250px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text27desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text27name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text27 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text27time }}</span>
              </div>
            </div>
          </div>
          <div class="text28">
            <div
              class="text14dian1"
              style="height: 30px; width: 200px"
              @mouseenter="showtext28 = true"
              @mouseleave="showtext28 = false"
            >
              {{ text28 }}
            </div>
            <div
              class="kuang"
              v-show="showtext28"
              style="margin-top: -240px; margin-left: -450px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text28desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text28name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text28 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text28time }}</span>
              </div>
            </div>
          </div>
          <div class="text29">
            <div
              class="text14dian1"
              style="height: 30px; width: 200px"
              @mouseenter="showtext29 = true"
              @mouseleave="showtext29 = false"
            >
              {{ text29 }}
            </div>
            <div
              class="kuang"
              v-show="showtext29"
              style="margin-top: -240px; margin-left: -450px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text29desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text29name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text29 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text29time }}</span>
              </div>
            </div>
          </div>
          <div class="text30">
            <div
              class="text14dian1"
              style="height: 30px; width: 200px"
              @mouseenter="showtext30 = true"
              @mouseleave="showtext30 = false"
            >
              {{ text30 }}
            </div>
            <div
              class="kuang"
              v-show="showtext30"
              style="margin-top: -240px; margin-left: -450px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text30desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text30name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text30 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text30time }}</span>
              </div>
            </div>
          </div>
          <div class="text31">
            <div
              class="text14dian1"
              style="height: 30px; width: 200px"
              @mouseenter="showtext31 = true"
              @mouseleave="showtext31 = false"
            >
              {{ text31 }}
            </div>
            <div
              class="kuang"
              v-show="showtext31"
              style="margin-top: -240px; margin-left: -450px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text31desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text31name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text31 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text31time }}</span>
              </div>
            </div>
          </div>
          <div class="text32">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext32 = true"
              @mouseleave="showtext32 = false"
            >
              {{ text32 }}
            </div>
            <div
              class="kuang"
              v-show="showtext32"
              style="margin-top: -250px; margin-left: -200px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text32desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text32name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text32 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text32time }}</span>
              </div>
            </div>
          </div>
          <div class="text33">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext33 = true"
              @mouseleave="showtext33 = false"
            >
              {{ text33 }}
            </div>
            <div
              class="kuang"
              v-show="showtext33"
              style="margin-top: -250px; margin-left: -200px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text33desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text33name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text33 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text33time }}</span>
              </div>
            </div>
          </div>
          <div class="text34">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext34 = true"
              @mouseleave="showtext34 = false"
            >
              {{ text34 }}
            </div>
            <div
              class="kuang"
              v-show="showtext34"
              style="margin-top: -250px; margin-left: -200px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text34desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text34name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text34 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text34time }}</span>
              </div>
            </div>
          </div>
          <div class="text35">
            <div
              class="text14dian1"
              style="width: 200px; text-align: left"
              @mouseenter="(showtext35 = true), text22show"
              @mouseleave="showtext35 = false"
            >
              {{ text35 }}
            </div>
            <div
              class="kuang"
              v-show="showtext35"
              style="margin-top: -250px; margin-left: -50px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text35desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text35name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text35 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text35time }}</span>
              </div>
            </div>
          </div>
          <div class="text36">
            <div
              class="text14dian1"
              style="width: 200px; text-align: left"
              @mouseenter="showtext36 = true"
              @mouseleave="showtext36 = false"
            >
              {{ text36 }}
            </div>
            <div
              class="kuang"
              v-show="showtext36"
              style="margin-top: -250px; margin-left: -50px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text36desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text36name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text36 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text36time }}</span>
              </div>
            </div>
          </div>
          <div class="text37">
            <div
              class="text14dian1"
              style="width: 200px; text-align: left"
              @mouseenter="showtext37 = true"
              @mouseleave="showtext37 = false"
            >
              {{ text37 }}
            </div>
            <div
              class="kuang"
              v-show="showtext37"
              style="margin-top: -250px; margin-left: -50px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text37desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text37name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text37 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text37time }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="center4" v-show="tubiaoShow == '4'">
          <div class="text14">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext14 = true"
              @mouseleave="showtext14 = false"
            >
              {{ text14 }}
            </div>
            <div class="kuang" v-show="showtext14">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text14desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text14name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text14 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text14time }}</span>
              </div>
            </div>
          </div>
          <div class="text15">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext15 = true"
              @mouseleave="showtext15 = false"
            >
              {{ text15 }}
            </div>
            <div class="kuang" v-show="showtext15">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text15desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text15name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text15 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text15time }}</span>
              </div>
            </div>
          </div>
          <div class="text16">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext16 = true"
              @mouseleave="showtext16 = false"
            >
              {{ text16 }}
            </div>
            <div class="kuang" v-show="showtext16">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text16desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text16name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text16 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text16time }}</span>
              </div>
            </div>
          </div>
          <div class="text17">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext17 = true"
              @mouseleave="showtext17 = false"
            >
              {{ text17 }}
            </div>
            <div class="kuang" v-show="showtext17">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text17desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text17name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text17 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text17time }}</span>
              </div>
            </div>
          </div>
          <div class="text18">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext18 = true"
              @mouseleave="showtext18 = false"
            >
              {{ text18 }}
            </div>
            <div class="kuang" v-show="showtext18">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text18desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text18name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text18 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text18time }}</span>
              </div>
            </div>
          </div>
          <div class="text19">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext19 = true"
              @mouseleave="showtext19 = false"
            >
              {{ text19 }}
            </div>
            <div class="kuang" v-show="showtext19">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text19desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text19name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text19 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text19time }}</span>
              </div>
            </div>
          </div>
          <div class="text20">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext20 = true"
              @mouseleave="showtext20 = false"
            >
              {{ text20 }}
            </div>
            <div class="kuang" v-show="showtext20">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text20desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text20name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text20 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text20time }}</span>
              </div>
            </div>
          </div>
          <div class="text21">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext21 = true"
              @mouseleave="showtext21 = false"
            >
              {{ text21 }}
            </div>
            <div
              class="kuang"
              v-show="showtext21"
              style="
                margin-right: 100px;
                margin-left: -350px;
                margin-top: -250px;
              "
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text21desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text21name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text21 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text21time }}</span>
              </div>
            </div>
          </div>
          <div class="text22">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext22 = true"
              @mouseleave="showtext22 = false"
            >
              {{ text22 }}
            </div>
            <div
              class="kuang"
              v-show="showtext22"
              style="
                margin-right: 100px;
                margin-left: -350px;
                margin-top: -250px;
              "
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text22desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text22name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text22 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text22time }}</span>
              </div>
            </div>
          </div>
          <div class="text23">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext23 = true"
              @mouseleave="showtext23 = false"
            >
              {{ text23 }}
            </div>
            <div
              class="kuang"
              v-show="showtext23"
              style="
                margin-top: -250px;
                margin-left: -350px;
                margin-right: 100px;
              "
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text23desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text23name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text23 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text23time }}</span>
              </div>
            </div>
          </div>
          <div class="text24">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext24 = true"
              @mouseleave="showtext24 = false"
            >
              {{ text24 }}
            </div>
            <div
              class="kuang"
              v-show="showtext24"
              style="margin-top: -250px; margin-left: -200px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text24desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text24name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text24 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text24time }}</span>
              </div>
            </div>
          </div>
          <div class="text25">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext25 = true"
              @mouseleave="showtext25 = false"
            >
              {{ text25 }}
            </div>
            <div
              class="kuang"
              v-show="showtext25"
              style="margin-left: -320px; margin-top: -250px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text25desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text25name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text25 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text25time }}</span>
              </div>
            </div>
          </div>
          <div class="text26">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext26 = true"
              @mouseleave="showtext26 = false"
            >
              {{ text26 }}
            </div>
            <div
              class="kuang"
              v-show="showtext26"
              style="margin-left: -300px; margin-top: -250px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text26desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text26name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text26 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text26time }}</span>
              </div>
            </div>
          </div>
          <div class="text27">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext27 = true"
              @mouseleave="showtext27 = false"
            >
              {{ text27 }}
            </div>
            <div
              class="kuang"
              v-show="showtext27"
              style="margin-left: -350px; margin-top: -250px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text27desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text27name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text27 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text27time }}</span>
              </div>
            </div>
          </div>
          <div class="text28">
            <div
              class="text14dian1"
              style="height: 30px; width: 200px"
              @mouseenter="showtext28 = true"
              @mouseleave="showtext28 = false"
            >
              {{ text28 }}
            </div>
            <div
              class="kuang"
              v-show="showtext28"
              style="margin-top: -240px; margin-left: -450px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text28desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text28name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text28 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text28time }}</span>
              </div>
            </div>
          </div>
          <div class="text29">
            <div
              class="text14dian1"
              style="height: 30px; width: 200px"
              @mouseenter="showtext29 = true"
              @mouseleave="showtext29 = false"
            >
              {{ text29 }}
            </div>
            <div
              class="kuang"
              v-show="showtext29"
              style="margin-top: -240px; margin-left: -450px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text29desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text29name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text29 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text29time }}</span>
              </div>
            </div>
          </div>
          <div class="text30">
            <div
              class="text14dian1"
              style="height: 30px; width: 200px"
              @mouseenter="showtext30 = true"
              @mouseleave="showtext30 = false"
            >
              {{ text30 }}
            </div>
            <div
              class="kuang"
              v-show="showtext30"
              style="margin-top: -240px; margin-left: -450px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text30desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text30name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text30 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text30time }}</span>
              </div>
            </div>
          </div>
          <div class="text31">
            <div
              class="text14dian1"
              style="height: 30px; width: 200px"
              @mouseenter="showtext31 = true"
              @mouseleave="showtext31 = false"
            >
              {{ text31 }}
            </div>
            <div
              class="kuang"
              v-show="showtext31"
              style="margin-top: -240px; margin-left: -450px"
            >
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text31desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text31name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text31 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text31time }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="center5" v-show="tubiaoShow == '5'">
          <div class="text14">
            <div
              class="text14dian1"
              style="width: 200px; text-align: right"
              @mouseenter="showtext14 = true"
              @mouseleave="showtext14 = false"
            >
              {{ text14 }}
            </div>
            <div class="kuang" v-show="showtext14" style="margin-left: -300px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text14desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text14name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text14 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text14time }}</span>
              </div>
            </div>
          </div>
          <div class="text15">
            <div
              class="text14dian1"
              style="width: 200px; text-align: left"
              @mouseenter="showtext15 = true"
              @mouseleave="showtext15 = false"
            >
              {{ text15 }}
            </div>
            <div class="kuang" v-show="showtext15">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text15desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text15name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text15 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text15time }}</span>
              </div>
            </div>
          </div>
          <div class="text16">
            <div
              class="text14dian1"
              style="width: 200px; text-align: left"
              @mouseenter="showtext16 = true"
              @mouseleave="showtext16 = false"
            >
              {{ text16 }}
            </div>
            <div class="kuang" v-show="showtext16">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text16desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text16name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text16 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text16time }}</span>
              </div>
            </div>
          </div>
          <div class="text17">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext17 = true"
              @mouseleave="showtext17 = false"
            >
              {{ text17 }}
            </div>
            <div class="kuang" v-show="showtext17" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text17desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text17name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text17 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text17time }}</span>
              </div>
            </div>
          </div>
          <div class="text18">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext18 = true"
              @mouseleave="showtext18 = false"
            >
              {{ text18 }}
            </div>
            <div class="kuang" v-show="showtext18" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text18desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text18name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text18 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text18time }}</span>
              </div>
            </div>
          </div>
          <div class="text19">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext19 = true"
              @mouseleave="showtext19 = false"
            >
              {{ text19 }}
            </div>
            <div class="kuang" v-show="showtext19" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text19desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text19name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text19 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text19time }}</span>
              </div>
            </div>
          </div>
          <div class="text20">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext20 = true"
              @mouseleave="showtext20 = false"
            >
              {{ text20 }}
            </div>
            <div class="kuang" v-show="showtext20" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text20desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text20name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text20 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text20time }}</span>
              </div>
            </div>
          </div>
          <div class="text21">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext21 = true"
              @mouseleave="showtext21 = false"
            >
              {{ text21 }}
            </div>
            <div class="kuang" v-show="showtext21" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text21desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text21name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text21 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text21time }}</span>
              </div>
            </div>
          </div>
          <div class="text22">
            <div
              class="text14dian1"
              style="width: 200px; text-align: center"
              @mouseenter="showtext22 = true"
              @mouseleave="showtext22 = false"
            >
              {{ text22 }}
            </div>
            <div class="kuang" v-show="showtext22" style="margin-top: -250px">
              <!-- <div class="kuang1" style="padding-left: 25px">
                备注: <span style="color: #00faf9"> {{ text22desc }}</span>
              </div> -->
              <div class="kuang1">
                测点名: <span style="color: #00faf9"> {{ text22name }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                数值: <span style="color: #00faf9"> {{ text22 }}</span>
              </div>
              <div class="kuang1" style="padding-left: 25px">
                时间: <span style="color: #00faf9"> {{ text22time }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="footer-right">
        <div class="right-biao">
          <!-- <div class="titleaa">脱硫脱硝投用情况</div> -->
          <div class="right1">
            <span class="right1name">额定功率</span>
            <span class="rightshu"
              >{{ shuju6 }} <span class="rightdan"> MW</span></span
            >
          </div>
          <div class="right2">
            <span class="right1name">负荷率</span>
            <span class="rightshu"
              >{{ shuju5 }} <span class="rightdan"> %</span></span
            >
          </div>
          <div class="right3">
            <span class="right1name">供电煤耗</span>
            <span class="rightshu"
              >{{ shuju4 }} <span class="rightdan"> g/kWh</span></span
            >
          </div>
          <div class="right4">
            <span class="right1name">锅炉热效率</span>
            <span class="rightshu"
              >{{ shuju3 }} <span class="rightdan"> %</span></span
            >
          </div>
          <div class="right5">
            <span class="right1name">汽机热耗率</span>
            <span class="rightshu"
              >{{ shuju2 }} <span class="rightdan"> kJ/kWh</span></span
            >
          </div>
          <div class="right6">
            <span class="right1name">厂用电率</span>
            <span class="rightshu"
              >{{ shuju1 }} <span class="rightdan">%</span></span
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      showtext1: false,
      showtext2: false,
      showtext3: false,
      showtext4: false,
      showtext5: false,
      showtext6: false,
      showtext7: false,
      showtext8: false,
      showtext9: false,
      showtext10: false,
      showtext11: false,
      showtext12: false,
      showtext13: false,
      text22show: true,
      text19show: true,
      text41show: true,
      text42show: true,
      text44show: true,
      text45show: true,
      text46show: true,
      text48show: true,
      text49show: true,
      text50show: true,
      text51show: true,
      text52show: true,
      text6show: true,
      text7show: true,
      text10show: true,
      text11show: true,
      text13show: true,
      tubiaoShow: 1,
      titlec: "",
      shuju1name: "",
      shuju1: "",
      shuju1dan: "",

      shuju2name: "",
      shuju2: "",
      shuju2dan: "",
      shuju3name: "",
      shuju3: "",
      shuju3dan: "",
      shuju4name: "",
      shuju4: "",
      shuju4dan: "",
      shuju5name: "",
      shuju5: "",
      shuju5dan: "",
      shuju6name: "",
      shuju6: "",
      shuju6dan: "",
      showtext00: false,
      showtext14: false,
      showtext15: false,
      showtext16: false,
      showtext17: false,
      showtext18: false,
      showtext19: false,
      showtext20: false,
      showtext21: false,
      showtext22: false,
      showtext23: false,
      showtext24: false,
      showtext25: false,
      showtext26: false,
      showtext27: false,
      showtext28: false,
      showtext29: false,
      showtext30: false,
      showtext31: false,
      showtext32: false,
      showtext33: false,
      showtext34: false,
      showtext35: false,
      showtext36: false,
      showtext37: false,
      showtext38: false,
      showtext39: false,
      showtext40: false,
      showtext41: false,
      showtext42: false,
      showtext43: false,
      showtext44: false,
      showtext45: false,
      showtext46: false,
      showtext47: false,
      showtext48: false,
      showtext49: false,
      showtext50: false,
      showtext51: false,
      showtext52: false,

      text1: 0,
      text1name: "",
      text1time: "",
      text1desc: "",

      text2: 0,
      text2name: "",
      text2time: "",
      text2desc: "",

      text3: 0,
      text3name: "",
      text3time: "",
      text3desc: "",

      text4: 0,
      text4name: "",
      text4time: "",
      text4desc: "",

      text5: 0,
      text5name: "",
      text5time: "",
      text5desc: "",

      text6: 0,
      text6name: "",
      text6time: "",
      text6desc: "",

      text7: 0,
      text7name: "",
      text7time: "",
      text7desc: "",

      text8: 0,
      text8name: "",
      text8time: "",
      text8desc: "",

      text9: 0,
      text9name: "",
      text9time: "",
      text9desc: "",

      text10: 0,
      text10name: "",
      text10time: "",
      text10desc: "",

      text11: 0,
      text11name: "",
      text11time: "",
      text11desc: "",

      text12: 0,
      text12name: "",
      text12time: "",
      text12desc: "",

      text13: 0,
      text13name: "",
      text13time: "",
      text13desc: "",

      text14: 0,
      text14name: "",
      text14time: "",
      text14desc: "",

      text15: 0,
      text15name: "",
      text15time: "",
      text15desc: "",

      text16: 0,
      text16name: "",
      text16time: "",
      text16desc: "",

      text17name: "",
      text17time: "",
      text17: 0,
      text17desc: "",

      text18name: "",
      text18time: "",
      text18: 0,
      text18desc: "",

      text19name: "",
      text19time: "",
      text19: 0,
      text19desc: "",

      text20name: "",
      text20time: "",
      text20: 0,
      text20desc: "",

      text21name: "",
      text21time: "",
      text21: 0,
      text21desc: "",

      text22name: "",
      text22time: "",
      text22: 0,
      text22desc: "",

      text23name: "",
      text23time: "",
      text23: 0,
      text23desc: "",

      text24name: "",
      text24time: "",
      text24: 0,
      text24desc: "",

      text25name: "",
      text25time: "",
      text25: 0,
      text25desc: "",

      text26name: "",
      text26time: "",
      text26: 0,
      text26desc: "",

      text27name: "",
      text27time: "",
      text27: 0,
      text27desc: "",

      text28name: "",
      text28time: "",
      text28: 0,
      text28desc: "",

      text29name: "",
      text29time: "",
      text29: 0,
      text29desc: "",

      text30name: "",
      text30time: "",
      text30: 0,
      text30desc: "",

      text31name: "",
      text31time: "",
      text31: 0,
      text31desc: "",

      text32name: "",
      text32time: "",
      text32: 0,
      text32desc: "",

      text33name: "",
      text33time: "",
      text33: 0,
      text33desc: "",

      text34name: "",
      text34time: "",
      text34: 0,
      text34desc: "",

      text35name: "",
      text35time: "",
      text35: 0,
      text35desc: "",

      text36name: "",
      text36time: "",
      text36: 0,
      text36desc: "",

      text37name: "",
      text37time: "",
      text37: 0,
      text37desc: "",

      text38name: "",
      text38time: "",
      text38: 0,
      text38desc: "",

      text39name: "",
      text39time: "",
      text39: 0,
      text39desc: "",

      text40name: "",
      text40time: "",
      text40: 0,
      text40desc: "",

      text41name: "",
      text41time: "",
      text41: 0,
      text41desc: "",

      text42name: "",
      text42time: "",
      text42: 0,
      text42desc: "",

      text43name: "",
      text43time: "",
      text43: 0,
      text43desc: "",

      text44name: "",
      text44time: "",
      text44: 0,
      text44desc: "",

      text45name: "",
      text45time: "",
      text45: 0,
      text45desc: "",

      text46name: "",
      text46time: "",
      text46: 0,
      text46desc: "",

      text47name: "",
      text47time: "",
      text47: 0,
      text47desc: "",

      text48name: "",
      text48time: "",
      text48: 0,
      text48desc: "",

      text49name: "",
      text49time: "",
      text49: 0,
      text49desc: "",

      text50name: "",
      text50time: "",
      text50: 0,
      text50desc: "",

      text51name: "",
      text51time: "",
      text51: 0,
      text51desc: "",

      text52name: "",
      text52time: "",
      text52: 0,
      text52desc: "",

      text00name: "",
      text00time: "",
      text00: 0,
      text00desc: "",

      tableData: [],
      // 默认显示第几页
      currentPage: 1,
      // 总条数，根据接口获取数据长度(注意：这里不能为空)
      totalCount: 1,
      // 个数选择器（可修改）
      pageSize: 10,
      formInline: {
        groupName: "6",
        factoryName: "",
        jzName: "",
        tubiaoName: "1",
        groupList: [],
        factoryList: [],
        jzList: [],
        tubiaoList: [
          {
            id: "1",
            name: "机组总图",
          },
          {
            id: "2",
            name: "汽轮机图",
          },
          {
            id: "3",
            name: "锅炉图",
          },
          {
            id: "4",
            name: "烟气处理图",
          },
          {
            id: "5",
            name: "电气总图",
          },
        ],
      },
    };
  },
  mounted() {
    this.$nextTick(function () {
      this.getGroupList();
      this.getOperationDiagram();
      let timeTicket;
      clearInterval(timeTicket);
      timeTicket = window.setInterval(() => {
        this.getOperationDiagram();
      }, 60000);
    });
  },
  methods: {
    enter() {
      console.log("2222");
    },
    getOperationDiagram() {
      this.text1 = 0;
      this.text1name = "";
      this.text1time = "";
      this.text1desc = "";

      this.text2 = 0;
      this.text2name = "";
      this.text2time = "";
      this.text2desc = "";

      this.text3 = 0;
      this.text3name = "";
      this.text3time = "";
      this.text3desc = "";

      this.text4 = 0;
      this.text4name = "";
      this.text4time = "";
      this.text4desc = "";

      this.text5 = 0;
      this.text5name = "";
      this.text5time = "";
      this.text5desc = "";

      this.text6 = 0;
      this.text6name = "";
      this.text6time = "";
      this.text6desc = "";

      this.text7 = 0;
      this.text7name = "";
      this.text7time = "";
      this.text7desc = "";

      this.text8 = 0;
      this.text8name = "";
      this.text8time = "";
      this.text8desc = "";

      this.text9 = 0;
      this.text9name = "";
      this.text9time = "";
      this.text9desc = "";

      this.text10 = 0;
      this.text10name = "";
      this.text10time = "";
      this.text10desc = "";

      this.text11 = 0;
      this.text11name = "";
      this.text11time = "";
      this.text11desc = "";

      this.text12 = 0;
      this.text12name = "";
      this.text12time = "";
      this.text12desc = "";

      this.text13 = 0;
      this.text13name = "";
      this.text13time = "";
      this.text13desc = "";

      this.text14 = 0;
      this.text14name = "";
      this.text14time = "";
      this.text14desc = "";

      this.text15 = 0;
      this.text15name = "";
      this.text15time = "";
      this.text15desc = "";

      this.text16 = 0;
      this.text16name = "";
      this.text16time = "";
      this.text16desc = "";

      this.text17name = "";
      this.text17time = "";
      this.text17 = 0;
      this.text17desc = "";

      this.text18name = "";
      this.text18time = "";
      this.text18 = 0;
      this.text18desc = "";

      this.text19name = "";
      this.text19time = "";
      this.text19 = 0;
      this.text19desc = "";

      this.text20name = "";
      this.text20time = "";
      this.text20 = 0;
      this.text20desc = "";

      this.text21name = "";
      this.text21time = "";
      this.text21 = 0;
      this.text21desc = "";

      this.text22name = "";
      this.text22time = "";
      this.text22 = 0;
      this.text22desc = "";

      this.text23name = "";
      this.text23time = "";
      this.text23 = 0;
      this.text23desc = "";

      this.text24name = "";
      this.text24time = "";
      this.text24 = 0;
      this.text24desc = "";

      this.text25name = "";
      this.text25time = "";
      this.text25 = 0;
      this.text25desc = "";

      this.text26name = "";
      this.text26time = "";
      this.text26 = 0;
      this.text26desc = "";

      this.text27name = "";
      this.text27time = "";
      this.text27 = 0;
      this.text27desc = "";

      this.text28name = "";
      this.text28time = "";
      this.text28 = 0;
      this.text28desc = "";

      this.text29name = "";
      this.text29time = "";
      this.text29 = 0;
      this.text29desc = "";

      this.text30name = "";
      this.text30time = "";
      this.text30 = 0;
      this.text30desc = "";

      this.text31name = "";
      this.text31time = "";
      this.text31 = 0;
      this.text31desc = "";

      this.text32name = "";
      this.text32time = "";
      this.text32 = 0;
      this.text32desc = "";

      this.text33name = "";
      this.text33time = "";
      this.text33 = 0;
      this.text33desc = "";

      this.text34name = "";
      this.text34time = "";
      this.text34 = 0;
      this.text34desc = "";

      this.text35name = "";
      this.text35time = "";
      this.text35 = 0;
      this.text35desc = "";

      this.text36name = "";
      this.text36time = "";
      this.text36 = 0;
      this.text36desc = "";

      this.text37name = "";
      this.text37time = "";
      this.text37 = 0;
      this.text37desc = "";

      this.text38name = "";
      this.text38time = "";
      this.text38 = 0;
      this.text38desc = "";

      this.text39name = "";
      this.text39time = "";
      this.text39 = 0;
      this.text39desc = "";

      this.text40name = "";
      this.text40time = "";
      this.text40 = 0;
      this.text40desc = "";

      this.text41name = "";
      this.text41time = "";
      this.text41 = 0;
      this.text41desc = "";

      this.text42name = "";
      this.text42time = "";
      this.text42 = 0;
      this.text42desc = "";

      this.text43name = "";
      this.text43time = "";
      this.text43 = 0;
      this.text43desc = "";

      this.text44name = "";
      this.text44time = "";
      this.text44 = 0;
      this.text44desc = "";

      this.text45name = "";
      this.text45time = "";
      this.text45 = 0;
      this.text45desc = "";

      this.text46name = "";
      this.text46time = "";
      this.text46 = 0;
      this.text46desc = "";

      this.text47name = "";
      this.text47time = "";
      this.text47 = 0;
      this.text47desc = "";

      this.text48name = "";
      this.text48time = "";
      this.text48 = 0;
      this.text48desc = "";

      this.text49name = "";
      this.text49time = "";
      this.text49 = 0;
      this.text49desc = "";

      this.text50name = "";
      this.text50time = "";
      this.text50 = 0;
      this.text50desc = "";

      this.text51name = "";
      this.text51time = "";
      this.text51 = 0;
      this.text51desc = "";

      this.text52name = "";
      this.text52time = "";
      this.text52 = 0;
      this.text52desc = "";

      this.text00name = "";
      this.text00time = "";
      this.text00 = 0;
      this.text00desc = "";
      this.tubiaoShow = this.formInline.tubiaoName;
      let param = {
        groupid: this.formInline.groupName,
        factoryid: this.formInline.factoryName,
        jzbh: this.formInline.jzName,
        diagramType: this.formInline.tubiaoName,
      };
      let result = [];
      this.titlec = "";
      let changdu = 0;
      this.$http({
        method: "get",
        url: `jndpportal/wbjk/getOperationDiagram.xhtml`,
        params: param,
      }).then((res) => {
        if (res.data[0].res) {
          result = res.data[0].data[0].DataList;
          this.titlec = res.data[0].data[0].TITLE;
          changdu = result.length;
          this.shuju1 = result[changdu - 1].value;
          this.shuju1name = result[changdu - 1].name.substring(
            result[changdu - 1].name.lastIndexOf("U1_") + 3,
            result[changdu - 1].name.length
          );
          this.shuju1dan = result[changdu - 1].unit;

          this.shuju2 = result[changdu - 2].value;
          this.shuju2name = result[changdu - 2].name.substring(
            result[changdu - 2].name.lastIndexOf("U1_") + 3,
            result[changdu - 2].name.length
          );
          this.shuju2dan = result[changdu - 2].unit;

          this.shuju3 = result[changdu - 3].value;
          this.shuju3name = result[changdu - 3].name.substring(
            result[changdu - 3].name.lastIndexOf("U1_") + 3,
            result[changdu - 3].name.length
          );
          this.shuju3dan = result[changdu - 3].unit;

          this.shuju4 = result[changdu - 4].value;
          this.shuju4name = result[changdu - 4].name.substring(
            result[changdu - 4].name.lastIndexOf("U1_") + 3,
            result[changdu - 4].name.length
          );
          this.shuju4dan = result[changdu - 4].unit;

          this.shuju5 = result[changdu - 5].value;
          this.shuju5name = result[changdu - 5].name.substring(
            result[changdu - 5].name.lastIndexOf("U1_") + 3,
            result[changdu - 5].name.length
          );
          this.shuju5dan = result[changdu - 5].unit;

          this.shuju6 = result[changdu - 6].value;
          this.shuju6name = result[changdu - 6].name.substring(
            result[changdu - 6].name.lastIndexOf("U1_") + 3,
            result[changdu - 6].name.length
          );
          this.shuju6dan = result[changdu - 6].unit;
          this.text1 = result[0].value;
          this.text1name = result[0].name;
          this.text1time = result[0].time;
          this.text1desc = result[0].desc;

          this.text2 = result[1].value;
          this.text2name = result[1].name;
          this.text2time = result[1].time;
          this.text2desc = result[1].desc;

          this.text3 = result[2].value;
          this.text3name = result[2].name;
          this.text3time = result[2].time;
          this.text3desc = result[2].desc;

          this.text4 = result[3].value;
          this.text4name = result[3].name;
          this.text4time = result[3].time;
          this.text4desc = result[3].desc;

          this.text5 = result[4].value;
          this.text5name = result[4].name;
          this.text5time = result[4].time;
          this.text5desc = result[4].desc;

          this.text6 = result[5].value;
          this.text6name = result[5].name;
          this.text6time = result[5].time;
          this.text6desc = result[5].desc;

          this.text7 = result[6].value;
          this.text7name = result[6].name;
          this.text7time = result[6].time;
          this.text7desc = result[6].desc;

          this.text8 = result[7].value;
          this.text8name = result[7].name;
          this.text8time = result[7].time;
          this.text8desc = result[7].desc;

          this.text9 = result[8].value;
          this.text9name = result[8].name;
          this.text9time = result[8].time;
          this.text9desc = result[8].desc;

          this.text10 = result[9].value;
          this.text10name = result[9].name;
          this.text10time = result[9].time;
          this.text10desc = result[9].desc;

          this.text11 = result[10].value;
          this.text11name = result[10].name;
          this.text11time = result[10].time;
          this.text11desc = result[10].desc;

          this.text12 = result[11].value;
          this.text12name = result[11].name;
          this.text12time = result[11].time;
          this.text12desc = result[11].desc;

          this.text13 = result[12].value;
          this.text13name = result[12].name;
          this.text13time = result[12].time;
          this.text13desc = result[12].desc;

          this.text00 = result[0].value + " " + result[0].unit;
          this.text00name = result[0].name;
          this.text00time = result[0].time;
          this.text00desc = result[0].desc;

          this.text14 = result[13].value + " " + result[13].unit;
          this.text14name = result[13].name;
          this.text14time = result[13].time;
          this.text14desc = result[13].desc;

          this.text15 = result[14].value + " " + result[14].unit;
          this.text15name = result[14].name;
          this.text15time = result[14].time;
          this.text15desc = result[14].desc;

          this.text16 = result[15].value + " " + result[15].unit;
          this.text16name = result[15].name;
          this.text16time = result[15].time;
          this.text16desc = result[15].desc;

          this.text17 = result[16].value + " " + result[16].unit;
          this.text17name = result[16].name;
          this.text17time = result[16].time;
          this.text17desc = result[16].desc;

          this.text18 = result[17].value + " " + result[17].unit;
          this.text18name = result[17].name;
          this.text18time = result[17].time;
          this.text18desc = result[17].desc;

          this.text19 = result[18].value + " " + result[18].unit;
          this.text19name = result[18].name;
          this.text19time = result[18].time;
          this.text19desc = result[18].desc;

          this.text20 = result[19].value + " " + result[19].unit;
          this.text20name = result[19].name;
          this.text20time = result[19].time;
          this.text20desc = result[19].desc;

          this.text21 = result[20].value + " " + result[20].unit;
          this.text21name = result[20].name;
          this.text21time = result[20].time;
          this.text21desc = result[20].desc;

          this.text22 = result[21].value + " " + result[21].unit;
          this.text22name = result[21].name;
          this.text22time = result[21].time;
          this.text22desc = result[21].desc;

          this.text23 = result[22].value + " " + result[22].unit;
          this.text23name = result[22].name;
          this.text23time = result[22].time;
          this.text23desc = result[22].desc;

          if (result[23]) {
            this.text24 = result[23].value + " " + result[23].unit;
            this.text24name = result[23].name;
            this.text24time = result[23].time;
            this.text24desc = result[23].desc;
          }

          if (result[24]) {
            this.text25 = result[24].value + " " + result[24].unit;
            this.text25name = result[24].name;
            this.text25time = result[24].time;
            this.text25desc = result[24].desc;
          }

          if (result[25]) {
            this.text26 = result[25].value + " " + result[25].unit;
            this.text26name = result[25].name;
            this.text26time = result[25].time;
            this.text26desc = result[25].desc;
          }

          if (result[26]) {
            this.text27 = result[26].value + " " + result[26].unit;
            this.text27name = result[26].name;
            this.text27time = result[26].time;
            this.text27desc = result[26].desc;
          }

          if (result[27]) {
            this.text28 = result[27].value + " " + result[27].unit;
            this.text28name = result[27].name;
            this.text28time = result[27].time;
            this.text28desc = result[27].desc;
          }

          if (result[28]) {
            this.text29 = result[28].value + " " + result[28].unit;
            this.text29name = result[28].name;
            this.text29time = result[28].time;
            this.text29desc = result[28].desc;
          }

          if (result[29]) {
            this.text30 = result[29].value + " " + result[29].unit;
            this.text30name = result[29].name;
            this.text30time = result[29].time;
            this.text30desc = result[29].desc;
          }

          if (result[30]) {
            this.text31 = result[30].value + " " + result[30].unit;
            this.text31name = result[30].name;
            this.text31time = result[30].time;
            this.text31desc = result[30].desc;
          }

          if (result[31]) {
            this.text32 = result[31].value + " " + result[31].unit;
            this.text32name = result[31].name;
            this.text32time = result[31].time;
            this.text32desc = result[31].desc;
          }

          if (result[32]) {
            this.text33 = result[32].value + " " + result[32].unit;
            this.text33name = result[32].name;
            this.text33time = result[32].time;
            this.text33desc = result[32].desc;
          }

          if (result[33]) {
            this.text34 = result[33].value + " " + result[33].unit;
            this.text34name = result[33].name;
            this.text34time = result[33].time;
            this.text34desc = result[33].desc;
          }

          if (result[34]) {
            this.text35 = result[34].value + " " + result[34].unit;
            this.text35name = result[34].name;
            this.text35time = result[34].time;
            this.text35desc = result[34].desc;
          }

          if (result[35]) {
            this.text36 = result[35].value + " " + result[35].unit;
            this.text36name = result[35].name;
            this.text36time = result[35].time;
            this.text36desc = result[35].desc;
          }

          if (result[36]) {
            this.text37 = result[36].value + " " + result[36].unit;
            this.text37name = result[36].name;
            this.text37time = result[36].time;
            this.text37desc = result[36].desc;
          }

          if (result[37]) {
            this.text38 = result[37].value + " " + result[37].unit;
            this.text38name = result[37].name;
            this.text38time = result[37].time;
            this.text38desc = result[37].desc;
          }

          if (result[38]) {
            this.text39 = result[38].value + " " + result[38].unit;
            this.text39name = result[38].name;
            this.text39time = result[38].time;
            this.text39desc = result[38].desc;
          }

          if (result[39]) {
            this.text40 = result[39].value + " " + result[39].unit;
            this.text40name = result[39].name;
            this.text40time = result[39].time;
            this.text40desc = result[39].desc;
          }

          if (result[40]) {
            this.text41 = result[40].value + " " + result[40].unit;
            this.text41name = result[40].name;
            this.text41time = result[40].time;
            this.text41desc = result[40].desc;
          }

          if (result[41]) {
            this.text42 = result[41].value + " " + result[41].unit;
            this.text42name = result[41].name;
            this.text42time = result[41].time;
            this.text42desc = result[41].desc;
          }

          if (result[42]) {
            this.text43 = result[42].value + " " + result[42].unit;
            this.text43name = result[42].name;
            this.text43time = result[42].time;
            this.text43desc = result[42].desc;
          }

          if (result[43]) {
            this.text44 = result[43].value + " " + result[43].unit;
            this.text44name = result[43].name;
            this.text44time = result[43].time;
            this.text44desc = result[43].desc;
          }

          if (result[44]) {
            this.text45 = result[44].value + " " + result[44].unit;
            this.text45name = result[44].name;
            this.text45time = result[44].time;
            this.text45desc = result[44].desc;
          }

          if (result[45]) {
            this.text46 = result[45].value + " " + result[45].unit;
            this.text46name = result[45].name;
            this.text46time = result[45].time;
            this.text46desc = result[45].desc;
          }

          if (result[46]) {
            this.text47 = result[46].value + " " + result[46].unit;
            this.text47name = result[46].name;
            this.text47time = result[46].time;
            this.text47desc = result[46].desc;
          }

          if (result[47]) {
            this.text48 = result[47].value + " " + result[47].unit;
            this.text48name = result[47].name;
            this.text48time = result[47].time;
            this.text48desc = result[47].desc;
          }

          if (result[48]) {
            this.text49 = result[48].value + " " + result[48].unit;
            this.text49name = result[48].name;
            this.text49time = result[48].time;
            this.text49desc = result[48].desc;
          }

          if (result[49]) {
            this.text50 = result[49].value + " " + result[49].unit;
            this.text50name = result[49].name;
            this.text50time = result[49].time;
            this.text50desc = result[49].desc;
          }

          if (result[50]) {
            this.text51 = result[50].value + " " + result[50].unit;
            this.text51name = result[50].name;
            this.text51time = result[50].time;
            this.text51desc = result[50].desc;
          }

          if (result[51]) {
            this.text52 = result[51].value + " " + result[51].unit;
            this.text52name = result[51].name;
            this.text52time = result[51].time;
            this.text52desc = result[51].desc;
          }
        } else {
          console.log("222");
          this.$message("实时监控查询接口报错");
        }
      });
    },
    clickBtn2() {
      this.getGroupList();
      this.formInline.tubiaoName = "1";
    },
    getGroupList() {
      this.$http({
        method: "get",
        url: `/jndpportal/wbjk/getGroupList.xhtml`,
      })
        .then((res) => {
          if (res.data[0].res == "success") {
            this.formInline.groupList = res.data[0].data;
            // this.formInline.groupName = '';
            this.getFactoryList();
          }
        })
        .catch((err) => {
          this.$message("查询集团列表接口报错");
        });
    },
    getFactoryList(val) {
      if (this.formInline.groupName == "") {
        this.$message("请选选择集团");
        return false;
      } else {
        this.factoryList = [];
        let param = {
          groupid: this.formInline.groupName,
        };
        this.$http({
          method: "get",
          url: `jndpportal/wbjk/getFactoryList.xhtml`,
          params: param,
        })
          .then((res) => {
            if (res.data[0].res == "success") {
              this.formInline.factoryList = res.data[0].data;
              if (this.formInline.factoryList.length > 0) {
                this.formInline.factoryName = this.formInline.factoryList[0].id;
                this.getJzList();
              }
            }
          })
          .catch((err) => {
            this.$message("查询集团列表接口报错");
          });
      }
    },
    getJzList() {
      if (this.formInline.groupName == "") {
        this.$message("请选择集团");
        return false;
      } else if (this.formInline.factoryName == "") {
        this.$message("请选择电厂");
        return false;
      } else {
        this.formInline.jzList = [];
        let param = {
          factoryid: this.formInline.factoryName,
        };
        this.$http({
          method: "get",
          url: `jndpportal/wbjk/getJzList.xhtml`,
          params: param,
        })
          .then((res) => {
            if (res.data[0].res == "success") {
              this.formInline.jzList = res.data[0].data;
              this.formInline.jzName = this.formInline.jzList[0].id;
              this.getOperationDiagram();
            }
          })
          .catch((err) => {
            this.$message("查询集团列表接口报错");
          });
      }
    },
  },
};
</script>
<style scoped lang='less'>
@import url("./jianKong.less");
</style>