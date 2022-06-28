def get_patch_single(img, i, j, patch_size):
    size = patch_size // 2  # int16((patch_size - 1) / 2) in matlab
    patch = img[(i - 1) - size: (i - 1) + size + 1, (j - 1) - size: (j - 1) + size + 1]
    return patch
