#include <iostream>
#include <vector>

// Function to perform convolution operation
std::vector<std::vector<int>> convolution(const std::vector<std::vector<int>>& image, const std::vector<std::vector<int>>& kernel, int stride, int padding) {
    int image_height = image.size();
    int image_width = image[0].size();
    int kernel_height = kernel.size();
    int kernel_width = kernel[0].size();
    int output_height = (image_height + 2 * padding - kernel_height) / stride + 1;
    int output_width = (image_width + 2 * padding - kernel_width) / stride + 1;

    std::vector<std::vector<int>> output(output_height, std::vector<int>(output_width, 0));

    // Perform convolution
    for (int i = 0; i < output_height; ++i) {
        for (int j = 0; j < output_width; ++j) {
            for (int m = 0; m < kernel_height; ++m) {
                for (int n = 0; n < kernel_width; ++n) {
                    int row = i * stride + m - padding;
                    int col = j * stride + n - padding;
                    if (row >= 0 && row < image_height && col >= 0 && col < image_width) {
                        output[i][j] += image[row][col] * kernel[m][n];
                    }
                }
            }
        }
    }

    return output;
}

int main() {
    // Define input image and kernel
    std::vector<std::vector<int>> image = {
        {1, 2, 3, 4, 5},
        {6, 7, 8, 9, 10},
        {11, 12, 13, 14, 15},
        {16, 17, 18, 19, 20},
        {21, 22, 23, 24, 25}
    };

    std::vector<std::vector<int>> kernel = {
        {1, 0, -1},
        {1, 0, -1},
        {1, 0, -1}
    };

    // Stride and padding
    int stride = 1;
    int padding = 1;

    // Perform convolution
    std::vector<std::vector<int>> output = convolution(image, kernel, stride, padding);

    // Output the result
    std::cout << "Output matrix:" << std::endl;
    for (const auto& row : output) {
        for (int val : row) {
            std::cout << val << "\t";
        }
        std::cout << std::endl;
    }

    return 0;
}
