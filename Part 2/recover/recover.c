#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// define the block size for reading
#define BLOCK_SIZE 512
// define the size of the header that we look for
#define JPEG_HEADER_SIZE 4
// define the JPEG header pattern with bytes
unsigned char JPEG_HEADER[JPEG_HEADER_SIZE] = {0xff, 0xd8, 0xff, 0xe0};

int main(int argc, char *argv[])
{
    // check if the correct number of arguments are provided
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1; // show error
    }

    // store the name of the input file from the argument
    char *infile = argv[1];

    // open the input file in read binary
    FILE *inptr = fopen(infile, "rb");

    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s\n", infile);
        return 1;
    }

    // declare a buffer to store each block of read data from input
    unsigned char buffer[BLOCK_SIZE];

    // initialize a counter for the number of jpeg files found
    int file_count = 0;

    // initialize a pointer to the current open output file
    FILE *outfile = NULL;

    // declare a filename buffer to store the name of the output file
    char filename[8];

    // loop through the input file, reading one block at a time
    while (fread(buffer, 1, BLOCK_SIZE, inptr) == BLOCK_SIZE)
    {
        // check if the block has the start of JPEG file
        if (buffer[0] == JPEG_HEADER[0] && buffer[1] == JPEG_HEADER[1] &&
            buffer[2] == JPEG_HEADER[2] && (buffer[3] & 0xf0) == (JPEG_HEADER[3] & 0xf0))
        {
            // if found jpeg and opened file, close
            if (outfile != NULL)
            {
                fclose(outfile);
            }

            // create a new filename for jpeg
            sprintf(filename, "%03i.jpg", file_count);

            // open new filename in binary
            outfile = fopen(filename, "wb");

            // Check if file was opened
            if (outfile == NULL)
            {
                fclose(inptr);
                fprintf(stderr, "could not create %s\n", filename);
                return 1;
            }

            // increment the file counter
            file_count++;

            // write current block to outfile
            fwrite(buffer, 1, BLOCK_SIZE, outfile);
        }

        else if (outfile != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, outfile);
        }
    }

    if (outfile != NULL)
    {
        fclose(outfile);
    }

    fclose(inptr);

    return 0;
}
