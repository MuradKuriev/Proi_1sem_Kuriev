__all__ = ['triangle_perimeter', 'triangle_area']
def triangle_perimeter(a=7, b=2, c=8):
    return a+b+c
def triangle_area(a=7, b=2, c=8):
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5