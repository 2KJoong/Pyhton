import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # 또는 'Qt5Agg'를 사용

def apply_blur(image, kernel_size=(5, 5)):
    # Create a normalized kernel
    kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])

    # Get image dimensions
    height, width = image.shape[:2]

    # Padding size
    pad_h = kernel_size[0] // 2
    pad_w = kernel_size[1] // 2

    # Pad the image to handle border effects
    padded_image = cv2.copyMakeBorder(image, pad_h, pad_h, pad_w, pad_w, cv2.BORDER_REFLECT)

    # Prepare an empty output image
    blurry_image = np.zeros_like(image, dtype=np.uint8)

    # Perform convolution
    for i in range(height):
        for j in range(width):
            for c in range(image.shape[2]):  # Handle color channels (e.g., BGR)
                blurry_image[i, j, c] = np.sum(
                    kernel * padded_image[i:i + kernel_size[0], j:j + kernel_size[1], c]
                )

    return blurry_image


# Load the input image
image = cv2.imread('images/plane.jpg')

# Apply custom blur
image_blurry = apply_blur(image, kernel_size=(5, 5))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(image_blurry, cv2.COLOR_BGR2RGB))
plt.title('Manually Blurred Image')
plt.axis('off')

plt.show()  # 반드시 호출