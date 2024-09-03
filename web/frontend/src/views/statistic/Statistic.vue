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
    <el-row style="display: flex; justify-content: center">
      <el-col :span="12">
        <h1 style="text-align: center">谣言地域-类别关联分析</h1>
        <img class="preview" src="../../assets/province_category_hot.png" width="90%" height="80%">
      </el-col>
      <el-col :span="1"/>
      <el-col :span="10">
        <h1 style="text-align: center">统计结论</h1>
        <p style="width: 100%; font-size: 18px; line-height: 1.6; color: #333; text-align: justify">
          <strong>1. 谣言类别统计：</strong>突发事件、食药卫生、公共政策和科学常识占9种谣言类别的近九成，其中类别为突发事件的谣言类别最多。<br><br>
          <strong>2. 谣言地域统计：</strong>在本系统收录的谣言数据集中，重庆、四川、山东、广东、河南、浙江等地的谣言数量较多，该现象可能与地区信息的传播方式等有关<br><br>
          <strong>3. 谣言地域-类别关联分析：</strong>整体来看，公共安全和突发事件类的谣言在不同省份中较为普遍，显示出这两类谣言是谣言传播中的主要类别。而在一些省份中，谣言类型较为集中，如河南省集中在突发事件类，广东省有关公共政策的谣言较多。<br><br>
          <strong>4. 总体观察：</strong> 通过这些观察可以初步了解谣言类别的分布情况，各省份谣言的数量对比，以及谣言的地域-分类关联关系，有助于进一步研究这些谣言的产生原因和传播路径。
        </p>
      </el-col>
    </el-row>
    </el-col>
  </el-card>
</template>