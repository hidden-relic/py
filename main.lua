function love.draw()

local winWidth, winHeight = love.graphics.getDimensions()
winWidth, winHeight =
winWidth - 16, winHeight - 16

local rafter = {
    peak = {x = 8, y = 8},
    wall = {x = (winWidth * 0.75), y = (winWidth * 0.5)}
}

love.graphics.line(rafter.peak.x, rafter.peak.y, rafter.peak.x, rafter.peak.y + 12, rafter.wall.x, rafter.wall.y + 12, rafter.wall.x, rafter.wall.y, rafter.peak.x, rafter.peak.y)

end