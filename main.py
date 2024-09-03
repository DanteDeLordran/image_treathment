import csv
import cv2
import numpy as np
from colorama import Fore, Style


def write_rgb_csv(_image, filename):
    _height, _width, _ = _image.shape
    _channels = ['R', 'G', 'B']

    for i, channel in enumerate(_channels):
        channel_img = _image[:, :, i]

        with open(f"{channel}_{filename}", mode="w") as csv_file:
            _csv = csv.writer(csv_file)
            _csv.writerows(channel_img)

        cv2.imshow(f"{channel}", channel_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def write_gray_csv( _image, filename):
    with open(filename, mode="w") as csv_file:
        _csv = csv.writer(csv_file)
        _csv.writerows(_image)
    cv2.imshow("GRAY", _image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def write_intensity_csv(_image , filename):
    img_height, img_width = _image.shape
    intensity = int(input('Intensity : '))
    if not -1 < intensity < 256:
        write_intensity_csv(_image, filename)
    _height = int(input('Height :'))
    _width = int(input('Width :'))
    if not -1 < _height < img_height and -1 < _width < img_width:
        write_intensity_csv(_image, filename)
    copy_img = _image.copy()
    copy_img[_height][_width] = intensity/255
    with open(filename, mode="w") as csv_file:
        _csv = csv.writer(csv_file)
        _csv.writerows(copy_img)
    cv2.imshow("INTENSITY", copy_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def write_copy_csv(_image, filename):
    copy = _image.copy()
    with open(filename, mode="w") as csv_file:
        _csv = csv.writer(csv_file)
        _csv.writerows(copy)
    cv2.imshow("ORIGINAL", _image)
    cv2.imshow("COPY", copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def img_to_gray(_image ):
    _height, _width, _ = _image.shape
    gray_img = np.zeros((_height, _width))
    for i in range(0, _height):
        for j in range(0, _width):
            gray_img[i][j] = (_image[i][j][0] * 0.33 + _image[i][j][1] * 0.33 + _image[i][j][2] * 0.33) / 255
    return gray_img


def main(file_name):
    print(Fore.GREEN + '1 - RGB matrix of image')
    print('2 - Gray matrix of image')
    print('3 - Change intensity of a pixel')
    print('4 - Copy of image')
    print(Fore.RED + '5 - Negative of an image')
    print('6 - Increment/decrement of brightness')
    print('7 - Contrast elongation/reduction')
    print('8 - Shifting H/V/D')
    print(Fore.GREEN + '9 - Quit' + Style.RESET_ALL)
    choice = int(input('Select an option : '))

    if choice == 1:
        write_rgb_csv(image, f"{file_name}_RGB.csv")
        main(file_name)
    elif choice == 2:
        write_gray_csv(img_to_gray(image), f"{file_name}_GRAY.csv")
        main(file_name)
    elif choice == 3:
        write_intensity_csv(img_to_gray(image) ,f"{file_name}_INTENSITY.csv")
        main(file_name)
    elif choice == 4:
        write_copy_csv(img_to_gray(image), f"{file_name}_COPY.csv")
        main(file_name)

if __name__ == '__main__':
    image = cv2.imread('./images/testimage2.png')
    height, width, channels = image.shape

    print(f'Height {height} , Width {width}')
    image_name = str(input('Save matrix with name : '))
    main(image_name)
