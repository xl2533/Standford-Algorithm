# -*- coding: utf-8 -*-
"""
Standford Algorithm - Lesson1 

Recurisive Interger Multiplication 

"""

input1 = 3141592653589793238462643383279502884197169399375105820974944592
input2 = 2718281828459045235360287471352662497757247093699959574966967627

Test_input1 = 1234
Test_input2 = 1234

Test_result = Test_input1 * Test_input2
def R_Multiply(input1,input2):
    if(input1 < 10 & input2 <10):
        return(input1 * input2);
    
    input1_str = str(input1);
    input2_str = str(input2);
    
    length = max(len(input1_str),len(input2_str));
    multiplier = int(length/2);
    
    input1_left = int(input1_str[ : multiplier]);
    input1_right = int(input1_str[multiplier :]);

    input2_left = int(input2_str[ :multiplier]);
    input2_right = int(input2_str[multiplier:]);
    
    a = input1_left * input2_left;
    b = input1_right *  input2_right;
    c = (input1_left + input1_right) * (input2_left + input2_right);
    output = 10**multiplier**2 * a + b + (c-a-b ) * 10 ** multiplier ;
 
    return output;

Test_result == R_Multiply(Test_input1,Test_input2)
