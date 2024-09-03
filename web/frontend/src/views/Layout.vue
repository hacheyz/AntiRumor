<script setup>
import NavBarVue from '@/components/NavBar.vue'
import FooterVue from '@/components/Footer.vue'
</script>

<template>
  <el-container class="layout-container">
    <nav-bar-vue/>
    <el-container class="main-container">
      <el-main class="content">
        <router-view/>
      </el-main>
      <footer-vue/>
    </el-container>
  </el-container>
</template>

<style lang="scss" scoped>
.layout-container {
  width: 100%;
  height: 100vh; /* 确保页面高度为视口高度 */
  display: flex;
  flex-direction: column;
}

.header-container {
  width: 100%;
  padding: 0;
  margin: 0;
}

.main-container {
  display: flex;
  flex-direction: column;
  flex: 1; /* 使 main-container 占据剩余空间 */
}

.content {
  flex: 1; /* 使 el-main 占据剩余空间 */
  padding: 20px;
  overflow: auto;
}

.footer {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  color: #666;
}
</style>
