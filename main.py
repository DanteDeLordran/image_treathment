import cv2
import numpy as np
import csv


def write_rgb_csv(_image, filename):
    with open(filename, mode="w") as csv_file:
        _csv = csv.writer(csv_file)
        _csv.writerows(_image)
    cv2.imshow("RGB", _image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def write_gray_csv(_height, _width, _image, filename):
    gray_img = np.zeros((_height, _width))
    for i in range(0, _height):
        for j in range(0, _width):
            gray_img[i][j] = (_image[i][j][0] * 0.33 + _image[i][j][1] * 0.33 + _image[i][j][2] * 0.33) / 255

    with open(filename, mode="w") as csv_file:
        _csv = csv.writer(csv_file)
        _csv.writerows(gray_img)
    cv2.imshow("GRAY", gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def write_intensity_csv():
    intensity = int(input('Intensity : '))


def write_clear_csv():
    return


def write_copy_csv():
    return


def main(file_name):
    print('1 - RGB matrix of image')
    print('2 - Gray matrix of image')
    print('3 - Change intensity of a pixel')
    print('4 - Copy of image')
    print('5 - Negative of an image')
    print('6 - Increment/decrement of brightness')
    print('7 - Contrast elongation/reduction')
    print('8 - Shifting H/V/D')
    print('9 - Quit')
    choice = int(input('Select an option : '))

    if choice == 1:
        write_rgb_csv(image, f"{file_name}_RGB.csv")
        main(file_name)
    elif choice == 2:
        write_gray_csv(height, width, image, f"{file_name}_GRAY.csv")
        main(file_name)


if __name__ == '__main__':
    image = cv2.imread('./images/testimage2.png')
    height, width, channels = image.shape

    print(f'Height {height} , Width {width}')
    image_name = str(input('Save matrix with name : '))
    main(image_name)
