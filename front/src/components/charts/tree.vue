<template>
  <div ref="dom" class="charts chart-tree"></div>
</template>

<script>
import echarts from 'echarts'
import tdTheme from './theme.json'
import { on, off } from '@/libs/tools'
echarts.registerTheme('tdTheme', tdTheme)
export default {
  name: 'ChartTree',
  props: {
    value: Array,
    text: String,
    subtext: String
  },
  data () {
    return {
      dom: null,
      option: null
    }
  },
  methods: {
    resize () {
      this.dom.resize()
    }
  },
  watch:{//用于监测子组件暴露的属性值变化所触发的动作
        value: function () {
          this.$nextTick(() => {
          // this.dom.clear();
          console.log(this.value)
          // let legend = this.value.map(_ => _.name)
          this.option = {
            title: {
              text: this.text,
              subtext: this.subtext,
              x: 'center',
              // y: 'bottom'
            },
        //     tooltip: {
        //       trigger: 'item',
        //       formatter: '{a} <br/>{b} : {c} ({d}%)'
        //     },
        //     toolbox: {
        //     show: true,
        //     feature: {
        //         dataZoom: {
        //             yAxisIndex: 'none'
        //         },
        //         dataView: {readOnly: false},
        //         magicType: {type: ['line', 'bar']},
        //         restore: {},
        //         saveAsImage: {}
        //     }
        // },
        //     legend: {
        //       orient: 'vertical',
        //       x: 'left',
        //       // y: 'bottom',
        //       padding: [80,0,0,8],
        //       data: legend
        //     },
            series: [{
              type: 'treemap',
              data: this.value
          }]
          }
        this.dom = echarts.init(this.$refs.dom, 'tdTheme')
        this.dom.setOption(this.option)
        on(window, 'resize', this.resize)
          })
        }

      },
  mounted () {
    this.$nextTick(() => {
          // this.dom.clear();
          console.log(this.value)
          // let legend = this.value.map(_ => _.name)
          this.option = {
            title: {
              text: this.text,
              subtext: this.subtext,
              x: 'center',
              // y: 'bottom'
            },
        //     tooltip: {
        //       trigger: 'item',
        //       formatter: '{a} <br/>{b} : {c} ({d}%)'
        //     },
        //     toolbox: {
        //     show: true,
        //     feature: {
        //         dataZoom: {
        //             yAxisIndex: 'none'
        //         },
        //         dataView: {readOnly: false},
        //         magicType: {type: ['line', 'bar']},
        //         restore: {},
        //         saveAsImage: {}
        //     }
        // },
        //     legend: {
        //       orient: 'vertical',
        //       x: 'left',
        //       // y: 'bottom',
        //       padding: [80,0,0,8],
        //       data: legend
        //     },
            series: [{
              type: 'treemap',
              data: [{
                  name: 'nodeA',            // First tree
                  value: 10,
                  children: [{
                      name: 'nodeAa',       // First leaf of first tree
                      value: 4
                  }, {
                      name: 'nodeAb',       // Second leaf of first tree
                      value: 6
                  }]
              }, {
                  name: 'nodeB',            // Second tree
                  value: 20,
                  children: [{
                      name: 'nodeBa',       // Son of first tree
                      value: 20,
                      children: [{
                          name: 'nodeBa1',  // Granson of first tree
                          value: 20
                      }]
                  }]
              }]
          }]
          }
        this.dom = echarts.init(this.$refs.dom, 'tdTheme')
        this.dom.setOption(this.option)
        on(window, 'resize', this.resize)
          })

  },
  beforeDestroy () {
    off(window, 'resize', this.resize)
  }
}
</script>
