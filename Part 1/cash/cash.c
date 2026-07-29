#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int change; // prompt user for change and declared it
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 0); // limit the amount

    int coins = 0; // count number of coins

    // declare coin values
    int quarters = 25;
    int dimes = 10;
    int nickles = 5;
    int pennies = 1;

    coins += change / quarters; // Count how many quarters fit
    change %= quarters;         // Get raiming cents

    coins += change / dimes; // += add and assign | change ÷ dime(10) = ammount we can use
    change %= dimes;         //  %= Modulo and assign | change % dime(10) = change left

    coins += change / nickles;
    change %= nickles;

    coins += change / pennies;
    change %= pennies;

    // print total
    printf("%i\n", coins);
}
