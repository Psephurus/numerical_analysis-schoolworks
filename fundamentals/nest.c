/**
 ******************************************************************************
 * @file    nest.c
 * @brief   秦九韶算法
 * @author  高迎新 2023200486 材料学院
 * @date    2024/05/07
 ******************************************************************************
 */

#include <stdio.h>

/**
 * @brief Evaluates polynomial using Horner's Method.
 * @param degree The degree of the polynomial.
 * @param coeff Array of d+1 coefficients where the first term is the constant.
 * @param x The x-coordinate at which to evaluate the polynomial.
 * @param basis Optional array of d base points; defaults to zero if not provided.
 * @return `double` The value of the polynomial at x.
 */
double nest(int degree, double coeff[], double x, double basis[]) {
    double y = coeff[degree];
    for (int i = degree - 1; i >= 0; i--) {
        y = y * (x - basis[i]) + coeff[i];
    }
    return y;
}

int main() {
    /* Example 1: Base points are 0 */
    int degree = 4;
    double coeff[] = {-1, 5, -3, 3, 2};  // Coefficients (constant term first)
    double x = 0.5;  // Point at which to evaluate the polynomial
    double basis[4] = {0, 0, 0, 0};  // All base points are 0 for simplicity
    
    /* Call the function and print result */
    double result = nest(degree, coeff, x, basis);
    printf("The value of the polynomial at x = %.2f is %.2f\n", x, result);
    
    /* Example 2: Evaluating an array of x */
    double x_2[] = {-2, -1, 0, 1, 2};
    double results_2[5];  // Array to store results
    printf("The value of the polynomial at array [");
    for (int i = 0; i < 5; i++) {
        results_2[i] = nest(degree, coeff, x_2[i], basis);
        printf("%d%s", (int)x_2[i], (i < 4) ? " " : "]");
    }
    printf(" is [");
    for (int i = 0; i < 5; i++) {
        printf("%.0f%s", results_2[i], (i < 4) ? " " : "]\n");
    }
    
    /* Example 3: Base points are not 0 */
    int degree_3 = 3;
    double coeff_3[] = {1, 0.5, 0.5, -0.5};  // Coefficients
    double x_3 = 1;  // Point at which to evaluate
    double basis_3[] = {0, 2, 3};  // Non-zero base points
    
    /* Call the function and print result */
    double result_3 = nest(degree_3, coeff_3, x_3, basis_3);
    printf("The value of the polynomial at x = %.2f is %.2f\n", x_3, result_3);

    return 0;
}
