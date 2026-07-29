#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            int average = round((red + green + blue) / 3.0);

            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            float sepiaRed_float = .393 * red + .769 * green + .189 * blue;
            float sepiaGreen_float = .349 * red + .686 * green + .168 * blue;
            float sepiaBlue_float = .272 * red + .534 * green + .131 * blue;

            image[i][j].rgbtRed = fmin(255, fmax(0, round(sepiaRed_float)));
            image[i][j].rgbtGreen = fmin(255, fmax(0, round(sepiaGreen_float)));
            image[i][j].rgbtBlue = fmin(255, fmax(0, round(sepiaBlue_float)));
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE left_pixel = image[i][j];
            RGBTRIPLE right_pixel = image[i][width - 1 - j];

            RGBTRIPLE temp = left_pixel;
            image[i][j] = right_pixel;
            image[i][width - 1 - j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp_image[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red_sum = 0;
            int green_sum = 0;
            int blue_sum = 0;
            int neighbor_count = 0;

            for (int row_offset = -1; row_offset <= 1; row_offset++)
            {
                for (int col_offset = -1; col_offset <= 1; col_offset++)
                {
                    int neighbor_row = i + row_offset;
                    int neighbor_col = j + col_offset;

                    if (neighbor_row >= 0 && neighbor_row < height && neighbor_col >= 0 &&
                        neighbor_col < width)
                    {
                        red_sum += image[neighbor_row][neighbor_col].rgbtRed;
                        green_sum += image[neighbor_row][neighbor_col].rgbtGreen;
                        blue_sum += image[neighbor_row][neighbor_col].rgbtBlue;
                        neighbor_count++;
                    }
                }
            }

            temp_image[i][j].rgbtRed = round((float) red_sum / neighbor_count);
            temp_image[i][j].rgbtGreen = round((float) green_sum / neighbor_count);
            temp_image[i][j].rgbtBlue = round((float) blue_sum / neighbor_count);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp_image[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp_image[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp_image[i][j].rgbtBlue;
        }
    }
    return;
}
