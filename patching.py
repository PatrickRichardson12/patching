from imagesearch import *
import time

def elimate_duplicates(results):
	for x in range(len(results)):
		for y in range(len(results[x])):
			results[x][y]['location'] = list(results[x][y]['location'])
			newArr0 = []
			newArr1 = []
			locations = list(results[x][y]['location'])
			#print(locations)
			for i in range(len(locations[0])):
				add = True
				for j in range(len(newArr0)):
					if ((newArr0[j] - locations[0][i] < tolerance and newArr0[j] - locations[0][i] > tolerance * -1) and (newArr1[j] - locations[1][i] < tolerance and newArr1[j] - locations[1][i] > tolerance * -1)):
						add = False
						break
				if (add):
					newArr0.append(locations[0][i])
					newArr1.append(locations[1][i])
			results[x][y]['location'][0] = newArr0
			results[x][y]['location'][1] = newArr1
	return results

def find_hierarchy(results):
	massive_Array =  [[0] * board_width for i in range(board_height)]
	index0 = 0 
	index1 = 0
	while (True):
		lowestx = 10000
		lowesty = 10000
		cords = [-1,-1,-1]
		for x in range(len(results)):
			for y in range(len(results[x])):
				for z in range(len(results[x][y]['location'][1])):
					if (results[x][y]['location'][1][z] < lowestx - tolerance):
						lowestx = results[x][y]['location'][1][z]
						lowesty = results[x][y]['location'][0][z]
						cords [0] = x
						cords [1] = y
						cords [2] = z
		for x in range(len(results)):
			for y in range(len(results[x])):
				for z in range(len(results[x][y]['location'][0])):
					if (results[x][y]['location'][0][z] < lowesty - tolerance and (results[x][y]['location'][1][z] - lowestx < tolerance and  results[x][y]['location'][1][z] - lowestx > tolerance * -1)):
						lowesty = results[x][y]['location'][0][z]
						cords [0] = x
						cords [1] = y
						cords [2] = z

		if (cords[0] == -1 or cords[1] == -1 or cords[2] == -1):
			break
		dictionary = {
			'direction': results[cords[0]][cords[1]]['direction'],
			'x': results[cords[0]][cords[1]]['location'][1][cords[2]],
			'y': results[cords[0]][cords[1]]['location'][0][cords[2]],
			'type': images[cords[0]]
		}

		results[cords[0]][cords[1]]['location'][0].pop(cords[2])
		results[cords[0]][cords[1]]['location'][1].pop(cords[2])
		massive_Array[index0][index1] = dictionary
		index0 += 1
		if(index0 >= board_height):
			index0 = 0
			index1 += 1
	return massive_Array


tolerance = 10
board_height = 2
board_width = 3
images = ['block.png', 'grom.png', 'off.png', 'spool.png', '3-tear.png','2-tear.png', '2-tear-r.png']
results = []
for item in images:
	results.append(imagesearch_count(item))
results = elimate_duplicates(results)
for index,item in enumerate(images):
	print(item, results[index])
results = find_hierarchy(results)

for item in results:
	print(item)

# for index,item in enumerate(images):
# 	print(item, results[index])





#pos = imagesearch_count("grom.png")
#print(pos)
# if pos[0] != -1:
#     print("position : ", pos[0], pos[1])
#     pyautogui.moveTo(pos[0], pos[1])
# else:
#     print("image not found")