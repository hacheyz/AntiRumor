<script setup>
import {ref, onMounted} from 'vue'
import {ElMessage} from 'element-plus'
// 假设你有一个名为 rumorPageListService 的 API 服务
import {rumorPageListService} from '@/api/list.js' // 请根据实际路径替换
import Pager from "@/components/Pager.vue";

const tags = ['疫苗', '药物', '病毒', '传播途径', '预防措施']
const searchQuery = ref('')
const selectedTags = ref([])
const itemsThisPage = ref([])
const total = ref(0)
const pageNum = ref(1)
const pageSize = ref(10)
const dialogVisible = ref(false)
const selectedItem = ref({
  rumor: '',
  truth: '',
  tags: [],
  origin: '',
  published_date: '',
  url: '',
})

const fetchCardsPageList = async () => {
  try {
    let params = {
      pageNum: pageNum.value,
      pageSize: pageSize.value,
    }
    if (searchQuery.value) {
      params.searchRumor = searchQuery.value
    }
    if (selectedTags.value.length > 0) {
      params.tags = selectedTags.value.join(',')
    }
    const result = await rumorPageListService(params)
    total.value = result.data.data.total
    itemsThisPage.value = result.data.data.items
  } catch (error) {
    ElMessage.error('Error fetching rumor list')
  }
}

const handleSearch = () => {
  pageNum.value = 1 // 搜索时重置到第一页
  fetchCardsPageList()
}

const openDialog = (item) => {
  selectedItem.value = item
  dialogVisible.value = true
}

const onSizeChange = (size) => {
  pageSize.value = size
  fetchCardsPageList()
}

const onCurrentChange = (num) => {
  pageNum.value = num
  fetchCardsPageList()
}

onMounted(fetchCardsPageList)
</script>

<template>
  <el-container style="height: 100%; width: 100%;">
    <!-- 使用 el-row 和 el-col 排列卡片 -->
    <el-row gutter="20" style="width: 100%;">
      <!-- 左侧筛选器 -->
      <el-col :span="6">
        <el-card class="filter-card">
          <!-- 搜索框 -->
          <el-input
              placeholder="请输入搜索内容"
              v-model="searchQuery"
              clearable
              style="margin-bottom: 20px;"
          />

          <!-- 标签筛选 -->
          <el-checkbox-group v-model="selectedTags" class="tag-filter">
            <el-checkbox v-for="tag in tags" :label="tag" :key="tag">{{ tag }}</el-checkbox>
          </el-checkbox-group>

          <!-- 搜索按钮 -->
          <el-button
              type="primary"
              @click="handleSearch"
              class="search-button"
          >
            搜索
          </el-button>
        </el-card>
      </el-col>

      <!-- 右侧大卡片 -->
      <el-col :span="18">
        <el-card class="big-card">
          <el-scrollbar class="scroll-area" height="300px">
            <div v-for="item in itemsThisPage" :key="item.id" class="small-card">
              <div class="card-content">
                <h4>{{ item.rumor }}</h4>
                <el-button type="primary" @click="openDialog(item)">查看详情</el-button>
              </div>
            </div>
            <template v-if="!itemsThisPage || itemsThisPage.length === 0">
              <el-empty description="没有数据"/>
            </template>
          </el-scrollbar>
          <Pager
              :pageNum="pageNum"
              :pageSize="pageSize"
              :total="total"
              @size-change="onSizeChange"
              @current-change="onCurrentChange"
          />
        </el-card>
      </el-col>
    </el-row>

    <!-- 详情对话框 -->
    <el-dialog
        :visible.sync="dialogVisible"
        title="详细信息"
        width="600px"
    >
      <p><strong>标题：</strong>{{ selectedItem?.rumor }}</p>
      <p><strong>正文：</strong>{{ selectedItem?.truth }}</p>
      <!--      <p><strong>标签：</strong>{{ selectedItem?.tags.join(', ') }}</p>--> <!-- TODO -->
      <p><strong>来源：</strong>{{ selectedItem?.origin }}</p>
      <p><strong>发布日期：</strong>{{ selectedItem?.published_date }}</p>
      <p><strong>链接：</strong>{{ selectedItem?.url }}</p>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">关闭</el-button>
      </span>
    </el-dialog>
  </el-container>
</template>

<style scoped>
.filter-card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.el-card__body {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  padding: 20px;
  box-sizing: border-box;
}

.tag-filter {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.search-button {
  margin-top: auto;
  width: 100%;
}

.card-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.big-card {
  width: 100%;
  height: 100%;
  padding: 20px;
  margin-bottom: 20px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}

.scroll-area {
  height: 100%;
  overflow-y: auto;
  margin-bottom: 20px;
}

.small-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border: 1px solid #ebeef5;
  margin-bottom: 10px;
}

.card-content {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.dialog-footer {
  text-align: right;
}
</style>
