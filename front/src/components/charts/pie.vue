<template>
  <div ref="dom" class="charts chart-pie"></div>
</template>

<script>
import echarts from 'echarts'
import tdTheme from './theme.json'
import { on, off } from '@/libs/tools'
echarts.registerTheme('tdTheme', tdTheme)
export default {
  name: 'ChartPie',
  props: {
        option: {
            type: Object,
            default(){
                return {}
            }
        },
    value: Array,
    text: String,
    title: String,
  },
  data () {
    return {
      dom: null,
    }
  },
  computed: {
    chartops: function () {
      return this.option
    }
},
  methods: {
    resize () {
      this.dom.resize()
    }
  },
  watch:{//用于监测子组件暴露的属性值变化所触发的动作
        option: function () {
          this.$nextTick(() => {
          // this.dom.clear()
          // alert(Object.keys(this.option).length)
          // document.getElementById("3")

          this.dom = echarts.init(this.$refs.dom, 'tdTheme')
          this.dom.clear()

          this.dom.setOption(this.chartops)
          
          
          // this.dom = echarts.init(document.getElementById("0"), 'tdTheme')
          // this.dom.clear()
          // this.dom.setOption(this.chartops)
 
          // echarts.refresh()
          on(window, 'resize', this.resize)
          })
          
        },
        deep: true

      },
  mounted () {
    this.$nextTick(() => {
      let legend = this.value.map(_ => _.name)
      this.opt = {
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        toolbox: {
        show: true,
        padding: [2,30,0,0],
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            dataView: {readOnly: false},
            magicType: {type: ['line', 'bar']},
            restore: {},
            saveAsImage: {}
        }
    },
        legend: {
          orient: 'vertical',
          x: 'left',
          y: 'center',
          // y: 'center',
          // padding: [80,0,0,8],
          data: legend
        },
        series: [
          {
            type: 'pie',
            radius: '55%',
            center: ['50%', '60%'],
            data: this.value,
            itemStyle: {
              emphasis: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      }
      this.dom = echarts.init(this.$refs.dom, 'tdTheme')
      this.dom.setOption(this.opt)
      this.dom.clear()
      on(window, 'resize', this.resize)
    })
  },
  beforeDestroy () {
    off(window, 'resize', this.resize)
  }
}
</script>
