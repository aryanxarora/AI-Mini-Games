// -------------------------------------------------------
// Assignment 2
// Written by: Aryan Arora - 2219549
// For “Programming Concepts I” Section 87411 and 01211 – Fall 2022 
// -------------------------------------------------------- 

import java.util.Scanner;
import java.io.IOException;

public class assignment2
{

  static void clear (Scanner sc)
  {
    System.out.println ("\n\nPress \"ENTER\" to continue...");
    try
    {
      int read = System.in.read (new byte[2]);
    } catch (IOException e)
    {
      e.printStackTrace ();
    }
    System.out.print ("\033[H\033[2J");
    System.out.flush ();
  }

  public static void main (String[]args)
  {
    Scanner sc = new Scanner (System.in);
    System.out.println ("Enter name: ");
    String user_name = sc.next ();
    System.out.
      printf
      ("\nHello %s!\nWelcome to Assignment 2 for Programming Concepts 1\n",
       user_name);
    clear (sc);

    System.out.println ("Problem 1\n");
    double pi = 0;
    int i;
    for (i = 10000; i > 0; i --){
        pi += Math.pow(-1, i + 1) / (2 * i - 1);
        if (i == 1){
            pi = pi * 4;
        }
    }
    System.out.println("PI: " + pi);
    clear(sc);

    System.out.println ("Problem 2\n");
    int rows = 5, j;
    for (i = 1; i <= rows; i++){
        for (j = 1; j <= rows - i; j++){
            System.out.print(" ");
        }

        for (j = 1; j <= i * 2 - 1; j++){
            System.out.print("*");
        }

        System.out.println();
    }
    for (i = rows - 1; i > 0; i--){
        for (j = 1; j <= rows - i; j++){
            System.out.print(" ");
        }
        for (j = 1; j <= i * 2 - 1; j++){
            System.out.print("*");
        }
        System.out.println();
    }
    clear(sc);

    rows = 7;
    int k;
    System.out.println ("Problem 3\n");
    for (i = 1; i < rows; i++){
        for (j = 1; j<= rows - i; j++){
            System.out.print(" ");
        }
        for (k = 0; k < i * 2 -1; k++){
            if (k == 0 || k == i * 2 - 2){
                System.out.print("*");
            }
            else if (k != 0 || k != i * 2 - 2){
                System.out.print(" ");
            }
        }
        System.out.println();
    }
    for (i = 0; i < rows; i++){
        System.out.print("* ");
    }
    clear(sc);

    System.out.print("Prolem 4\n\n");
    rows = 5;
    k = 0;
    int ctr1 = 0, ctr2 = 0;
    for (i = 1; i <= rows; i++){
        for (j = 1; j <= rows - i; j++){
            System.out.print("  ");
            ctr1++;
        }

        while (k != 2 * i - 1){
            if (ctr1 <= rows - 1){
                System.out.print((i + k) + " ");
                ctr1++;
            }
            else {
                ctr2++;
                System.out.print((i + k - 2 * ctr2) + " ");
            }

            k++;
        }

        ctr2 = ctr1 = k = 0;
        System.out.println();
    }

    System.out.println ("\nThank you! Exiting Program...");
  }
}
