
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0; argv[1][i] != '\0'; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(argv[1]) % 26;

    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];

        if (isalpha(c))
        {
            int pi;
            int ci;

            if (isupper(c))
            {
                pi = c - 'A';
                ci = (pi + key) % 26;
                printf("%c", ci + 'A');
            }
            else if (islower(c))
            {
                pi = c - 'a';
                ci = (pi + key) % 26;
                printf("%c", ci + 'a');
            }
        }
        else
        {
            printf("%c", c);
        }
    }
    printf("\n");
}
