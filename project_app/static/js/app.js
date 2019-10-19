// Calculate a rolling average for an array
function rollingAverage(arr, windowPeriod = 10) {
    // rolling averages array to return
    let averages = [];

    // Loop through all of the data
    for (let i = 0; i < arr.length - windowPeriod + 1; i++) {
        // calculate the average for a window of data
        let sum = 0;
        for (let j = 0; j < windowPeriod; j++) {
            sum += arr[i + j];
        }
        // calculate the average and push it to the averages array
        averages.push(sum / windowPeriod);
    }
    return averages;
}



function buildChart1() {
    let graphdata = "/syria";
    d3.json(graphdata).then(function (data) {

        let names = data.data_id;
        let startDate = data.event_date.slice(1)[0];
        let endDate = data.event_date.slice(-1)[0];
        let dates = data.event_date;
        let fatalities = data.fatalities
        let rollingPeriod = 30;
        let rollingAvg = rollingAverage(fatalities, rollingPeriod);

        let trace1 = {
            type: "scatter",
            mode: "lines",
            name: "Fatalities",
            x: dates,
            y: fatalities,
        };

        let trace2 = {
            type: "scatter",
            mode: "lines",
            name: "Rolling Avg. Fatalities",
            x: dates.slice(0, dates.length - rollingPeriod),
            y: rollingAvg
        };

        let data1 = [trace1, trace2];
        let layout = {
            xaxis: {
                range: [startDate, endDate],
                type: "date"
            },
            yaxis: {
                autorange: true,
                type: "linear"
            },
            width: 1000,
            height: 500,
        };
        Plotly.newPlot("Fatalities", data1, layout)

    });
}


function buildChart2() {
    let graphdata2 = "/syria2";
    d3.json(graphdata2).then(function (data) {

        // let admin = data.admin1
        // let fatalities = data.fatalities
        // let sub_event_type = Object.values(data.sub_event_type);

        // console.log(data.Idleb_fatalities);
        // console.log(fatalities);
        // console.log(sub_event_type);
        // console.log(admin);


        // let data2 = [{
        //     type: 'bar',
        //     x: fatalities,
        //     y: sub_event_type,
        //     orientation: 'h'
        // }];

        let trace1 = {
            y: data.Idleb_fatalities,
            x: data.Idleb_sub_event_type,
            name: data.Idleb_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let trace2 = {
            y: data.Hama_fatalities,
            x: data.Hama_sub_event_type,
            name: data.Hama_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let trace3 = {
            y: data.DeirezZor_fatalities,
            x: data.DeirezZor_sub_event_type,
            name: data.DeirezZor_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let trace4 = {
            y: data.AlHasakeh_fatalities,
            x: data.AlHasakeh_sub_event_type,
            name: data.AlHasakeh_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let trace6 = {
            y: data.ArRaqqa_fatalities,
            x: data.ArRaqqa_sub_event_type,
            name: data.ArRaqqa_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let trace7 = {
            y: data.Dara_fatalities,
            x: data.Dara_sub_event_type,
            name: data.Dara_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let trace8 = {
            y: data.AsSweida_fatalities,
            x: data.AsSweida_sub_event_type,
            name: data.AsSweida_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let trace9 = {
            y: data.Homs_fatalities,
            x: data.Homs_sub_event_type,
            name: data.Homs_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let trace10 = {
            y: data.RuralDamascus_fatalities,
            x: data.RuralDamascus_sub_event_type,
            name: data.RuralDamascus_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let trace11 = {
            y: data.Aleppo_fatalities,
            x: data.Aleppo_sub_event_type,
            name: data.Aleppo_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let trace12 = {
            y: data.Damascus_fatalities,
            x: data.Damascus_sub_event_type,
            name: data.Damascus_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let trace13 = {
            y: data.Quneitra_fatalities,
            x: data.Quneitra_sub_event_type,
            name: data.Quneitra_admin1.slice(1)[0],
            //    orientation: 'h',
            //    marker: {
            //        color: 'rgba(55,128,191,0.6)',
            //        width: 1
            //    },
            type: 'bar'
        };

        let trace14 = {
            y: data.Lattakia_fatalities,
            x: data.Lattakia_sub_event_type,
            name: data.Lattakia_admin1.slice(1)[0],
            //    orientation: 'h',
            //    marker: {
            //        color: 'rgba(55,128,191,0.6)',
            //        width: 1
            //    },
            type: 'bar'
        };

        let trace15 = {
            y: data.Tartous_fatalities,
            x: data.Tartous_sub_event_type,
            name: data.Tartous_admin1.slice(1)[0],
            // orientation: 'h',
            // marker: {
            //     color: 'rgba(55,128,191,0.6)',
            //     width: 1
            // },
            type: 'bar'
        };

        let data3 = [trace1, trace2, trace3, trace4,
            trace6, trace7, trace8, trace9, trace10,
            trace11, trace12, trace13, trace14, trace15
        ]

        let layout2 = {
            height: 500,
            xaxis: {
                automargin: true
            },
            barmode: 'relative',
        };


        Plotly.newPlot('plot1', data3, layout2);
    });
}

function init() {
    buildChart1();
    buildChart2();
}

init();