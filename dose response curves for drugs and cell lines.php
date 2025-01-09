<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dose Response Curves</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #444;
        }
        #chart-container {
            max-width: 900px;
            margin: 0 auto;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        canvas {
            display: block;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <h1>Dose Response Curves</h1>
    <div id="chart-container">
        <canvas id="doseResponseChart" width="800" height="400"></canvas>
    </div>

    <script>
        // Data for the two drugs
        const data = {
            labels: [100, 25, 6.25, 1.56, 0.39, 0.098, 0.024, 0.0061], // Concentrations for Irinotecan
            datasets: [
                {
                    label: 'Irinotecan',
                    data: [1.73, 16.48, 23.63, 56.32, 111.28, 110.96, 114.76, 118.19],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 2,
                    pointRadius: 5,
                    pointBackgroundColor: 'rgba(255, 99, 132, 1)',
                    pointHoverRadius: 7,
                    errorBars: [1.84, 1.24, 5.66, 3.24, 19.16, 29.31, 24.96, 17.14],
                },
                {
                    label: '5-Fluorouracil',
                    data: [48.51, 60.83, 92.37, 106.10, 111.65, 119.82, 106.16, 106.38],
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2,
                    pointRadius: 5,
                    pointBackgroundColor: 'rgba(54, 162, 235, 1)',
                    pointHoverRadius: 7,
                    errorBars: [2.72, 3.10, 6.55, 0.11, 2.22, 4.21, 3.53, 0.16],
                }
            ]
        };

        // Custom plugin to add error bars
        const errorBarPlugin = {
            id: 'errorBarPlugin',
            afterDatasetsDraw(chart) {
                const { ctx } = chart;
                chart.data.datasets.forEach((dataset, i) => {
                    if (dataset.errorBars) {
                        const meta = chart.getDatasetMeta(i);
                        meta.data.forEach((point, index) => {
                            const x = point.x;
                            const y = point.y;
                            const error = dataset.errorBars[index];
                            ctx.save();
                            ctx.beginPath();
                            ctx.strokeStyle = dataset.borderColor;
                            ctx.lineWidth = 1.5;
                            ctx.moveTo(x, y - error);
                            ctx.lineTo(x, y + error);
                            ctx.stroke();
                            ctx.beginPath();
                            ctx.moveTo(x - 5, y - error);
                            ctx.lineTo(x + 5, y - error);
                            ctx.stroke();
                            ctx.beginPath();
                            ctx.moveTo(x - 5, y + error);
                            ctx.lineTo(x + 5, y + error);
                            ctx.stroke();
                            ctx.restore();
                        });
                    }
                });
            }
        };

        // Config for the chart
        const config = {
            type: 'line',
            data: data,
            options: {
                responsive: true,
                plugins: {
                    tooltip: {
                        usePointStyle: true,
                        backgroundColor: 'rgba(0, 0, 0, 0.8)',
                        titleColor: '#fff',
                        bodyColor: '#fff',
                        borderWidth: 1,
                        borderColor: '#ccc',
                        callbacks: {
                            title: function (tooltipItems) {
                                return `Concentration: ${tooltipItems[0].label} µg/ml`;
                            },
                            label: function (tooltipItem) {
                                const dataset = data.datasets[tooltipItem.datasetIndex];
                                const value = dataset.data[tooltipItem.dataIndex];
                                const error = dataset.errorBars[tooltipItem.dataIndex];
                                return `${dataset.label}: ${value} ± ${error}`;
                            }
                        }
                    },
                    legend: {
                        position: 'top',
                    }
                },
                scales: {
                    x: {
                        type: 'logarithmic',
                        title: {
                            display: true,
                            text: 'Concentration (µg/ml)'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Response (%)'
                        }
                    }
                }
            },
            plugins: [errorBarPlugin]
        };

        // Render the chart
        const ctx = document.getElementById('doseResponseChart').getContext('2d');
        new Chart(ctx, config);
    </script>
</body>
</html>
