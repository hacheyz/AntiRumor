<script setup>
</script>

<template>
  <el-container class="layout-container">
    <el-header class="header-container">
      <el-menu
        active-text-color="#ffd04b"
        background-color="#014561"
        text-color="#fff"
        class="top-menu"
        mode="horizontal"
        router>
        <el-menu-item index="/home"><span>科普园地</span></el-menu-item>
        <el-menu-item index="/list"><span>辟谣信息聚合</span></el-menu-item>
        <el-menu-item index="/judge"><span>辟谣法官</span></el-menu-item>
      </el-menu>
    </el-header>

    <el-container class="main-container">
      <el-main class="content">
        <router-view></router-view>
      </el-main>
      <el-footer class="footer">
        谣言治理系统 ©2024 Created by&nbsp;<a href="http://github.com/hacheyz/AntiRumor" target="_blank">HIT-AntiRumor team</a>
      </el-footer>
    </el-container>
  </el-container>
</template>

<style lang="scss" scoped>
.layout-container {
  width: 100%;
  height: 100vh;  /* 确保页面高度为视口高度 */
  display: flex;
  flex-direction: column;
}

.header-container {
  width: 100%;
  padding: 0;
  margin: 0;
}

.top-menu {
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
