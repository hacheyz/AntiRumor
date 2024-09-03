<script setup>
import {onMounted, ref, computed} from "vue";
import Table from "@/components/Table.vue";
import Pager from "@/components/Pager.vue";
import {
  questionPageListService,
  questionAddService,
  questionAddAgreeService,
  questionAddDisagreeService
} from "@/api/judge.js";
import {CloseBold, Select} from "@element-plus/icons-vue";
import { ElMessage } from 'element-plus';

const currentContent = ref([{
  id: 1,
  question: '',
  create_date: '',
  num_agree: 0,
  num_disagree: 0,
  expert_conclusion: '',
}])
const newQuestion = ref('')
const total = ref(0)

// 计算属性：用于根据投票状态显示数据或提示
const displayedContent = computed(() => {
  return currentContent.value.map(item => {
    const hasVoted = localStorage.getItem(`question_${item.id}_clicked`);
    return {
      ...item,
      hasVoted,
      num_agree_display: hasVoted ? item.num_agree : '投票后查看',
      num_disagree_display: hasVoted ? item.num_disagree : '投票后查看',
      expert_conclusion_display: hasVoted ? item.expert_conclusion : '投票后查看',
    };
  });
});

const columns = ref([
  {
    label: '序号',
    prop: 'id',
    align: 'center',
    sortable: true,
  },
  {
    label: '问题',
    prop: 'question',
    align: 'center',
  },
  {
    label: '创建时间',
    prop: 'create_date',
    align: 'center',
    sortable: true,
  },
  {
    label: '赞成数',
    prop: 'num_agree_display',  // 使用计算后的字段
    align: 'center',
  },
  {
    label: '反对数',
    prop: 'num_disagree_display',  // 使用计算后的字段
    align: 'center',
  },
  {
    label: '你的观点',
    prop: 'action',
    align: 'center',
    slot: [
      {
        icon: Select,
        type: 'success',
        action: (row) => handleAction(row, 'agree')
      },
      {
        icon: CloseBold,
        type: 'danger',
        action: (row) => handleAction(row, 'disagree')
      }
    ]
  },
  {
    label: '专家结论',
    prop: 'expert_conclusion_display',  // 使用计算后的字段
    align: 'center',
  },
]);

const fetchQuestionPageList = async () => {
  const res = await questionPageListService({
    pageNum: pageNum.value,
    pageSize: pageSize.value,
  });
  currentContent.value = res.data.data.items;
  total.value = res.data.data.total;
}

const handleAction = async (row, actionType) => {
  const key = `question_${row.id}_clicked`; // 使用问题ID作为唯一标识符
  if (!localStorage.getItem(key)) { // 检查 localStorage 中是否已存在该键
    if (actionType === 'agree') {
      await questionAddAgreeService(row.id);
    } else if (actionType === 'disagree') {
      await questionAddDisagreeService(row.id);
    }
    localStorage.setItem(key, 'true'); // 标记该问题已被点击
    await fetchQuestionPageList(); // 刷新列表
  } else {
    // alert('您已经对这个问题发表过意见了！'); // 提示用户已点击过
    ElMessage.error("您已经对这个问题发表过意见了！");
  }
}

const addQuestion = async () => {
  const res = await questionAddService({}, {
    question: newQuestion.value
  });
  ElMessage.success(res.data.message);
  // alert(res.data.message);
  newQuestion.value = '';
  await fetchQuestionPageList();
}

const pageNum = ref(1)
const pageSize = ref(10)
const onSizeChange = (size) => {
  pageSize.value = size
  fetchQuestionPageList()
}
const onCurrentChange = (num) => {
  pageNum.value = num
  fetchQuestionPageList()
}

onMounted(() => {
  fetchQuestionPageList()
})
</script>

<template>
  <el-card>
    <el-row :gutter="20" class="search-input">
      <el-col :span="1"/>
      <el-col :span="20">
        <el-input v-model="newQuestion" placeholder="请输入你的问题，以问号结尾" clearable/>
      </el-col>
      <el-col :span="2" style="display: flex; justify-content: center">
        <el-button type="primary" @click="addQuestion()">投递问题</el-button>
      </el-col>
      <el-col :span="1"/>
    </el-row>
    <el-row>
      <Table :data="displayedContent" :columns="columns"/>
    </el-row>
    <Pager
        :pageNum="pageNum"
        :pageSize="pageSize"
        :total="total"
        @size-change="onSizeChange"
        @current-change="onCurrentChange"
    />
  </el-card>
</template>


<style>
.search-input {
  margin-bottom: 20px;
}
</style>