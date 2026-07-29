#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: "); // prompt user for text

    int letters = 0;
    int words = 1;
    int sentences = 0;

    for (int i = 0; i < strlen(text); i++) // count words and letters
    {
        if (isalpha(text[i]))
        {
            letters++;
        }

        else if (text[i] == ' ')
        {
            words++;
        }

        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }

    float L = (float) letters / words * 100; // calculate grade
    float S = (float) sentences / words * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1) // retrun grade
    {
        printf("Before Grade 1\n");
    }

    else if (index > 16)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %i\n", index);
    }
}
