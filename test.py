import math
import pygame as vec

# Angle in degrees
angle = 30

# Convert to radians (optional, if needed)
angle_in_radians = math.radians(angle)

# Create the direction vector
direction_vector = vec.Vector2(
    math.cos(angle_in_radians),
    math.sin(angle_in_radians)
)

print(direction_vector)  # Output: (0.8660254037844386, 0.5)
