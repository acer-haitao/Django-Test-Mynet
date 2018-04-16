/**
 * Created by admin on 2018/4/14.
 */

function jszc_wage_pi_wh(pie_wage_wh,jobcount,pie_wh_wagename){
    var myChart = echarts.init(document.getElementById('main7'));
    var option = {
        title: {
            text: '武汉技术支持薪资统计--饼图',
            subtext:'职位总数:'+jobcount
        },
        tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        legend: {
            type: 'scroll',
            orient: 'vertical',
            right: 10,
            top: 50,
            bottom: 20,
            data: pie_wh_wagename,
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

        series: [
            {
                name: '访问来源',
                type: 'pie',
                radius: ['40%', '50%'],
                label: {
                    normal: {
                        formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                        backgroundColor: '#eee',
                        borderColor: '#aaa',
                        borderWidth: 1,
                        borderRadius: 4,

                        rich: {
                            a: {
                                color: '#999',
                                lineHeight: 22,
                                align: 'center'
                            },

                            hr: {
                                borderColor: '#aaa',
                                width: '100%',
                                borderWidth: 0.5,
                                height: 0
                            },
                            b: {
                                fontSize: 16,
                                lineHeight: 33
                            },
                            per: {
                                color: '#eee',
                                backgroundColor: '#334455',
                                padding: [2, 4],
                                borderRadius: 2
                            }
                        }
                    }
                },
                name: '岗位薪资及岗位数',
                type: 'pie',
                data: pie_wage_wh,
            }
        ]
    };
    // 使用刚指定的配置项和数据显示图表
    myChart.setOption(option);
}

