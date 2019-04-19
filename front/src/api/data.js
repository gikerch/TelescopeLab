import axios from '@/libs/api.request'

export const getTableData = () => {
  return axios.request({
    url: 'get_table_data',
    method: 'get'
  })
}

export const getDragList = () => {
  return axios.request({
    url: 'get_drag_list',
    method: 'get'
  })
}

export const errorReq = () => {
  return axios.request({
    url: 'error_url',
    method: 'post'
  })
}

export const saveErrorLogger = info => {
  return axios.request({
    url: 'save_error_logger',
    data: info,
    method: 'post'
  })
}

export const uploadImg = formData => {
  return axios.request({
    url: 'upload',
    data: formData
  })
}

export const getOrgData = () => {
  return axios.request({
    url: 'get_org_data',
    method: 'get'
  })
}

export const getChart = (query, table) => {
  return axios.request({
    // url: 'http://10.119.159.121:5000/api/getchart',
    url: 'getchart',
    method: 'get',
    params: {
      query: query,
      table: table
    }
  })
}

export const read_dimitions = (filename,index) => {
  return axios.request({
    url: 'readDimitions',
    // url: 'http://10.119.159.121:5000/api/readDimitions',
    method: 'get',
    params: {
      filename: filename,
      index: index
    }
  })
}

export const readDatasets = () => {
  return axios.request({
    url: 'readDatas',
    // url: 'http://10.119.159.121:5000/api/readDatas',
    method: 'get'
  })
}

export const getSuggests = (query) => {
  return axios.request({
    url: 'getSuggests',
    // url: 'http://10.119.159.121:5000/api/readDatas',
    method: 'get',
    params: {
      query: query
    }
  })
}

export const getTop30 = (table, field) => {
  return axios.request({
    url: 'getTop30',
    // url: 'http://10.119.159.121:5000/api/readDatas',
    method: 'get',
    params: {
      table: table,
      field: field
    }
  })
}

