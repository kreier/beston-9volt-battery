# Mandelbrot ASCII renderer (80x25)

width = 80
height = 25
max_iter = 50

# Characters from light to dense
chars = " .:-=+*#%@"

for y in range(height):
    for x in range(width):
        # Map pixel to complex plane
        რე = -2.0 + (x / width) * 3.0   # real part: -2.0 to +1.0
        იმ = -1.0 + (y / height) * 2.0  # imaginary: -1.0 to +1.0

        c = complex(რე, იმ)
        z = 0
        iteration = 0

        while abs(z) <= 2 and iteration < max_iter:
            z = z*z + c
            iteration += 1

        # Choose character based on iteration count
        if iteration == max_iter:
            char = "@"
        else:
            char = chars[iteration * len(chars) // max_iter]

        print(char, end="")
    print()
