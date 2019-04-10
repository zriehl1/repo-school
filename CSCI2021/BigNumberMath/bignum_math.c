// Zachary Riehl riehl046 5387064


/* -----------
 * bignum_math.c
 * Project for CSCI 2021, Fall 2018, Professor Chris Dovolis
 * orginially written by Andy Exley
 * modified by Ry Wiese, Min Choi, Aaron Councilman
 * ---------- */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define false 0;
#define true 1;

typedef int bool;
/*
 * Returns true if the given char is a digit from 0 to 9
 */
bool is_digit(char c) {
	return c >= '0' && c <= '9';
}

/*
 * Returns true if lower alphabetic character
 */
bool is_lower_alphabetic(char c) {
	return c >= 'a' && c <= 'z';
}

/*
 * Returns true if upper alphabetic character
 */
bool is_upper_alphabetic(char c) {
	return c >= 'A' && c <= 'Z';
}

/*
 * Convert a string to an integer
 * returns 0 if it cannot be converted.
 */
int string_to_integer(char* input) {
	int result = 0;
	int length = strlen(input);
	int num_digits = length;
	int sign = 1;

	int i = 0;
	int factor = 1;

	if (input[0] == '-') {
		num_digits--;
		sign = -1;
	}

	for (i = 0; i < num_digits; i++, length--) {
		if (!is_digit(input[length-1])) {
			return 0;
		}
		if (i > 0) factor*=10;
		result += (input[length-1] - '0') * factor;
	}

	return sign * result;
}

/*
 * Returns true if the given base is valid.
 * that is: integers between 2 and 36
 */
bool valid_base(int base) {
	if(!(base >= 2 && base <= 36)) {
		return false;
	}
	return true;
}

/*
 * TODO
 * Returns true if the given string (char array) is a valid input,
 * that is: digits 0-9, letters A-Z, a-z
 * and it should not violate the given base and should not handle negative numbers
 */
 bool char_within(char c, int base,char *arr, int count){ // this would be the second for loop, but done recursively. please don't kill my grade
   //printf("%i\n", count);
   if(c == *arr && count < base) return true;
   if(count >= base){
     return false;
   }
   else{
     return char_within(c,base,arr+1,count+1);
   }
 }
/* I want to outright say that this is not a good solution to this problem, and were I to redo this
 * section I would use nested for loops. When I wrote this I didnt know you could use int* inputs
 * in a similar fashion to arrays. So I walked down pointers. */

 bool valid_input(char *input, int base) { //basically done through double recursion instead of iteration, this would be the first for loop
 	char *lower_alphabetic = "0123456789abcdefghijklmnopqrstuvwxyz";
 	char *upper_alphabetic = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
 	//if(!valid_base(base)) return false;
 	if(*input == '\0'){
     return true;
   }
 	else{
 		if(char_within(*input,base,lower_alphabetic,0) || char_within(*input,base,upper_alphabetic,0)) return valid_input(input+1,base);
 		return false;
 	}
 	return true;
 }
/*
 * converts from an array of characters (string) to an array of integers
 */
int* string_to_integer_array(char* str) {
	int* result;
	int i, str_offset = 0;
		result = malloc((strlen(str) + 1) * sizeof(int));
		result[strlen(str)] = -1;
	for(i = str_offset; str[i] != '\0'; i++) {
		if(is_digit(str[i])) {
			result[i - str_offset] = str[i] - '0';
		} else if (is_lower_alphabetic(str[i])) {
			result[i - str_offset] = str[i] - 'a' + 10;
		} else if (is_upper_alphabetic(str[i])) {
			result[i - str_offset] = str[i] - 'A' + 10;
		} else {
			printf("I don't know how got to this point!\n");
		}
	}
	return result;
}

/*
 * finds the length of a bignum...
 * simply traverses the bignum until a negative number is found.
 */
int bignum_length(int* num) {
	int len = 0;
	while(num[len] >= 0){
		len++;
	}
	return len;
}

/*
 * TODO
 * Prints out a bignum using digits and lower-case characters
 * Current behavior: prints integers
 * Expected behavior: prints characters
 */
 void bignum_print(int* num) {
   char base_characters[36] = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j',
 					'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
 	int i;
 	if(num == NULL) { return; }

 	i = bignum_length(num);

 	/* Then, print each digit */
 	for(i = 0; num[i] >= 0; i++) {
 		printf("%c", base_characters[num[i]]);
 	}
 	printf("\n");
 }

/*
 *	Helper for reversing the result that we built backward.
 *  see add(...) below
 */
void reverse(int* num) {
	int i, len = bignum_length(num);
	for(i = 0; i < len/2; i++) {
		int temp = num[i];
		num[i] = num[len-i-1];
		num[len-i-1] = temp;
	}
}

/*
 * addition of input1 and input2
 * PROVIDED FOR GUIDANCE
 */
int* add(int* input1, int* input2, int base) {
	int len1 = bignum_length(input1);
	int len2 = bignum_length(input2);
	int resultlength = ((len1 > len2)? len1 : len2) + 2;
	int* result = (int*) malloc (sizeof(int) * resultlength);
	int r = 0;
	int carry = 0;
	int sign = input1[len1];
	int num1, num2;

	len1--;
	len2--;

	while (len1 >= 0 || len2 >= 0) {
	        if (len1 >= 0) {
        	    num1 = input1[len1];
	        } else {
        	    num1 = 0;
        	}

		if (len2 >= 0) {
		    num2 = input2[len2];
		} else {
		    num2 = 0;
		}

		result[r] = (num1 + num2 + carry) % base;
		carry = (num1 + num2 + carry) / base;

		len1--;
		len2--;
		r++;
	}
	if (carry > 0) {
		result[r] = carry;
		r++;
    	}
	result[r] = sign;
	reverse(result);
	return result;
}


/*
 * TODO
 * return true if input1 < input2, and false otherwise
 */
bool less_than(int* input1, int* input2) {
	int count = 0;
	if(bignum_length(input1) < bignum_length(input2)){ //if input2 is longer than input1 it is larger by default
		return true;
	}
	else if(bignum_length(input1) == bignum_length(input2)){ //if they are of equal size, check elements. Whichever hits a lower value first is the lower
		while(input1[count] == input2[count] && input1[count] >= 0){// walk through until corresponding elements aren't equal
			count++;
		}
		if(input1[count] < input2[count]) return true;
		return false;
	}


	return false; //if the first isn't shorter and isn't the same length, then it must be bigger
}


/*
 * TODO
 * return true if input1 > input2, and false otherwise
 */
bool greater_than(int* input1, int* input2) { //the same as less_than, but with the signs flipped.
	int count = 0;
	if(bignum_length(input1) > bignum_length(input2)){
		return true;
	}
	else if(bignum_length(input1) == bignum_length(input2)){
		while(input1[count] == input2[count] && input1[count] >= 0){
			count++;
		}
		if(input1[count] > input2[count]) return true;
		return false;
	}

	return false;
}

/*
 * TODO
 * return true if input1 == input2, and false otherwise
 */
bool equal_to(int* input1, int* input2) {
	if(!(bignum_length(input1) == bignum_length(input2))) return false; //this is probably the most common case so I put in a catch for it
	if(!(greater_than(input1,input2) || less_than(input1,input2))) return true; //if the numbers aren't greater or less than eachother, they must be equal
	//please don't kill my grade for this definition
	return false;
}
/*
 * TODO
 * multiply input1 * input2
 */
 void bignum_zero(int *arr, int len){ //creates a bignum of size len-1 important numbers, filled with 0s
   for(int i = 0; i < len; i++){
     arr[i] = 0;
   }
   arr[len-1] = -1;
 }

 int power(int base, int expo){ //returns base^expo
 	int val = 1;
 	for(int i = 0; i < expo; i++){
 		val = val * base;
 	}
 	return val;
 }

 int* multiply(int *input1, int *input2,int base){ //defined as adding input1 to itself input2 times.
   int len = bignum_length(input1) + 1;
   reverse(input2); //flip input2 so the low-order numbers come first
   int *ret = (int*) malloc(sizeof(int) * len);
   bignum_zero(ret,len); //create a bignum of all zeroes for adding
   for(int i = 0; input2[i] >= 0; i++){ //uses input2 to determine the number of times to add input1 to the return array
     int times = input2[i] * power(base,i);
     for(int j = 0; j < times; j++){ //does the addition the correct number of times
       ret = add(input1,ret,base);
     }
   }
   return ret;
 }

/*
 * TODO
 * This function is where you will write the code that performs the heavy lifting,
 * actually performing the calculations and comparisons on input1 and input2.
 * This function prints the result using printf. It does not return any value.
 * The text printed should always be of the form
 *    Result: ...
 * Where the ... is either a number of one of 'true' or 'false'.
 * See the project write-up for examples.
 * HINT: For better code structure, use helper functions.
 */
void perform_operation(int* input1, int* input2, char op, int base) {//used the exact same format given, so it shouldn't merit more explanation.

	if(op == '+') {
		int* result = add(input1, input2, base);
		printf("Result: ");
		bignum_print(result);
		printf("\n");
		free(result);
	}

	if(op == '*'){
		int *result = multiply(input1,input2,base);
		printf("Result: ");
		bignum_print(result);
		printf("\n");
		free(result); //free the malloc'ed memory to prevent memory leaks.
	}

	if(op == '<'){
		printf("Result: ");
		if(less_than(input1,input2)){
			printf("True");
		}
		else{
			printf("False");
		}
		printf("\n");

	}

	if(op == '>'){
		printf("Result: ");
		if(greater_than(input1,input2)){
			printf("True");
		}
		else{
			printf("False");
		}
		printf("\n");

	}

	if(op == '='){
		printf("Result: ");
		if(equal_to(input1,input2)){
			printf("True");
		}
		else{
			printf("False");
		}
		printf("\n");

	}
	/*
	 * TODO
	 * Handle multiplication, less than, greater than, and equal to
	 */
}

/*
 * Print to "stderr" and exit program
 */
void print_usage(char* name) {
	fprintf(stderr, "----------------------------------------------------\n");
	fprintf(stderr, "Usage: %s base input1 operation input2\n", name);
	fprintf(stderr, "base must be number between 2 and 36, inclusive\n");
	fprintf(stderr, "input1 and input2 are arbitrary-length integers\n");
	fprintf(stderr, "Permited operations are allowed '+', '*', '<', '>', and '='\n");
	fprintf(stderr, "----------------------------------------------------\n");
	exit(1);
}


/*
 * MAIN: Run the program and tests your functions.
 * sample command: ./bignum 4 12 + 13
 * Result: 31
 */
int main(int argc, char** argv) {

	int input_base;

	int* input1;
	int* input2;

	if(argc != 5) {
		print_usage(argv[0]);
	}

	input_base = string_to_integer(argv[1]);

	if(!valid_base(input_base)) {
		fprintf(stderr, "Invalid base: %s\n", argv[1]);
		print_usage(argv[0]);
	}


	if(!valid_input(argv[2], input_base)) {
		fprintf(stderr, "Invalid input1: %s\n", argv[2]);
		print_usage(argv[0]);
	}

	if(!valid_input(argv[4], input_base)) {
		fprintf(stderr, "Invalid input2: %s\n", argv[4]);
		print_usage(argv[0]);
	}

	char op = argv[3][0];
	if(op != '+' && op != '*' && op != '<' && op != '>' && op != '=') {
		fprintf(stderr, "Invalid operation: %s\n", argv[3]);
		print_usage(argv[0]);
	}

	input1 = string_to_integer_array(argv[2]);
	input2 = string_to_integer_array(argv[4]);

	perform_operation(input1, input2, op, input_base);

	free(input1);
	free(input2);

	exit(0);
}
