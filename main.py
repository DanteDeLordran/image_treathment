import cv2
import numpy as np
import csv


def write_rgb_csv(_image, filename):
    with open(filename, mode="w") as csv_file:
        _csv = csv.writer(csv_file)
        _csv.writerows(_image)


def write_gray_csv(_height, _width, _image, _gray_image, filename):
    for i in range(0, _height):
        for j in range(0, _width):
            _gray_image[i][j] = (_image[i][j][0] * 0.33 + _image[i][j][1] * 0.33 + _image[i][j][2] * 0.33) / 255

    with open(filename, mode="w") as csv_file:
        _csv = csv.writer(csv_file)
        _csv.writerows(_gray_image)


def write_clear_csv():
    return


if __name__ == '__main__':
    image = cv2.imread('./images/testimage2.png')
    height, width, channels = image.shape
    gray_img = np.zeros((height, width))

    print(f'Height {height} , Width {width}')
    print('Change intensity of a pixel')
    intensity = int(input('Intensity : '))
    image_name = str(input('Image name : '))

    write_rgb_csv(image, f"{image_name}_RGB.csv")
    write_gray_csv(height, width, image, gray_img, f"{image_name}_GRAY.csv")

    cv2.imshow("RGB", image)
    cv2.imshow("GRAY", gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
