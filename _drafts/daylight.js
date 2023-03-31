const lat = cb_obj.value
const x = source.data.x
const phi = Math.pi * 23.45 / 180
const y = Array.from(x, (x) => 2 / 365 * 24 * 60 * phi * Math.cos(x) * Math.tan(lat) /
    Math.pow(Math.cos(phi * Math.sin(x)), 2) /
    Math.sqrt(1 - Math.pow(Math.tan(lat) * Math.tan(phi * Math.sin(x)), 2)))
