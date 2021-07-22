import math
import matplotlib.pyplot as plt


def find_plot_dims(stack_length):

    mults = {4: (2, 2),
             6: (2, 3),
             9: (3, 3),
             12: (4, 3)}

    solution = min([i for i in mults.keys() if (i >= stack_length)])

    return mults[solution]


def plot_multiple_images(image_list):

    plt.figure('Multiple Images Plot')

    x_num, y_num = find_plot_dims(len(image_list))

    for img_num in range(1, len(image_list) + 1):
        plt.subplot(x_num, y_num, img_num)
        plt.imshow(image_list[img_num])
        plt.title(str(img_num), fontsize=8)
        plt.xticks([])
        plt.yticks([])

    plt.show()


