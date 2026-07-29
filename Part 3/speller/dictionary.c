// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 65536;

// Hash table
node *table[N];

unsigned int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    unsigned int index = hash(word);

    node *cursor = table[index];

    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }

        cursor = cursor->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long hash_value = 0;

    for (int i = 0; word[i] != '\0'; i++)
    {
        char c = tolower(word[i]);

        hash_value = hash_value * 31 + c;
    }

    return hash_value % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    for (int i =0; i < N; i++)
    {
        table[i] = NULL;
    }

    FILE *file = fopen(dictionary, "r");

    if (file == NULL)
    {
        fprintf(stderr, "could not open dicttionary file: %s\n", dictionary);
        return false;
    }

    char word_buffer[LENGTH + 1];

    while (fscanf(file, "%s", word_buffer) != EOF)
    {
        node *new_node = (node *)malloc(sizeof(node));

        if (new_node == NULL)
        {
            fclose(file);
            unload();
            return false;
        }

        strcpy(new_node->word, word_buffer);

        unsigned int index = hash(new_node->word);

        new_node->next = table[index];

        table[index] = new_node;

        word_count++;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        while (cursor != NULL)
        {
            node *tmp = cursor->next;

            free(cursor);

            cursor = tmp;
        }
    }
    // TODO
    return true;
}
