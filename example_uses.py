from polynomial import poly
def main():
	poly1 = poly([2, 0, 4, -1, 0, 6])
	poly2 = poly([-1, -3, 0, 4.5])
	poly1.order()
	poly1.addition(poly2)
	(poly(poly1.sum)).represent("added")
	poly1.derivate()
	(poly(poly1.derivative)).represent("derivated")
	poly3 = poly(poly1.derivative)
	poly3.integrate(2)
	(poly(poly3.integral)).represent("integrated")
main()
