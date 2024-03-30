# My GitHub Page

This is my GitHub page with interactive Plotly graphs.

## Graph 1

<div id="graph1"></div>

<script src=Histogram.html"></script>
<script>
    var data = [{
        x: [1, 2, 3, 4],
        y: [10, 15, 13, 17],
        type: 'scatter'
    }];

    var layout = {
        title: 'My Plotly Graph',
        xaxis: { title: 'X Axis' },
        yaxis: { title: 'Y Axis' }
    };

    Plotly.newPlot('graph1', data, layout);
</script>
