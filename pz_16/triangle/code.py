__all__ = ["triangle_perimeter", "triangle_area"]
d_a, d_b, d_c = 7, 2, 8

def triangle_perimeter(a=d_a,b=d_b,c=d_c):
    return (a + b + c) / 2
def triangle_area(a=d_a,b=d_b,c=d_c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5