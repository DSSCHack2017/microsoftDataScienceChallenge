let APP
let WIDTH
let HEIGHT
let MARGINS
let PATH_AREA

const lineData = [
	{
		x: 1,
		y: 5
	},
	{
		x: 20,
		y: 20
	},
	{
		x: 40,
		y: 10
	},
	{
		x: 60,
		y: 40
	},
	{
		x: 80,
		y: 5
	},
	{
		x: 100,
		y: 60
	}
]

const lineGenerator = d3.line()
						.x(d => MARGINS.left + d.x)
						.y(d => HEIGHT - MARGINS.bottom  - d.y)

const axisGenerator = d3.line()
						.x(d => d.x)
						.y(d => d.y)

const drawAxis = () => {

	APP.attr("width", WIDTH)
	   .attr("height", HEIGHT)
	   .attr("preserveAspectRatio", "xMidYMid meet")
	   .attr("viewBox", `0 0 ${WIDTH} ${HEIGHT}`)

	PATH_AREA = APP.append("g")

	const xAxisCoords = [{x:MARGINS.right,y: HEIGHT - MARGINS.bottom},{x: MARGINS.right,y: MARGINS.top}]
	const xAxis = APP.append("path")
					 .attr("d", axisGenerator(xAxisCoords))
					 .attr("stroke", "white")
					 .attr("stroke-width", 2)
					 .attr("fill", "none")

	const yAxisCoords = [{x:MARGINS.right,y: HEIGHT - MARGINS.bottom},{x: WIDTH - MARGINS.left,y: HEIGHT - MARGINS.bottom}]
	const yAxis = APP.append("path")
					 .attr("d", axisGenerator(yAxisCoords))
					 .attr("stroke", "white")
					 .attr("stroke-width", 2)
					 .attr("fill", "none")

	const xLabel = "Width"
	const yLabel = "Height"

	APP.append("text")
	   .text(xLabel)
	   .attr("x", WIDTH - MARGINS.right)
	   .attr("y", HEIGHT - MARGINS.bottom)

	APP.append("text")
	   .text(yLabel)
	   .attr("x", 20)
	   .attr("y", MARGINS.top - 20)
}

const drawPaths = () => {
	PATH_AREA.append("path")
	   .attr("d", lineGenerator(lineData))
	   .attr("stroke", "red")
	   .attr("stroke-width", 2)
	   .attr("fill", "none")
	   .on("click", () => {
			console.log("Ouch, don't click me!")
			d3.event.stopPropagation()
	   })
}

const flushPaths = () => {
	PATH_AREA.selectAll("*").remove()
}

const setup = () => {

	APP = d3.select("#root")
	WIDTH = 720
	HEIGHT = 480
	MARGINS = {
		top: 40,
		right: 40,
		bottom: 40,
		left: 40
	}

	drawAxis()

	drawPaths()

}

document.addEventListener("DOMContentLoaded", setup)