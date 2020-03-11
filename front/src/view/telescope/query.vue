<template>
  <div style="margin:0px;">
    <!-- 搜索输入 -->
    <Card>
      <row style="margin:10px">
        <i-col span="3">
          <Select v-model="selected_table" size="large" placeholder="场景选择">
            <Option v-for="item in tableList" :value="item" :key="item">{{ item }}</Option>
          </Select>
        </i-col>
          <!-- 搜索建议 -->
          <AutoComplete search
            clearable = true
            size="large"
            v-model="queryString"
            :data="suggestData"
            @on-search="handleSearch"
            @on-select="click"
            placeholder="请先选择左侧的查询场景，方可获得有效数据..."
            style="width:400px;margin-left:30px">
          </AutoComplete>
          <Button type="primary" size="large" style="margin-left:16px" shape="circle" icon="ios-search" @click="click"></Button>
         <div class="search-select">
            <!-- transition-group也是vue2.0中的新特性,tag='ul'表示用ul包裹v-for出来的li -->
                <transition-group name="itemfade" tag="ul" mode="out-in" v-cloak>
                    <li v-for="(value,index) in myData" :class="{selectback:index==now}" class="search-select-option search-select-list" @mouseover="selectHover(index)" @click="selectClick(index)" :key="value">
                        {{value}}
                    </li>
                </transition-group>
            </div>
      </row>
      <row style="margin:10px">
        <i-col style="padding-top: 6px">
          <div v-show="dimitions.length>0"><h4>可以针对如下数据提问：<span v-for="d in dimitions" :key="d" ><Divider type="vertical" /><a @click="getDimition"><Icon :type="d.type"/> {{d.name}}</a></span><span style="padding-left: 20px" ><Button size="small" type="primary" @click="moreDimitions"> 全部字段 <Icon type="ios-arrow-down" /></Button></span></h4></div>
        </i-col>
      </row>
    </Card>

    <!-- 可视化图表 -->
    <Card style="margin-top: 16px">
       <Tabs style="padding-left: 8px">
        <TabPane label="可视化" icon="md-stats">
          <!-- <Row></Row> -->
          <Row  style="padding-top: 8px">
            <i-col span='5'><h2>{{queryString}}</h2>
              <!-- 描述信息 -->
              <p style="margin-top:12px">{{options[0].text}}</p>
            </i-col>
            <i-col span="18">
              <i-col v-if="chartType=='count'" span='12' offset="5" style="height: 150px;margin-top:150px;margin-bottom:12px;padding-bottom: 10px;">
                <count-to :end="options[0].Chartoption" count-class="count-style"/>
              </i-col>
                <chart-pie v-for="(opt,index) in options" :key=index :id=index style="height: 500px" :value="pieData" :option="opt.Chartoption" :text="queryString"></chart-pie>
            </i-col>
          </Row>
          <Row>
            <span>点我反馈：<a>满意<Icon type="md-happy" size="18"/></a><Divider type="vertical" /><a @click='bad'>不满意<Icon type="md-sad" size="18"/></a></span>
            <!-- <p style="margin-top:16px"><Input style="width:300px;"/><Button style="margin-left:8px">提交</Button></p> -->
          </Row>            
        </TabPane>
        <TabPane label="数据视图" icon="md-grid" >
          <Table border :columns="columns6" :data="data5"></Table>
        </TabPane>
    </Tabs>
    </Card>
    <!-- 数据样例模态框 -->
    <Modal v-model="showDimition" v-bind:title="clickDimition">
      <p>{{top30}}</p>
    </Modal>
  </div>
</template>

<script>
import { errorReq, getChart, readDimetions, getSuggests, readDatasets,read_dimitions, getTop30} from '@/api/data'
import { ChartPie, ChartBar, ChartTree } from '_c/charts'
import CountTo from '_c/count-to'
// import InforCard from '_c/info-card'

export default {
  name: 'query',
  components: {
    ChartPie,
    ChartBar,
    ChartTree,
    CountTo,
    // InforCard
  },
  data () {
    return {
      queryString: '',
      suggestData: [],
      top30: '',
      chartType :'pie',
      opt: Object,
      options: Array,
      dimitions: [],
      Dvalues: [],
      showDimition: false,
      clickDimition: '',
      queryString: '',
      selected_table: '',
      filter2: [
                    {
                        value: 'table1',
                        label: '25岁以下'
                    },
                    {
                        value: 'tabel2',
                        label: '25-50岁'
                    },
                    {
                        value: 'table3',
                        label: '50岁以上'
                    },

                ],
      tableList: ['贷款场景'

                ],
      treeData: [{
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
              }],
      inforCardData:  { title: '上海男性的数量', icon: 'md-help-circle', count: 142, color: '#2d8cf0' },
      pieData: [
        {value: 335, name: '直接访问'},
        {value: 310, name: '邮件营销'},
        {value: 234, name: '联盟广告'},
        {value: 135, name: '视频广告'},
        {value: 1548, name: '搜索引擎'}
      ],
      barData: {
        Mon: 13253,
        Tue: 34235,
        Wed: 26321,
        Thu: 12340,
        Fri: 24643,
        Sat: 1322,
        Sun: 1324
      },
      columns6: [
                    {
                        title: 'Date',
                        key: 'date'
                    },
                    {
                        title: 'Name',
                        key: 'name'
                    },
                    {
                        title: 'Age',
                        key: 'age',
                        filters: [
                            {
                                label: 'Greater than 25',
                                value: 1
                            },
                            {
                                label: 'Less than 25',
                                value: 2
                            }
                        ],
                        filterMultiple: false,
                        filterMethod (value, row) {
                            if (value === 1) {
                                return row.age > 25;
                            } else if (value === 2) {
                                return row.age < 25;
                            }
                        }
                    },
                    {
                        title: 'Address',
                        key: 'address',
                        filters: [
                            {
                                label: 'New York',
                                value: 'New York'
                            },
                            {
                                label: 'London',
                                value: 'London'
                            },
                            {
                                label: 'Sydney',
                                value: 'Sydney'
                            }
                        ],
                        filterMethod (value, row) {
                            return row.address.indexOf(value) > -1;
                        }
                    }
                ],
      data5: [
          {
              name: 'John Brown',
              age: 18,
              address: 'New York No. 1 Lake Park',
              date: '2016-10-03'
          },
          {
              name: 'Jim Green',
              age: 24,
              address: 'London No. 1 Lake Park',
              date: '2016-10-01'
          },
          {
              name: 'Joe Black',
              age: 30,
              address: 'Sydney No. 1 Lake Park',
              date: '2016-10-02'
          },
          {
              name: 'Jon Snow',
              age: 26,
              address: 'Ottawa No. 2 Lake Park',
              date: '2016-10-04'
          }
      ]
    }
  },
  mounted () {
    // alert(test)
    readDatasets().then(res => {
      this.tableList = res.data.filename
    }).catch(err => {
      console.log(err)
    })
    // 初始化echart对象
    getChart('今日搜索量','b.csv').then(res => {
              this.options = [1,2,3,4,5,6]
              this.opt = res.data.Chartoption
              this.chartType = 'init'
              this.title = res.data.title
              this.text = res.data.text
            }).catch(err => {
              console.log(err)
            })
  },

  watch: {
    selected_table: function (val) {
      this.dimitions = []
      //  ajax访问后台读取常见字段
      // alert(val)

      read_dimitions(val, 10).then(res => {
        this.dimitions = res.data.dimitions
      }).catch(err => {
        console.log(err)
        // alert(err)
      })
    }
  },

  methods: {
    // 搜索建议
    handleSearch: function (value) {
      // alert(this.selected_table)
     let query = value
     getSuggests(query).then(res => {
      //  alert(query)
       this.suggestData = []
       this.suggestData = res.data.suggestsList
      }).catch(err => {
        console.log(err)
        // alert(err)
      })

    },


    getData(itableName, queryString) {
      getChart().then(res => {
      this.tableData = res.data
    }).catch(err => {
      console.log(err)
    })
    },
    getDimition: function (event) {
      this.clickDimition = event.currentTarget.innerText+'数据样例'
      getTop30(this.selected_table,this.clickDimition).then(res => {
        this.top30 = res.data.values
      }).catch(err => {
        console.log(err)
      })
      this.showDimition = true
    },
    moreDimitions: function () {
      // alert(this.selected_table)
     read_dimitions(this.selected_table,-1).then(res => {
       this.dimitions = []
        this.dimitions = res.data.dimitions
      }).catch(err => {
        console.log(err)
        // alert(err)
      })

    },

    click () {
      if (this.queryString!=='' & this.selected_table!==''){
        // alert('触发后端检索')
        if (this.queryString==='京东访问来源分布'){
          this.pieData = [
            {value: 335, name: '直接访问'},
            {value: 310, name: '邮件营销'},
            {value: 234, name: '联盟广告'}
            ]
        }
        else{
          // ajax.get请求
          // bad solution for more than one chart

            this.options = [1,2,3,4,5]
            this.opt = res.data.Chartoption
            this.chartType = 'bad solution'
            this.title = res.data.title
            this.text = res.data.text


            getChart(this.queryString,this.selected_table).then(res => {
              this.options = res.data
              // this.opt = res.data.Chartoption
              this.chartType = res.data[0].chartType
              this.title = res.data.title
              this.text = res.data.text

              
            }).catch(err => {
              console.log(err)
            })
          console.log(this.Chartoption)
          console.log(this.chartType)
        }
        console.log("检索语句为："+this.queryString),
        console.log("数据库为:"+this.selected_table)
        console.log(this.pieData)
      }
      else {
        this.$Notice.warning({
          title: '输入有误',
          desc: '您的输入有误，请重新输入'
        })
      }

    },
    bad (){
        this.$Notice.success({
          title: '反馈已收到',
          desc: '您问的是：'+this.queryString+"<br>您的反馈是：Bad"+'<br>您的反馈内容是：'+this.buginfo
        })
    },
  }
}
</script>

<style>
.input {
  line-height: 50px;
}
.count-style{
  font-size: 150px;
}
</style>
