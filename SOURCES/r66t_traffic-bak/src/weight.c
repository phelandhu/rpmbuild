/* This program reads a weight in  pounds from the key board representing it as an integer.
 * It converts the weight to ounce, and prints it. Program from "Applications Programming in ANSI C" 
 * by Hohnsonbaugh & Kalin
 * */

#include<stdio.h>

main( )
{
   int pounds;

   /* Read first weight in pounds  */

   printf("\n\n\tWeight in pounds?");
   scant("%d",&pounds);

   /* Loop until user signals halt with negatie integer.  */

   while(pounds>=0)
   {
   printf("\n\n\tEquivalent weight in ounces: %d", pounds * 16);
   printf("\n\n\tWeight in pounds?");
   printf("\n\n\tEnter a negative integer to quit.");
   scanf("%d",&pounds);
   }
}
