from scipy import misc
from tqdm import tqdm

IMAGE = 'ball.jpg'

T = [0, 255, 0]
S = [255, 0, 0]

def dist(x, y):
	return sum((x - y) ** 2)

def get_neighbours(i, j, max_i, max_j):
	result = []
	if i > 0:
		result.append((i - 1, j))
	if j > 0:
		result.append((i, j - 1))
	if (i + 1) < max_i:
		result.append((i + 1, j))		
	if (j + 1) < max_j:
		result.append((i, j  + 1))

	return result	

def flip(i, j, A, B):
	if (i, j) in A:
		A.remove((i, j))
		B.add((i, j))
	else:
		B.remove((i, j))
		A.add((i, j))

def cut(image):
	dim_x, dim_y, colors = image.shape
	A = set()
	B = {(i, j) for i in range(dim_x) for j in range(dim_y)}
	for _ in range(10):
		print len(A), len(B)
		changed = False
		for i in tqdm(range(dim_x), total=dim_x):
			for j in range(dim_y):
				if (i,j) in A:
					in_cut =  dist(image[i, j, : 3], S) 
					in_set =  dist(image[i, j, : 3], T) 
				else:
					in_set =  dist(image[i, j, : 3], S) 
					in_cut =  dist(image[i, j, : 3], T)

				for i_n, j_n in get_neighbours(i, j, dim_x, dim_y):
					dst = dist(image[i,j,:3], image[i_n, j_n,:3])
					if ((i,j) in A and (i_n, j_n) in B) or ((i,j) in B and (i_n, j_n) in A):
						in_cut += dst
					else:
						in_set += dst

				if in_set > in_cut:
					changed = True
					flip(i, j, A, B)

		if not changed:
			break

	return A, B


if __name__ == "__main__":
	image = misc.imread(IMAGE)
	dim_x, dim_y, colors = image.shape
	print "Loaded image of shape {x}, {y}".format(x=dim_x, y=dim_y) 

	A, B = cut(image)

	for i in range(dim_x):
		for j in range(dim_y):
			if (i, j) in A:
				image[i, j, 0] = min(255, image[i, j, 0] + 100)
				image[i, j, 1] = image[i, j, 1] / 3
				image[i, j, 2] = image[i, j, 2] / 3
			elif (i,j) in B:
				image[i, j, 0] = image[i, j, 0] / 3 
				image[i, j, 1] = min(255, image[i, j, 1] + 100)
				image[i, j, 2] = image[i, j, 2] / 3

	misc.imsave('out.png', image)
