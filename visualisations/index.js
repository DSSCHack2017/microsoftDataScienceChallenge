let APP
let WIDTH
let HEIGHT
let PADDING
let PATH_AREA
let DIMENSIONS
let ASPECT_RATIO
let STROKE_WIDTH

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

const getDimensions = data => {
	let dimensions = {
		height: {
			min: 0,
			max: 0
		},
		width: {
			min: 0,
			max: 0
		}
	}

	if (data.length > 0) {
		for (let point of data) {
			if (point) {
				if (point.x > dimensions.width.max) {
					dimensions.width.max = point.x
				}
				if (point.y > dimensions.height.max) {
					dimensions.height.max = point.y
				}
				if (point.x < dimensions.width.min) {
					dimensions.width.min = point.x
				}
				if (point.y < dimensions.height.min) {
					dimensions.height.min = point.y
				}
			}
		}
	}
	return dimensions
}

const drawAxis = () => {

	const axisGenerator = d3.line().x(d => d.x).y(d => d.y)

	APP.append("path")
	   .attr("d", axisGenerator([DIMENSIONS.bottomLeft, DIMENSIONS.topLeft]))
	   .attr("stroke", "white")
	   .attr("stroke-width", STROKE_WIDTH)
	APP.append("path")
	   .attr("d", axisGenerator([DIMENSIONS.bottomLeft, DIMENSIONS.bottomRight]))
	   .attr("stroke", "white")
	   .attr("stroke-width", STROKE_WIDTH)

	PATH_AREA = APP.append("g")

	APP.append("text")
	   .text("x-axis")
	   .attr("x", WIDTH - PADDING)
	   .attr("y", HEIGHT - PADDING)
	APP.append("text")
	   .text("y-axis")
	   .attr("x", PADDING)
	   .attr("y", PADDING)
}

const transformPoint = point => {
	const newPoint = {
		x: PADDING + (point.x * DIMENSIONS.plotWidth / DIMENSIONS.width),
		y: HEIGHT - PADDING - (point.y * DIMENSIONS.plotHeight / DIMENSIONS.height)
	}
	return newPoint
}

const drawPaths = () => {
	const lineGenerator = d3.line()
							.x(d => transformPoint(d).x)
							.y(d => transformPoint(d).y)
	APP.append("path")
	   .attr("d", lineGenerator(lineData))
	   .attr("stroke", "#0F608A")
	   .attr("stroke-width", STROKE_WIDTH)
	   .attr("fill", "none")

	lineData.map( point => {
		APP.append("circle")
			.attr("cx", transformPoint(point).x)
			.attr("cy", transformPoint(point).y)
			.attr("r", 3)
			.attr("fill", "#0F608A")
			.attr("stroke", "none")
			.on("click", () => {
				console.log("Ouch, don't click me!")
				d3.event.stopPropagation()
			})
	})
}

const flushPaths = () => {
	PATH_AREA.selectAll("*").remove()
}

const setup = () => {

	const viewSizes = getDimensions(lineData)

	APP = d3.select("#root")
	PADDING = 30
	ASPECT_RATIO = 720 / 480
	WIDTH = 720
	HEIGHT = WIDTH / ASPECT_RATIO
	STROKE_WIDTH = 1

	DIMENSIONS = {
		topLeft: {x: PADDING,y: PADDING},
		bottomRight: {x: WIDTH - PADDING,y: HEIGHT - PADDING},
		bottomLeft: {x:PADDING,y: HEIGHT - PADDING},

		width: viewSizes.width.max - viewSizes.width.min,
		height: viewSizes.height.max - viewSizes.height.min,

		plotWidth: WIDTH - 2 * PADDING,
		plotHeight: HEIGHT - 2 * PADDING
	}

	APP.attr("width", WIDTH)
	   .attr("height", HEIGHT)
	   .attr("preserveAspectRatio", "xMidYMid meet")
	   .attr("viewBox", `0 0 ${WIDTH} ${HEIGHT}`)

	drawAxis()

	drawPaths()

}

document.addEventListener("DOMContentLoaded", setup)