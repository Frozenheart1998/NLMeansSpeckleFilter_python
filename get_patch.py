def get_patch(img, i, j, patch_size):
    size = (patch_size - 1) // 2
    patch1 = img[i - 2 * size:i + 1, j - 2 * size: j + 1]
    patch2 = img[i:i + 2 * size + 1, j: j + 2 * size + 1]
    patch3 = img[i - 2 * size:i + 1, j: j + 2 * size + 1]
    patch4 = img[i:i + 2 * size + 1, j - 2 * size: j + 1]
    return patch1, patch2, patch3, patch4
