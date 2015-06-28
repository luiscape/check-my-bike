//
// Generate a time-series chart based on a station
// id and a date.
//
// Author: Luis Capelo | luiscape@gmail.com
//


//
// Two parameters to fetch data: station id and date.
//
var id = 433
var today = moment().subtract(1, 'days').format('YYYY-MM-DD')
var api_query = 'api/station_processeds?id=' + id + '&day=' + today

//
// Fetch data from the processed data endpoint.
//
d3.json(api_query, function(data) {

    var graph_data = data['resources']

    //
    // Parse data into a datetime object.
    //
    parseDate = d3.time.format("%Y-%m-%d %H:%M").parse
    graph_data.forEach(function(item) { item['executionTime'] = parseDate(item['executionTime']) })

    //
    // Create chart.
    //
    MG.data_graphic({
        data: graph_data,
        width: 400,
        height: 200,
        right: 0,
        animate_on_load: true,
        target: document.getElementById('chart_example'),
        x_accessor: 'executionTime',
        y_accessor: 'availableBikesRatio',
        area: false,
        x_axis: false,
        y_axis: true
    })
})

function CreateSparkLike(station_id) {

    //
    // Two parameters to fetch data: station id and date.
    //
    var today = moment().subtract(1, 'days').format('YYYY-MM-DD')
    var api_query = 'api/station_processeds?id=' + station_id + '&day=' + today

    //
    // Fetch data from the processed data endpoint.
    //
    d3.json(api_query, function(data) {

        var graph_data = data['resources']

        //
        // Parse data into a datetime object.
        //
        parseDate = d3.time.format("%Y-%m-%d %H:%M").parse
        graph_data.forEach(function(item) {
            item['executionTime'] = parseDate(item['executionTime'])
        })

        //
        // Create chart.
        //
        MG.data_graphic({
                    data: graph_data,
                    width: 400,
                    height: 200,
                    right: 0,
                    animate_on_load: true,
                    target: document.getElementById('chart_example'),
                    x_accessor: 'executionTime',
                    y_accessor: 'availableBikesRatio',
                    area: false,
                    x_axis: false,
                    y_axis: true
                })

        //
        // Change the latest numbers.
        //
        document.getElementById('bike-status-number').innerHTML = graph_data[0]['availableBikes']
        document.getElementById('dock-status-number').innerHTML = graph_data[0]['availableDocks']

    })
}
