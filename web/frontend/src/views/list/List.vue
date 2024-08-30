<script setup>
import {ref, onMounted} from 'vue'
import {ElMessage} from 'element-plus'
import dayjs from 'dayjs'
// 假设你有一个名为 rumorPageListService 的 API 服务
import {rumorPageListService} from '@/api/list.js' // 请根据实际路径替换
import Pager from "@/components/Pager.vue";
import {Calendar, DataAnalysis} from "@element-plus/icons-vue";

const tags = ['食品安全', '营养健康', '疾病防治', '美容健身', '生活解惑', '天文地理', '生物', '数理化', '交通运输', '航空航天',
  '前沿科技', '能源环境', '农业技术', '建筑水利']
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
    itemsThisPage.value = result.data.data.items.map(item => ({
      ...item,
      date: dayjs(item.published_date).format('YYYY/MM/DD')
    }))
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

          <el-row gutter="30" style="margin: 20px; display: flex; justify-content: center">
            <el-col span="1" style="display: flex; justify-content: center;">
              <!-- 重置按钮 -->
              <el-button
                  type="danger"
                  @click="selectedTags = []; searchQuery = ''; handleSearch()"
                  class="search-button"
              >
                重置
              </el-button>
            </el-col>
            <el-col span="12" style="display: flex; justify-content: center;">
              <!-- 搜索按钮 -->
              <el-button
                  type="primary"
                  @click="handleSearch"
                  class="search-button"
              >
                搜索
              </el-button>
            </el-col>
          </el-row>

        </el-card>
      </el-col>

      <!-- 右侧大卡片 -->
      <el-col :span="18">
        <el-card class="big-card">
          <el-scrollbar class="scroll-area">
            <div v-for="item in itemsThisPage" :key="item.id" class="small-card" @click="openDialog(item)">
              <!-- 新增红色标签 -->
              <el-row gutter="0" style="width: 100%;">
                <el-col :span="3" class="card-date">
                  <h3 class="centered">{{ item.date }}</h3>
                </el-col>
                <el-col :span="1">
                  <el-divider direction="vertical" style="height: 120px"></el-divider>
                </el-col>
                <el-col :span="18" class="card-content">
                  <el-row>
                    <el-col :span="18">
                      <h3>{{ item.rumor.concat("?") }}</h3>
                    </el-col>
                    <el-col :span="6" style="align-content: center; display: flex; justify-content: flex-end">
                      <span class="rumor-label">谣言</span>
                    </el-col>
                  </el-row>
                  <el-row>
                    <el-col :span="12">
                      <p>
                        <el-icon>
                          <CollectionTag/>
                        </el-icon>
                        <p> {{ item.tags }} </p>
                      </p>
                    </el-col>
                    <el-col :span="12">
                      <p class="origin-text">来源：{{ item.origin }}</p>
                    </el-col>
                  </el-row>
                </el-col>
              </el-row>
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
        v-model="dialogVisible"
        title="详细信息"
        width="1000px"
        :close-on-click-modal="false"
    >
      <el-row :gutter="20" class="dialog-content">
        <el-col :span="24">
          <h3>
            <el-icon class="near-text-icon">
              <chat-line-round/>
            </el-icon>
            <strong>谣言</strong>
          </h3>
          <p class="text-in-dialog">{{ selectedItem?.rumor }}</p>
        </el-col>

        <el-divider></el-divider>

        <el-col :span="24">
          <h3>
            <el-icon class="near-text-icon">
              <document-copy/>
            </el-icon>

            <strong>真相</strong>
          </h3>
          <p class="text-in-dialog">{{ selectedItem?.truth }}</p>
        </el-col>

        <el-divider></el-divider>

        <el-row :gutter="20" style="width: 100%; margin-left: 10px; margin-right: 10px">
          <p style="padding-right: 140px">
            <el-icon class="near-text-icon">
              <location/>
            </el-icon>
            <strong>来源：</strong>{{ selectedItem?.origin }}
            <el-divider direction="vertical"></el-divider>
            <el-icon class="near-text-icon">
              <calendar/>
            </el-icon>
            <strong>发布日期：</strong>{{ selectedItem?.published_date }}
          </p>
        </el-row>

        <el-row style="width: 100%; padding-left: 10px; padding-right: 10px">
          <p>
            <el-icon class="near-text-icon">
              <Link/>
            </el-icon>
            <strong>辟谣链接：</strong><a :href="selectedItem?.url" target="_blank">{{ selectedItem?.url }}</a>
          </p>
        </el-row>
      </el-row>
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
  width: 100px;
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
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.el-card__body {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  padding: 0; /* 移除内边距以确保没有额外间距 */
  overflow: hidden; /* 防止超出内容导致滚动 */
}

.scroll-area {
  flex-grow: 1; /* 使其在 flex 布局中扩展以填充剩余空间 */
  overflow-y: auto;
  margin-bottom: 20px;
  height: 66vh;
  padding-right: 20px;
}

.small-card {
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  border: 1px solid #ebeef5;
  margin-bottom: 15px;
  transition: background-color 0.3s;
  border-radius: 10px; /* 为卡片增加圆角 */
}

.small-card:hover {
  background-color: #f5f5f5;
}

.rumor-label {
  background-color: #f56c6c; /* 红色背景 */
  color: #fff; /* 白色文字 */
  padding: 4px 2px; /* 内边距 */
  font-size: 12px; /* 字体大小 */
  border-radius: 4px; /* 圆角 */
  font-weight: bold; /* 加粗 */
  margin: 10px;
  text-align: center;
  align-self: center;
}

.card-date {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding-right: 10px; /* 增加右内边距 */
  font-size: 14px;
}

.card-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding-left: 10px; /* 增加左内边距 */
}

.card-footer {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

.card-footer el-icon {
  margin-right: 5px;
}

.dialog-footer {
  text-align: right;
}

.centered {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 75%;
  width: 100%;
}

.origin-text {
  color: #909399;
  font-size: 14px;
  text-align: right;
}

.dialog-content {
  padding: 20px;
}

.near-text-icon {
  margin-right: 8px;
}

.text-in-dialog {
  font-size: 16px;
  padding-left: 30px;
  padding-right: 30px;
}
</style>
