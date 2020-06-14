//Simple calculator program coded in java (Made: Jauaries).

import java.util.Scanner;
import java.lang.Math;

public class Calculator {
    public static void main(String[] args) {
        double num1, num2;

        Scanner scanner = new Scanner(System.in);


        //Defining the numbers (num1 & num2)
        System.out.print("Enter first number: ");
        num1 = scanner.nextDouble();
        System.out.print("Enter second number: ");
        num2 = scanner.nextDouble();


        //Operators
        System.out.print("Enter an operator (+, -, *, /, ^): ");
        char operator = scanner.next().charAt(0);

        scanner.close();
        double output;


        //Defining the operators used in the program
        switch(operator) {
            case '+':
                output = num1 + num2;
                break;

            case '-':
                output = num1 - num2;
                break;

            case '*':
                output = num1 * num2;
                break;

            case '/':
                output = num1 / num2;
                break;

            case '^':
                output = Math.pow(num1, num2);
                break;


            //Error message if the user selects different operator, that isn't in the list
            default:
                System.out.print("ERROR: You have entered wrong operator");
                return;
        }

        System.out.println(num1 + " " + operator + " " + num2 + " = " + output);
    }
}
