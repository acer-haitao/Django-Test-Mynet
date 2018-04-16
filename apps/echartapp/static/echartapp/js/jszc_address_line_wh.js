/**
 * Created by admin on 2018/4/14.
 */

function jszc_address_line(jobcount,address,address_count){
    var myChart = echarts.init(document.getElementById('main5'));
    var option = {
        title: {
            text: '武汉技术支持职位区域及数量分析--柱状图',
            subtext:'职位总数:'+jobcount
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:['武汉']
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
            data: address
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name:'武汉',
                type:'bar',
                step: 'start',
                data:address_count
            }
        ]
    };
    // 使用刚指定的配置项和数据显示图表
    myChart.setOption(option);
}

