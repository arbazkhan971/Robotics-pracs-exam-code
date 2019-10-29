def get_seed_point(image):
    """
    given an image, return any point having 1.
    """
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == 1:
                return (i, j)

    
def get_chain_code(image, i, j, m, n, visited):
    """
        0
      6 x 2
        4
    """

    # condition which will check if the pixel (i, j) is 1 in the image and is not visited yet.
    one_and_visited = lambda i, j: (image[i][j] == 1) and (not visited[i][j])
    
    if (0 <= i < m) and (0 <= j < n) and (not visited[i][j]):
        visited[i][j] = True
        if one_and_visited(i, j+1):
            return "0" + get_chain_code(image, i, j + 1, m, n, visited)
        elif one_and_visited(i - 1, j):
            return "2" + get_chain_code(image, i - 1, j, m, n, visited)
        elif one_and_visited(i, j - 1):
            return "4" + get_chain_code(image, i, j - 1, m, n, visited)
        elif one_and_visited(i + 1, j):
            return "6" + get_chain_code(image, i + 1, j, m, n, visited)
        return ""
    else:
        return ""


if __name__ == '__main__':
    image = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    m, n = len(image), len(image[0])  # dimensions of the image.
    i, j = get_seed_point(image)      # any random point in the image having value 1
    visited = [[False for _ in range(n)] for _ in range(m)]
    print(visited)
    print(get_chain_code(image, i, j, m, n, visited))

