<template>
  <div ref="chart" style="width: 1200px; height: 400px;"></div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import * as echarts from 'echarts';

export default {
  props: {
    chartData: {
      type: Array,
      required: true
    }
  },
  setup(props) {
    const chart = ref(null);
    let myChart = null;

    const setOption = () => {
      const option = {
        title: {
          text: '',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'horizontal', // Change orientation to horizontal
          top: '-0%', // Position at the bottom
          formatter: function (name) {
            // If text is too long, add ellipsis
            return name.length > 4 ? name.slice(0, 4) + '...' : name;
          },
        },
        series: [
          {
            name: '分类数量',
            type: 'pie',
            radius: '50%',
            center: ['50%', '50%'], // Keep the pie chart centered
            data: props.chartData,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };
      if (myChart) {
        myChart.setOption(option);
      }
    };

    onMounted(() => {
      myChart = echarts.init(chart.value);
      setOption();
    });

    watch(
        () => props.chartData,
        () => {
          setOption();
        }
    );

    return {
      chart
    };
  }
};
</script>
