/**
 * Created by admin on 2018/4/14.
 */
function jszc_address_line_bj(jobcount_bj,address_bj,address_count_bj){
    var myChart = echarts.init(document.getElementById('main4'));
    var option = {
        title: {
            text: '北京技术支持职位区域统计分析--柱状图',
            subtext:'职位总数:'+jobcount_bj
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:[ '北京']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {},
                dataView : {show: true, readOnly: false},
                magicType : {show: true, type: ['line', 'bar']},
                restore : {show: true},
            }
        },
        xAxis: {
            type: 'category',
            data: address_bj
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name:'北京',
                type:'bar',
                step: 'middle',
                data:address_count_bj
            },
        ]
    };
    // 使用刚指定的配置项和数据显示图表
    myChart.setOption(option);
}

