<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dose Response Curves with D3.js</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        /* General styling */
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }

        h1 {
            text-align: center;
            margin: 20px 0;
            color: #444;
        }

        svg {
            display: block;
            margin: 0 auto;
            background-color: #fff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            border: 1px solid #ddd;
        }

        .tooltip {
            position: absolute;
            background-color: rgba(0, 0, 0, 0.8);
            color: #fff;
            border-radius: 5px;
            padding: 8px;
            font-size: 0.9em;
            pointer-events: none;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
        }

        /* Axis styling */
        .axis path,
        .axis line {
            fill: none;
            stroke: #bbb;
            shape-rendering: crispEdges;
        }

        .axis text {
            font-size: 12px;
            fill: #666;
        }

        /* Line styles */
        .line {
            fill: none;
            stroke-width: 2.5px;
        }

        /* Error bar styling */
        .error-bar {
            stroke-width: 1.5px;
            stroke-dasharray: 2, 2;
        }

        /* Circle styles */
        circle {
            cursor: pointer;
            stroke: #333;
            stroke-width: 1px;
        }

        circle:hover {
            stroke-width: 2px;
            stroke: #000;
        }

        /* Footer styling */
        footer {
            text-align: center;
            margin-top: 20px;
            font-size: 0.85em;
            color: #888;
        }

        footer a {
            color: #0073e6;
            text-decoration: none;
        }

        footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Dose Response Curves</h1>
    <svg id="chart" width="900" height="500"></svg>
    <div id="tooltip" class="tooltip" style="display: none;"></div>
    <script>
        const data = {
            irinotecan: [
                { concentration: 100, response: 1.73, error: 1.84 },
                { concentration: 25, response: 16.48, error: 1.24 },
                { concentration: 6.25, response: 23.63, error: 5.66 },
                { concentration: 1.5625, response: 56.32, error: 3.24 },
                { concentration: 0.390625, response: 111.28, error: 19.16 },
                { concentration: 0.09765625, response: 110.96, error: 29.31 },
                { concentration: 0.024414063, response: 114.76, error: 24.96 },
                { concentration: 0.006103516, response: 118.19, error: 17.14 },
            ],
            fluorouracil: [
                { concentration: 1000, response: 48.51, error: 2.72 },
                { concentration: 500, response: 60.83, error: 3.10 },
                { concentration: 250, response: 92.37, error: 6.55 },
                { concentration: 125, response: 106.10, error: 0.11 },
                { concentration: 62.5, response: 111.65, error: 2.22 },
                { concentration: 31.25, response: 119.82, error: 4.21 },
                { concentration: 15.625, response: 106.16, error: 3.53 },
                { concentration: 7.8125, response: 106.38, error: 0.16 },
            ]
        };

        const svg = d3.select("#chart");
        const width = 900;
        const height = 500;
        const margin = { top: 40, right: 40, bottom: 60, left: 60 };

        const x = d3.scaleLog()
            .domain([0.001, 1000])
            .range([margin.left, width - margin.right]);

        const y = d3.scaleLinear()
            .domain([0, 130])
            .range([height - margin.bottom, margin.top]);

        const color = d3.scaleOrdinal()
            .domain(["irinotecan", "fluorouracil"])
            .range(["#ff6384", "#36a2eb"]);

        // Add axes
        svg.append("g")
            .attr("transform", `translate(0,${height - margin.bottom})`)
            .call(d3.axisBottom(x).ticks(10, "~s"));

        svg.append("g")
            .attr("transform", `translate(${margin.left},0)`)
            .call(d3.axisLeft(y));

        // Add labels
        svg.append("text")
            .attr("x", width / 2)
            .attr("y", height - 10)
            .attr("text-anchor", "middle")
            .text("Concentration (µg/ml)");

        svg.append("text")
            .attr("transform", "rotate(-90)")
            .attr("x", -height / 2)
            .attr("y", 20)
            .attr("text-anchor", "middle")
            .text("Response (%)");

        const tooltip = d3.select("#tooltip");

        // Add lines and error bars
        Object.entries(data).forEach(([key, dataset]) => {
            const group = svg.append("g");

            // Add error bars
            group.selectAll(".error-bar")
                .data(dataset)
                .join("line")
                .attr("class", "error-bar")
                .attr("x1", d => x(d.concentration))
                .attr("x2", d => x(d.concentration))
                .attr("y1", d => y(d.response - d.error))
                .attr("y2", d => y(d.response + d.error))
                .attr("stroke", color(key));

            // Add the line
            const line = d3.line()
                .x(d => x(d.concentration))
                .y(d => y(d.response));
            group.append("path")
                .datum(dataset)
                .attr("d", line)
                .attr("class", "line")
                .attr("stroke", color(key))
                .attr("fill", "none");

            // Add circles for data points
            group.selectAll(".circle")
                .data(dataset)
                .join("circle")
                .attr("cx", d => x(d.concentration))
                .attr("cy", d => y(d.response))
                .attr("r", 5)
                .attr("fill", color(key))
                .on("mouseover", (event, d) => {
                    tooltip.style("display", "block")
                        .style("left", `${event.pageX + 10}px`)
                        .style("top", `${event.pageY - 10}px`)
                        .html(`
                            <strong>Drug:</strong> ${key}<br>
                            <strong>Concentration:</strong> ${d.concentration} µg/ml<br>
                            <strong>Response:</strong> ${d.response} ± ${d.error}
                        `);
                })
                .on("mouseout", () => tooltip.style("display", "none"));
        });
    </script>
</body>
</html>
