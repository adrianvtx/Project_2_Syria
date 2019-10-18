
// function buildCharts() { 
  let graphdata = "/syria";
  d3.json(graphdata).then(function (data) {
    
    let names = data.data_id;
    let startDate = data.event_date.slice(1)[0];
    let endDate = data.event_date.slice(-1)[0];
    let dates = data.event_date;
    let fatalities = data.fatalities

    console.log(startDate);
    console.log(endDate);
    console.log(dates);

    var trace1 = {
        type: "scatter",
        mode: "lines",
        name: "fatalities",
        x: dates,
        y: fatalities,
        line: {
            color: "#17BECF"
        }
    };

    // Candlestick Trace
    // var trace2 = {
    //   type: "candlestick",
    //   x: dates,
    //   high: highPrices,
    //   low: lowPrices,
    //   open: openingPrices,
    //   close: closingPrices
    // };

    var data1 = [trace1];
    var layout = {
        title: "Olympic trends over the years",
        xaxis: {
            range: [startDate, endDate],
               type: "date"
            },
            yaxis: {
                autorange: true,
                type: "linear"
            },
    };
    Plotly.newPlot("plot", data1, layout)
});
// }
