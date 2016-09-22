from scipy import misc
from tqdm import tqdm

IMAGE = 'plane.jpg'

T = [100, 120, 200]
S = [120, 120, 120]

def cut(image):
	dim_x, dim_y, colors = image.shape
	A = set()
	B = {(i, j) for i in range(dim_x) for j in range(dim_y)}
	for _ in range(10):
		...

	return A, B


if __name__ == "__main__":
	image = misc.imread(IMAGE)
	dim_x, dim_y, colors = image.shape
	print "Loaded image of shape {x}, {y}".format(x=dim_x, y=dim_y) 

	A, B = cut(image)

	for i in range(dim_x):
		for j in range(dim_y):
			if (i, j) in A:
				image[i, j, 0] = image[i, j, 0] * 2 + 100 
				image[i, j, 1] = image[i, j, 1] / 3
				image[i, j, 2] = image[i, j, 2] / 3
			elif (i,j) in B:
				image[i, j, 0] = image[i, j, 0] / 3 
				image[i, j, 1] = image[i, j, 1] * 2 + 100
				image[i, j, 2] = image[i, j, 2] / 3

	misc.imsave('out.png', image)
