google.charts.load('current', {
    packages: ['corechart', 'bar']
});

google.charts.setOnLoadCallback(drawStuff);

function drawStuff() {
    var data = new google.visualization.arrayToDataTable([
        ['Mes', 'Puntuacion'],
        ['Enero', 12],
        ['Febrero', 19],
        ['Marzo', 3],
        ['Abril', 5],
        ['Mayo', 2]
    ]);

    var options = {
        title: 'Puntuacion Mensuales',
        chartArea: {
            width: '50%'
        },
        hAxis: {
            title: 'Puntuacion Total',
            minValue: 0
        },
        vAxis: {
            title: 'Meses'
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}


