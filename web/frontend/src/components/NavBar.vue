<template>
  <el-header class="header-container">
    <el-menu
        active-text-color="#8888FF"
        text-color="#fff"
        class="top-menu"
        mode="horizontal"
        router>
      <el-menu-item index="/home"><span>科普园地</span></el-menu-item>
      <el-menu-item index="/list"><span>辟谣信息聚合</span></el-menu-item>
      <el-menu-item index="/judge"><span>辟谣法官</span></el-menu-item>
      <el-menu-item index="/statistic"><span>统计分析</span></el-menu-item>
    </el-menu>
  </el-header>
</template>

<style scoped>
.top-menu {
  padding: 0;
  margin: 0;
  background-image: url('/colorful_minimal_vector_abstract_art_background.jpg');
  background-size: cover; /* 图片会被缩放到足以覆盖整个元素 */
  background-position: bottom right;
}
</style>