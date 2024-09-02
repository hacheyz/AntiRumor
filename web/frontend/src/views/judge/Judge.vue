<script setup>
import {onMounted, ref} from "vue";
import Table from "@/components/Table.vue";
import Pager from "@/components/Pager.vue";
import {
  questionPageListService,
  questionAddService,
  questionAddAgreeService,
  questionAddDisagreeService
} from "@/api/judge.js";
import {CloseBold, Select} from "@element-plus/icons-vue";

const currentContent = ref([{
  id: 1,
  question: '',
  create_date: '',
  num_agree: 0,
  num_disagree: 0,
  expert_conclusion: '',
}])
const title = ref('')
const total = ref(0)
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
    prop: 'num_agree',
    align: 'center',
    sortable: true,
  },
  {
    label: '反对数',
    prop: 'num_disagree',
    align: 'center',
    sortable: true,
  },
  {
    label: '你的观点',
    prop: 'action',
    align: 'center',
    slot: [
      {
        icon: Select  ,
        type: 'success',
        action: (row) => doAgree(row)
      },
      {
        icon: CloseBold,
        type: 'danger',
        action: (row) => doDisagree(row)
      }
    ]
  },
  {
    label: '专家结论',
    prop: 'expert_conclusion',
    align: 'center',
  },
])

const fetchQuestionPageList = async () => {
  const res = await questionPageListService({
    pageNum: pageNum.value,
    pageSize: pageSize.value,
  })
  currentContent.value = res.data.data.items
  total.value = res.data.data.total
}

const doAgree = async (row) => {
  await questionAddAgreeService(row.id)
  await fetchQuestionPageList()
}

const doDisagree = async (row) => {
  await questionAddDisagreeService(row.id)
  await fetchQuestionPageList()
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
  <Table :data="currentContent" :columns="columns"/>
  <Pager
      :pageNum="pageNum"
      :pageSize="pageSize"
      :total="total"
      @size-change="onSizeChange"
      @current-change="onCurrentChange"
  />
</template>