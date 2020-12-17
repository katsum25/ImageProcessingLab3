import numpy as np


def distance_map(image):

    height = image.shape[0]
    width = image.shape[1]

    offset_height = 1
    offset_width = 1

    distance_map = np.zeros((height + 2, width + 2), dtype=np.uint8)
    distance_map_f = np.zeros((height, width), dtype=np.uint8)

    distance_map[0, :] = 254
    distance_map[:, 0] = 254
    distance_map[height + offset_height, :] = 254
    distance_map[:, width + offset_width] = 254

    for i in range(height):
        for j in range(width):
            if (image[i, j] != 0):
                new_j = j + offset_width
                new_i = i + offset_height
                
                v = min(distance_map[i, new_j], distance_map[new_i, j]) + 1
                if (v > 255):
                    v = 255
                distance_map[new_i, new_j] = v

    for i in range(height - 1, -1, -1):
        for j in range(width - 1, -1, -1):
            if (image[i, j] != 0):
                new_j = j + offset_width
                new_i = i + offset_height
                
                v = min(distance_map[new_i + 1, new_j], distance_map[new_i, new_j + 1]) + 1
                v = min(v, distance_map[new_i, new_j])
                if (v > 255):
                    v = 255
                distance_map[new_i, new_j] = v
                distance_map_f[i, j] = v

    return distance_map_f