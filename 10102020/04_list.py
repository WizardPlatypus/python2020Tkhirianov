import turtle;

A = [(1, 10), (2, 20), (3,30)]
for angle, move in A:
    print(angle, move)
    turtle.left(angle)
    turtle.forward(move)
