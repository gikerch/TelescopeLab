# -*- coding: utf-8 -*-
# @Author   : Weizhou
# @Email    : 491315091@qq.com

import json
import os
import numpy as np
import pandas as pd
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS, cross_origin  # 导入包
# from pyecharts import Bar, Line, Pie
from pyecharts_javascripthon.api import TRANSLATOR

import argparse
import logging
parser = argparse.ArgumentParser()
# parser.add_argument('text', help = 'print some text') # 3
parser.add_argument('-d','--debug', type = bool, help = 'Output debug info or not')
args = parser.parse_args()
if args.debug:
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')
else:
    logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')


app = Flask(__name__)
CORS(app, resources=r'/*')
app.logger.error('ss')

def pie(df=None):
    option = {
        'title': {
            'text': '',
            'x': 'center'
        },
        'tooltip': {
            'trigger': 'item',
            'formatter': "{a} <br/>{b} : {c} ({d}%)",
        },
        'legend': {
            'data': [],
            'orient': 'vertical',
            'x': 'left',
            'y': 'center'
        },
        'series': [
            {
                'name': '',
                'type': 'pie',
                'data': [],
            }
        ]
    }
    list1, list2 = [], []
    dict3 = {"年份": ['2015', '2016', '2017', '2018'],
             "销量": [50, 100, 150, np.nan]}
    df = pd.DataFrame(dict3)
    df = df.fillna(0)
    for i in range(len(df)):
        list1.append(df.iloc[i, 0])
        list2.append(df.iloc[i, 1])
        key1 = df.columns[0]
        key2 = df.columns[1]
    title = "各{}的{}所占比重".format(key1, key2)
    option['title']['text'] = title
    option['legend']['data'] = list1
    list_data = []
    for i in range(len(list1)):
        list_data.append({'value': list2[i], 'name': list1[i]})
    option['series'][0]['data'] = list_data
    return option


def line(df=None):
    option = {
        'title': {
            'text': '',
            'x': 'center'
        },
        'xAxis': {
            'type': 'category',
            'name': '',
            'data': []
        },
        'yAxis': {
            'type': 'value',
            'name': ''
        },
        'toolbox': {
            'feature': {
                'dataZoom': {
                    'yAxisIndex': None
                },
                'mark': {'show': True},
                'dataView': {'show': True, 'readOnly': False},
                'magicType': {'show': True, 'type': ['line', 'bar']},
                'restore': {'show': True},
                'saveAsImage': {'show': True}
            }
        },
        'series': [
            {
                'name': '',
                'type': 'line',
                'data': [],
                'label': {
                    'normal': {
                        'show': True,
                        'position': 'top'
                    }
                }

            }
        ]
    }
    list1, list2 = [], []
    dict3 = {"年份": ['2015', '2016', '2017', '2018'],
             "销量": [50, 100, 150, np.nan]}
    df = pd.DataFrame(dict3)
    df = df.fillna(0)
    for i in range(len(df)):
        list1.append(df.iloc[i, 0])
        list2.append(df.iloc[i, 1])
        key1 = df.columns[0]
        key2 = df.columns[1]
    title = "{}随{}的变化情况".format(key2, key1)
    option['title']['text'] = title
    option['xAxis']['name'] = key1
    option['xAxis']['data'] = list1
    option['yAxis']['name'] = key2
    option['series'][0]['data'] = list2
    return option


def bar(intention=None,df=None):
    
    dict1 = {"学历":["初中及以下","高中/职高","中专/技术学校","大专","本科","研究生及以上"],"贷款逾期数":[10268,76583,4320,167760,43568,3405]}
    df = pd.DataFrame(dict1)
    df = df.fillna(0)
    df = df.sort_values(df.columns[1],ascending = False)

    text = '{}人数随{}分布中，最多为{}，最少为{}'.format(df.columns.tolist()[-1],df.columns.tolist()[0],df.iloc[0,-1],df.iloc[-1,-1])

    option = {
        'title' : {
            'text':'',
            'x':'center'
        },
        'xAxis': {
        'type': 'category',
        'name':'',
        'data': []
    },
        'yAxis': {
        'type': 'value',
        'name':''
        },
        'toolbox': {
            'feature': {
                'dataZoom': {
                    'yAxisIndex': None
                },
                'mark': {'show': True},
                'dataView': {'show': True, 'readOnly': False},
                'magicType': {'show': True, 'type': ['line', 'bar']},
                'restore': {'show': True},
                'saveAsImage': {'show': True}
            }
        },
        'tooltip': {
            'trigger': 'axis',
            'axisPointer':{
                'type': 'shadow'
            }
        },
        'series' : [
            {
                'name': '',
                'type': 'bar',
                'data':[],
                'label': {
                    'normal': {
                    'show': True,
                    'position': 'top'
                    }
                }

            }
        ]
    }
    list1,list2 = [],[]
    for i in range(len(df)):
        list1.append(df.iloc[i,0])
        list2.append(int(df.iloc[i,1]))
        key1 = df.columns.tolist()[0]
        key2 = df.columns.tolist()[1]
    title = "不同{}的{}对比".format(key1,key2)
    option['title']['text'] = title
    option['xAxis']['name'] = key1
    option['xAxis']['data'] = list1
    option['yAxis']['name'] = key2
    option['series'][0]['data'] = list2
    dict_return = {}
    dict_return['option'] = option
    dict_return['text'] = text
    return dict_return


def scatter(df=None):
    option = {
        'title': {
            'text': '',
            'x': 'center'
        },
        'xAxis': {
            'name': ''
        },
        'yAxis': {
            'name': ''
        },
        'toolbox': {
            'feature': {
                'dataZoom': {
                    'yAxisIndex': None
                },
                'mark': {'show': True},
                'dataView': {'show': True, 'readOnly': False},
                'magicType': {'show': True, 'type': ['line', 'bar']},
                'restore': {'show': True},
                'saveAsImage': {'show': True}
            }
        },
        'series': [
            {
                'name': '',
                'type': 'scatter',
                'data': []
            }
        ],
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'cross'
            }
        }
    }
    list1, list2 = [], []
    dict3 = {"投入金额": [40, 50, 70, 5], "销量": [50, 100, 150, np.nan]}
    df = pd.DataFrame(dict3)
    df = df.fillna(0)
    for i in range(len(df)):
        list1.append(df.iloc[i, 0])
        list2.append(df.iloc[i, 1])
        key1 = df.columns[0]
        key2 = df.columns[1]
    title = "不同{}的{}对比".format(key1, key2)
    option['title']['text'] = title
    option['xAxis']['name'] = key1
    option['yAxis']['name'] = key2
    list_data = []
    for i in range(len(list1)):
        list_data.append([int(list1[i]), int(list2[i])])
    option['series'][0]['data'] = list_data
    return option


def funnel(df=None):
    option = {
        'title': {
            'text': '',
            'text': '',
            'x': 'center'
        },
        'tooltip': {
            'trigger': 'item',
            'formatter': "{a} <br/>{b} : {c}"
        },
        'toolbox': {
            'feature': {
                'dataZoom': {
                    'yAxisIndex': None
                },
                'mark': {'show': True},
                'dataView': {'show': True, 'readOnly': False},
                'magicType': {'show': True, 'type': ['line', 'bar']},
                'restore': {'show': True},
                'saveAsImage': {'show': True}
            }
        },

        'legend': {
            'data': [],
            'orient': 'vertical',
            'x': 'left',
            'y': 'center',
        },
        'calculable': True,
        'series': [
            {
                'name': '',
                'type': 'funnel',
                'sort': 'descending',
                'label': {
                    'normal': {
                        'show': True,
                        'position': 'inside'
                    },
                    'emphasis': {
                        'textStyle': {
                            'fontSize': 20
                        }
                    }
                },
                'data': []
            }
        ]
    }
    list1, list2 = [], []
    dict3 = {"状态": ['展现', '点击', '访问', '咨询', '订单'],
             "人数": [200, 160, 90, 80, 30]}
    df = pd.DataFrame(dict3)
    df = df.fillna(0)
    for i in range(len(df)):
        list1.append(df.iloc[i, 0])
        list2.append(df.iloc[i, 1])
        key1 = df.columns[0]
        key2 = df.columns[1]
    title = "不同{}的{}转化情况".format(key1, key2)
    option['title']['text'] = title
    option['legend']['data'] = list1
    list_data = []
    for i in range(len(list1)):
        dict_temp = {}
        dict_temp['value'] = int(list2[i])
        dict_temp['name'] = list1[i]
        list_data.append(dict_temp)
    option['series'][0]['data'] = list_data
    return option


def stacked_line(df=None):
    option = {
        'title': {
            'text': ''
        },
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'cross',
            }
        },
        'legend': {
            'data': []
        },
        'toolbox': {
            'feature': {
                # 'dataZoom': {
                #     'yAxisIndex': None
                # },
                'mark': {'show': True},
                'dataView': {'show': True, 'readOnly': False},
                'magicType': {'show': True, 'type': ['line', 'bar']},
                'restore': {'show': True},
                'saveAsImage': {'show': True}
            }
        },
        'xAxis': [
            {
                'type': 'category',
                'boundaryGap': False,
                'data': []
            }
        ],
        'yAxis': [
            {
                'type': 'value'
            }
        ],
        'series': []
    }
    columns = ['邮件营销', '联盟广告', '视频广告', '直接访问']
    index = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

    list_raw = [[100, 50, 200, 350, 400, 50, 45],
                [400, 500, 600, 350, 500, 300, 400],
                [200, 300, 350, 150, 50, 100, 400],
                [100, 50, 200, 300, 200, 100, 250]]
    df = pd.DataFrame(list_raw, dtype='int')
    df = df.T
    df = df.fillna(0)
    df.index = index
    df.columns = columns
    title = "堆叠区域图"
    option['title']['text'] = title
    option['legend']['data'] = df.columns.tolist()
    option['xAxis'][0]['data'] = df.index.tolist()

    for i in range(len(df.columns)):
        dict_temp = {}
        dict_temp['name'] = df.columns[i]
        dict_temp['type'] = 'line'
        dict_temp['stack'] = '总量'
        dict_temp['areaStyle'] = {}
        data_temp = df.iloc[:, i].values.tolist()
        dict_temp['data'] = data_temp
        if i == len(df.columns)-1:
            dict_temp['label'] = {'normal': {
                'show': True, 'position': 'top'}}
        option['series'].append(dict_temp)
    return option


def box(df = None):
    option = {
        'title': {
            'text': '箱线图',
            'x':'center'
        },
        'tooltip' : {
            'trigger': 'axis',
            'axisPointer': {
              'type': 'cross',
                'label': {
                    }
                }
            },
        'toolbox': {
            'feature': {
                'dataZoom': {
                    'yAxisIndex': None
                },
                'mark' : {'show': True},
                'dataView' : {'show': True, 'readOnly': False},
                'magicType': {'show': True, 'type': ['line', 'bar']},
                'restore' : {'show': True},
                'saveAsImage' : {'show': True}
            }
        },
        'xAxis': {
            'data': []
        },
        'yAxis': {},
        'series': [{
            'type': 'k',
            'data': []
        }]
    }
    columns = ['周一','周二','周三','周四','周五','周六','周日']

    list_raw = [[100,50,200,350,400,50,45],\
                [400,500,600,350,500,300,400],\
                [200,300,350,150,50,100,400],\
                [100,50,200,300,200,100,250]]
    df = pd.DataFrame(list_raw)
    df = df.fillna(0)
    df.columns = columns
    option['xAxis']['data'] = df.columns.tolist()
    option['series'][0]['data'] = df.values.tolist()
    return option
# def Gauge():
#     option = {
#         'tooltip': {
#             'formatter': "{a} <br/>{b} : {c}%"
#         },
#         'toolbox': {d
#             'feature': {
#                 'restore': {},
#                 'saveAsImage': {}
#             }
#         },
#         'series': [
#             {
#                 'name': '业务指标',
#                 'type': 'gauge',
#                 'detail': {'formatter': '{value}%'},
#                 'data': [{'value': 50, 'name': '完成率'}]
#             }
#         ]
#     }
#   return option

#仪表盘
def gauge(data=0.45):
    option = {
        'title': {
            'text': '仪表盘',
            'subtext': '',
            'left': 'center',
            'padding': [140, 0],
            'link': 'http://www.baidu.com'
        },
        'backgroundColor': '',
        'tooltip': {
        },
        'toolbox': {
            'feature': {
                'restore': {},
                'saveAsImage': {}
            }
        },
        'series': [{
            'axisLine': {
                'show': True,
                'lineStyle': {
                    'color': [
                        [0.2, '#FFB90F'],
                        [0.4, '#FFA500'],
                        [0.6, '#FF7F00'],
                        [0.8, '#FF4500'],
                        [1,'#EE0000']
                    ],
                    'width': 30
                }
            },
            'axisTick': {
                'show': True
            },
            'axisLabel': {
                'distance': 6,
                'textStyle': {
                    'color': 'auto'
                }
            },
            'itemStyle': {
                'normal': {
                    'color': 'auto'
                }
            },
            'radius': '45%',
            'pointer': {
                'width': 10
            },
            'title': {
                'offsetCenter': [0, '100%']
            },
            'detail': {
                'textStyle': {
                    'fontWeight': 'bolder',
                    'fontSize': 23,
                    'color': 'black'
                },
                'offsetCenter': [0, '58%'],
                'formatter': '{value}万\n(5048人)'
            },
            'min': 0,
            'max': 1,
            'name': '米类仪表盘',
            'type': 'gauge',
            'show': 'false',
            'splitNumber': 10,

            'data': [{
                'value': '',
                'name': '月目标900吨，月累环比下降20%'
            }]
        }]
    }
    option['series'][0]['data'][0]['value'] = data
    return option

#桑吉图
def sankey(df=None):
    option = {
        'title': {
            'text': '桑吉图',
            'subtext': '',
            'left': 'center',
        },
        'tooltip': {
        },
        'toolbox': {
            'feature': {
                'restore': {},
                'saveAsImage': {}
            }
        },
        'series': {
            'type': 'sankey',
            'layout':'none',
            'data': [],
            'links': []
        }
    }
    list1 = [['a','a1',5],['a','a2',3],['b','b1','8'],['a','b1',3],['b1','a1',1],['b1','c',2]]
    df = pd.DataFrame(list1,columns=['source','target','value'])
    set1 = set()
    for item in df.iloc[:,0]:
        #if item not in set1:
        set1.add(item)
    for item in df.iloc[:,1]:
        #if item not in set1:
        set1.add(item)
    for item in set1:
        dict_temp1 = {}
        dict_temp1['name'] = item
        option['series']['data'].append(dict_temp1)

    for i in range(len(df)):
        dict_temp2 = {}
        dict_temp2['source'] = df.iloc[i,0]
        dict_temp2['target'] = df.iloc[i,1]
        dict_temp2['value'] = df.iloc[i,2]
        option['series']['links'].append(dict_temp2)
    return option


@app.route('/api/upload', methods=['GET', 'POST'])
def upload():
    f = request.files['file']
    print(f.filename)
    savepath = open('./datasets/'+f.filename, 'wb')
    f.save(savepath)
    print('good')
    return 'GOOD'


@app.route('/api/getchart', methods=['GET', 'POST'])
def getchart():
    # text = request.form['payload']
    query = request.args.get('query')
    table = request.args.get('table')
    print('选定的数据集为：%s' % table)
    print('前端传回的查询语句为：%s' % query)

    print('开始调用nlp解析')
    try:
        print('nlp解析成功')
    except Exception as e:
        print('nlp解析失败')
    print('开始读取数据集%s' % table)
    print('生成图表配置')
    print('前端图表渲染')

    l = []
    d = {}
    if query == 'pie':
        d = {'chartType': 'pie',
             'Chartoption': pie()
             }
    if query == 'pie3':
        d = {'chartType': 'pie',
             'Chartoption': pie()
             }
        l.append(d)
    
    
    elif query == 'bar':
        d = {'chartType': 'bar',
           'Chartoption': bar()
           }
    elif query == 'count':
        d = {'chartType': 'count',
           'Chartoption': 23
           }
    elif query == 'count1':
        d = {'chartType': 'count',
           'Chartoption': 39
           }
    elif query == 'line':
        d = {'chartType': 'line',
           'Chartoption': line()
           }
    elif query == 'scatter':
        d = {'chartType': 'scatter',
             'Chartoption': scatter()
             }
    elif query == 'Gauge':
        d = {'chartType': 'scatter',
             'Chartoption': Gauge()
             }
    elif query == 'funnel':
        d = {'chartType': 'funnel',
             'Chartoption': funnel()
             }
    elif query == 'stacked_line':
        d = {'chartType': 'stacked_line',
             'Chartoption': stacked_line()
             }
    elif query == 'box':
        d = {'chartType': 'box',
             'Chartoption': box()
             }
    elif query == 'gauge':
        d = {'chartType': 'gauge',
             'Chartoption': gauge()
             }
    elif query == 'sankey':
        d = {'chartType': 'sankey',
             'Chartoption': sankey()
             }
    # elif query == 'count':
    #     d = {'chartType': 'count',
    #          'Chartoption': 

    #          }
    # 多图
    l.append(d)
    l.append({'chartType': 'scatter',
                'Chartoption': scatter()
                })
    # elif query == 'pie3':
    #     d = {'chartType': 'pie',
    #          'Chartoption': pie()
    #          }
    #     l.extend([d,d,d])

    #     l.append({'chartType': 'scatter',
    #             'Chartoption': scatter()
    #             })
    #     l.append({'chartType': 'scatter',
    #             'Chartoption': scatter()
    #             })
    # elif query == 'pie4':
    #     d = {'chartType': 'pie',
    #          'Chartoption': pie()
    #          }
    #     l.append(d)
    #     l.append({'chartType': 'scatter',
    #             'Chartoption': scatter()
    #             })
    #     l.append({'chartType': 'scatter',
    #             'Chartoption': scatter()
    #             })
    #     l.append({'chartType': 'scatter',
    #             'Chartoption': scatter()
    #             })
    
    
    # l.append({'chartType': 'pie',
    #          'Chartoption': pie()
    #          })
    # l.append({'chartType': 'pie',
    #          'Chartoption': pie()
    #          })
    # l.append({'chartType': 'pie',
    #          'Chartoption': pie()
    #          })
    # l.append(d)

    response = make_response(jsonify(l))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return jsonify(l)


@app.route('/api/readDatas', methods=['GET'])
def readDatas():
    filenames = [f for f in os.listdir('./datasets') if f.endswith('.csv')]
    print(filenames)
    d = {}
    d['filename'] = filenames
    response = make_response(jsonify(d))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return jsonify(d)

# 获取前30个字段值
@app.route('/api/getTop30', methods=['GET'])
def getTop30():
    table = request.args.get('table')
    field = request.args.get('field')
    # 直接读会报错
    df = pd.read_csv(open(r'./datasets/'+table),sep=',',skiprows=3)
    values = '、'.join(df.groupby([field])[field].count().sort_values()[:30])
    # if int(index) == -1:
    #     index = len(df.columns)+1
    # dimitions = df.columns.tolist()[:int(index)]
    # print(dimitions)

 
    d = {}
    d['values'] = values
    response = make_response(jsonify(d))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return jsonify(d)

# 获取字段
@app.route('/api/readDimitions', methods=['GET'])
def readDimitions():

    filename = request.args.get('filename')
    index = request.args.get('index')
    # 直接读会报错
    # df = pd.read_csv(open(r'./datasets/'+filename),sep=',',skiprows=3)
    # if int(index) == -1:
    #     index = len(df.columns)+1
    # dimitions = df.columns.tolist()[:int(index)]
    # print(dimitions)
    logging.debug("the filename is :"+filename)
    dimitions = [{'type':'md-globe','name':'出生地'},
                 {'type':'md-calendar','name':'出生日期'},
                 {'type':'md-stats','name':'学历'},
                 {'type':'logo-yen','name':'年收入'}]
    d = {}
    d['dimitions'] = dimitions
    response = make_response(jsonify(d))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return jsonify(d)

@app.route('/api/logout', methods=['GET'])
def logout():

    d = {}
    d['code'] = 200
    d['data'] = None
    d['msg'] = ''
    response = make_response(jsonify(d))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return jsonify(d)

@app.route('/api/get_info', methods=['GET'])
def get_info():

    d = {}
    d['code'] = 200
    d['access'] = ['admin']
    d['avator'] = 'https://file.iviewui.com/dist/a0e88e83800f138b94d2414621bd9704'
    d['user_id'] = '14138'
    d['user_name'] = 'iview_admin'
    d['msg'] = ''
    response = make_response(jsonify(d))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return jsonify(d)


# 获取搜索建议
@app.route('/api/getSuggests', methods=['GET'])
def getSuggests():
    query = request.args.get('query')
    logging.debug("the query is :"+query)
    print(query)
    suggestsList = ['我是搜索建议0','我是搜索建议1','我是搜索建议2']
    print(suggestsList)
    d = {}
    d['suggestsList'] = suggestsList
    response = make_response(jsonify(d))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return jsonify(d)

@app.route('/api/login', methods=['GET','POST'])
def login():
    d = {}
    d['code'] = 200
    d['data'] = {'token': "jsfuirns94nkjskjjd9dsfknfds"}
    d['msg'] = ''
    print('login')
    response = make_response(jsonify(d))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return jsonify(d)
app.run(port=5000, debug=True)
