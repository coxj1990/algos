def intersection(r1, r2):
    x = min(r1.x2, r2.x2) - max(r1.x1, r2.x1)
    y = min(r1.y2, r2.y2) - max(r1.y1, r2.y1)
    if x <= 0 or y <= 0:
        return 0
    return x * y
