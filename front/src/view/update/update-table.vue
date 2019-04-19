<template>
<div>
  <Row :gutter="10">
    <i-col>
      <Card>
        <Upload
        multiple
        type="drag"
        v-bind:action="uploadurl">
        <div style="padding: 40px 0">
            <Icon type="ios-cloud-upload" size="60" style="color: #3399ff"></Icon>
            <p @click='click'>Click or drag files here to upload</p>
        </div>
      </Upload>
      </Card>
    </i-col>
  </Row>
</div>
</template>

<script>

import { getArrayFromFile, getTableDataFromArray } from '@/libs/util'
import config from '@/config'
const baseUrl = process.env.NODE_ENV === 'development' ? config.baseUrl.dev : config.baseUrl.pro

export default {
  name: 'update_table_page',
  data () {
    return {
      // 文件上传地址
      // uploadurl: baseUrl+'upload',
      // uploadurl: 'http://127.0.0.1:5000/upload',
      uploadurl: baseUrl+'upload',
      columns: [],
      tableData: [],
           options: {
          // https://github.com/simple-uploader/Uploader/tree/develop/samples/Node.js
          target: 'upload',
          testChunks: false
        },
        attrs: {
          accept: 'image/*'
        }
    }
  },
  methods: {
    click (){
      console.log(baseUrl)
    },
    beforeUpload (file) {
      getArrayFromFile(file).then(data => {
        let { columns, tableData } = getTableDataFromArray(data)
        this.columns = columns
        this.tableData = tableData
      }).catch(() => {
        this.$Notice.warning({
          title: '只能上传Csv文件',
          desc: '只能上传Csv文件，请重新上传'
        })
      })
      return false
    }
  }
}
</script>

<style>
.update-table-intro{
  margin-top: 10px;
}
.code-high-line{
  color: #2d8cf0;
}

  .uploader-example {
    /* width: 880px;
    padding: 15px;
    margin: 40px auto 0; */
    font-size: 12px;
    /* box-shadow: 0 0 10px rgba(0, 0, 0, .4); */
  }
  .uploader-example .uploader-btn {
    margin-right: 4px;
  }
  .uploader-example .uploader-list {
    max-height: 440px;
    overflow: auto;
    overflow-x: hidden;
    overflow-y: auto;
  }

</style>
