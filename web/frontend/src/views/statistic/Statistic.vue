<script setup>
import {onMounted, ref} from "vue";
import PieChart from "@/components/PieChart.vue";
import {tagListWithRelateNumService} from "@/api/tag.js";

const categoryData = ref([
  {value: 0, name: ''},
]);

const areaData = ref([
  {value: 0, name: ''},
]);

const categories = ref(['突发事件', '食药卫生', '公共政策', '时事政治', '社会热点', '科学常识', '党史国史', '公共安全', '其它'])
const fetchPieChartData = async () => {
  const res = await tagListWithRelateNumService();
  const data = res.data.data;
  // data = [id: , name: , relateNum: ]
  const categoryDataTemp = [];
  const areaDataTemp = [];
  data.forEach(item => {
    if (categories.value.includes(item.name)) {
      categoryDataTemp.push({value: item.relateNum, name: item.name});
    } else {
      areaDataTemp.push({value: item.relateNum, name: item.name});
    }
  });
  categoryData.value = categoryDataTemp;
  areaData.value = areaDataTemp;
};

onMounted(() => {
  fetchPieChartData();
});
</script>

<template>
  <el-card>
    <el-row :gutter="20">
      <el-col :span="1"/>
      <el-col :span="8">
        <h1 style="text-align: center">谣言类别统计</h1>
        <div style="display: flex; justify-content: center; align-items: center;">
          <PieChart :chartData="categoryData"/>
        </div>
      </el-col>
      <el-col :span="14">
        <h1 style="text-align: center">谣言地域统计</h1>
        <div style="display: flex; justify-content: center; align-items: center;">
          <PieChart :chartData="areaData"/>
        </div>
      </el-col>
      <el-col :span="1"/>
    </el-row>
    <el-col>
      <h1 style="text-align: center">谣言地域关联分析</h1>
    <el-row style="display: flex; justify-content: center">
      <img class="preview" src="../../assets/province_category_hot.png" width="50%" height="80%">
    </el-row>
    </el-col>
  </el-card>
</template>