import numpy as np
import math
import pygame

X = 0
Y = 1
Z = 2

class vec3:
	def __init__(self, x, y, z):
		self.v = np.array([x, y, z])

	def unit_vector(self):
		v = self.v
		self.lenght_sq = v[X] * v[X]+ v[Y] * v[Y] + v[Z] * v[Z]
		self.lenght = np.sqrt(self.lenght_sq)
		if self.lenght == 0:
			return [0, 0, 0]
		return v / self.lenght

	def get_v(self):
		return self.v

class Ray:
	def __init__(self, origin:vec3, direction:vec3):
		self.origin = origin
		self.direction = direction

	def at(self, t):
		return self.origin.get_v() + t * self.direction.get_v()

def	hit_sphere(center:vec3, radius:float, ray:Ray):
	oc = ray.origin.get_v() - center.get_v()
	ray.direction.unit_vector()
	a = ray.direction.lenght_sq
	half_b = np.dot(oc, ray.direction.get_v())
	oc_v3 = vec3(oc[X], oc[Y], oc[Z])
	oc_v3.unit_vector()
	c = oc_v3.lenght_sq - radius * radius
	discriminant = half_b * half_b - a * c
	if discriminant < 0:
		return -1
	return (-half_b - np.sqrt(discriminant))/ a

def raycolor(ray: Ray) -> pygame.Color:
	t = hit_sphere(vec3(0, 0, -1), 0.5, ray)
	if (t > 0):
		n = ray.at(t) - np.array([0, 0, -1])
		N = vec3(n[X], n[Y], n[Z]).unit_vector()
		color = np.array([N[X] + 1, N[Y] + 1, N[Z] + 1]) * 255 * 0.5
		return pygame.Color(int(color[X]), int(color[Y]), int(color[Z]), 255)
	unit_direction = ray.direction.unit_vector()
	t = 0.5 * (unit_direction[Y] + 1)
	color = (1.0 - t) * vec3(1, 1, 1).get_v() + t * vec3(0.5, 0.7, 1).get_v()
	color *= 255
	return pygame.Color(int(color[X]), int(color[Y]), int(color[Z]), 255)


def render(width, height, canvas: pygame.Surface):
	aspect_ratio = width / height
	viewport_height = 2
	viewport_width = viewport_height * aspect_ratio
	focal_lenght = 1

	origin = vec3(0, 0, 0)
	horizontal = vec3(viewport_width, 0, 0)
	vertical = vec3(0, viewport_height, 0)

	lower_left = origin.get_v() - horizontal.get_v() / 2 - vertical.get_v() / 2 - np.array([0, 0, focal_lenght])
	for j in range(height):
		for i in range(width):
			u = i / width
			v = 1 - j / height
			direction = lower_left + u * horizontal.get_v() + v * vertical.get_v() - origin.get_v()
			ray = Ray(origin, vec3(direction[X], direction[Y], direction[Z]))
			color = raycolor(ray)
			#print(color)
			canvas.set_at((i, j), color)

