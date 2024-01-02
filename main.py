import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread


def change_contrast(image_array, factor):
    # Ensure the factor is greater than 0
    if factor <= 0:
        raise ValueError("Contrast factor should be greater than 0.")

    # Calculate the midpoint and adjust the pixel values
    midpoint = 127.5  # Assuming 8-bit image (0-255 range)
    adjusted_image = (image_array - midpoint) * factor + midpoint

    # Clip the values to the valid range [0, 255]
    adjusted_image = np.clip(adjusted_image, 0, 255).astype(np.uint8)

    return adjusted_image


def change_brightness(image_array, factor):
    # Adjust the pixel values by adding a constant delta
    adjusted_image = image_array * factor

    # Clip the values to the valid range [0, 255]
    adjusted_image = np.clip(adjusted_image, 0, 255).astype(np.uint8)

    return adjusted_image


# Example usage:
image_array = imread("./01.jpg")

# Display the original image
plt.imshow(image_array)
plt.title("Original Image")
plt.show()

# Change the contrast by a factor of 1.5
contrast_adjusted_image = change_contrast(image_array, factor=1.5)
plt.imshow(contrast_adjusted_image)
plt.title("Contrast Adjusted Image")
plt.show()

# Change the brightness by a factor of 1.5
brightness_adjusted_image = change_brightness(image_array, factor=1.5)
plt.imshow(brightness_adjusted_image)
plt.title("Brightness Adjusted Image")
plt.show()
