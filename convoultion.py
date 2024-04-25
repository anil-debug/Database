import numpy as np

def convolution(image, kernel, stride, padding):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    output_height = (image_height + 2 * padding - kernel_height) // stride + 1
    output_width = (image_width + 2 * padding - kernel_width) // stride + 1
    print("the output height is", output_height)
    print("the output width is ", output_width)
    output = np.zeros((output_height, output_width))
    # Perform convolution
    for i in range(output_height):
        for j in range(output_width):
            for m in range(kernel_height):
                for n in range(kernel_width):
                    row = i * stride + m - padding
                    col = j * stride + n - padding
                    if row >= 0 and row < image_height and col >= 0 and col < image_width:
                        output[i, j] += image[row, col] * kernel[m, n]

    return output

##############################################################
######    with out stride but padding is there          ######
##############################################################
def convolution_wostride(image, kernel, padding):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    output_height = (image_height + 2 * padding - kernel_height) // stride + 1
    output_width = (image_width + 2 * padding - kernel_width) // stride + 1
    print("the output height is", output_height)
    print("the output width is ", output_width)
    output = np.zeros((output_height, output_width)) 
    for i in range(output_height):
        for j in range(output_width):
            for m in range(kernel_height):
                for n in range(kernel_width):
                    # Calculate input indices without stride and with padding
                    row = i + m - padding
                    col = j + n - padding
                    if row >= 0 and row < image_height and col >= 0 and col < image_width:
                        # Convolution operation
                        output[i, j] += image[row, col] * kernel[m, n]
    return output
##############################################################
######    with out padding but stride is there          ######
##############################################################
def convolution_wopadding(image, kernel, stride):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    output_height = (image_height + 2 * padding - kernel_height) // stride + 1
    output_width = (image_width + 2 * padding - kernel_width) // stride + 1
    print("the output height is", output_height)
    print("the output width is ", output_width)
    output = np.zeros((output_height, output_width)) 
    for j in range(output_width):
        for m in range(kernel_height):
            for n in range(kernel_width):
                # Calculate input indices with stride and without padding
                row = i * stride + m
                col = j * stride + n
                if row >= 0 and row < image_height and col >= 0 and col < image_width:
                    # Convolution operation
                    output[i, j] += image[row, col] * kernel[m, n]
    return output
##############################################################
######    with out padding and stride                   ######
##############################################################
def convolution_wopadding_stride(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    output_height = (image_height + 2 * padding - kernel_height) // stride + 1
    output_width = (image_width + 2 * padding - kernel_width) // stride + 1
    print("the output height is", output_height)
    print("the output width is ", output_width)
    output = np.zeros((output_height, output_width)) 
    for i in range(output_height):
        for j in range(output_width):
            for m in range(kernel_height):
                for n in range(kernel_width):
                    # Calculate input indices without stride and without padding
                    row = i + m
                    col = j + n
                    # Convolution operation
                    output[i, j] += image[row, col] * kernel[m, n]
    return output

# Define input image and kernel
image = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

kernel = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

# Stride and padding
stride = 1
padding = 2

# Perform convolution
output = convolution(image, kernel, stride, padding)

# Output the result
print("Output matrix:")
print(output)
