/**
 * Created by admin on 2018/4/14.
 */

function jszc_wage_line_bj(wage_name_bj,wage_bj,jobcount_bj){
    var myChart = echarts.init(document.getElementById('main6'));
    var option = {
        title: {
            text: '北京技术支持职位薪资及数量分析--折线图',
            subtext:'职位总数:'+jobcount_bj,
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:['北京']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },

        toolbox: {
            feature: {

                dataZoom : {
                    show : true,
                    title : {
                        dataZoom : '区域缩放',
                        dataZoomReset : '区域缩放后退'
                    }
                },
                saveAsImage : {
                    show : true,
                    title : '保存为图片',
                    type : 'png',
                    lang : ['点击保存']
                },
                dataView : {show: true, readOnly: false},
                magicType : {show: true, type: ['line', 'bar','pie']},
                restore : {show: true},
            }
        },
        xAxis: {
            type: 'category',
            data: wage_name_bj,
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name:'北京',
                type:'line',
                step: 'start',
                data:wage_bj,
            }
        ]
    };
    // 使用刚指定的配置项和数据显示图表
    myChart.setOption(option);
}

