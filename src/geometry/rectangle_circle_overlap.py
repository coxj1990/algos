def overlaps(rect, circle):
    x1, x2 = rect.x1 - circle.x, rect.x2 - circle.x
    y1, y2 = rect.y1 - circle.y, rect.y2 - circle.y
    xsq = min(x1**2, x2**2) if x1 * x2 > 0 else 0
    ysq = min(y1**2, y2**2) if y1 * y2 > 0 else 0
    return xsq + ysq <= circle.r**2
