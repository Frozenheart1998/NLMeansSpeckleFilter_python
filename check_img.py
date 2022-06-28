def check_img(img, i, j, window_size, patch_size):
    check = 1
    size1 = (window_size - 1) / 2
    size2 = (patch_size - 1) / 2
    if i - (size1 + size2) < 0 or \
        j - (size1 + size2) < 0 or \
        i + (size1 + size2) > img.shape[0] or \
        j + (size1 + size2) > img.shape[1]:
        check = 0
    return check
