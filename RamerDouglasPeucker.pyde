"""
 * Ramer-Douglas-Peucker Algorithm (v1.2.3)
 * GoToLoop & JeffThompson (2019/Aug/27)
 *
 * https://Discourse.Processing.org/t/reducing-points-in-polygon/13590/3
 *
 * https://en.Wikipedia.org/wiki/Ramer-Douglas-Peucker_algorithm
 * https://Karthaus.nl/rdp/js/rdp2.js
 *
 * https://Bl.ocks.org/GoToLoop/a5db257be4d7756a00220a3e97066dd5
 * https://www.OpenProcessing.org/sketch/747172
"""

from Calc import reducePolygon
from Data import loadCoordsXYAsPVectorsTuple

QTY, DIAM, BOLD = 12, 15, 2;
BG, FG, STROKE = -1, 0x64000000, 0xff0096FF

DEBUG = True

def setup():
    size(800, 600)
    smooth(), noLoop(), strokeWeight(BOLD)

    global coords, reduced

    coords = loadCoordsXYAsPVectorsTuple()
    if DEBUG: print "Polygon's original size: %d" % len(coords)

    reduced = reducePolygon(coords, QTY, DEBUG = DEBUG)
    if DEBUG: print "Polygon's final size: %d\n" % len(reduced)

    if DEBUG:
        txt, digits = '%s: %s', len(`max(0, len(reduced) - 1)`)
        for i, v in enumerate(reduced): print txt % (`i`.zfill(digits), v)


def draw():
    background(BG)
    drawPoints(coords)

    translate(width >> 1, 0)
    drawPoints(reduced)


def drawPoints(dots):
    if not dots: return

    noFill()
    stroke(STROKE)

    with beginClosedShape():
        for v in dots: vertex(v.x, v.y)

    fill(FG)
    noStroke()

    for v in dots: circle(v.x, v.y, DIAM)