/* -----------
 * project2.c
 * Project for CSCI 2021, Fall 2018, Professor Chris Dovolis
 * Written by Ry Wiese
 * ---------- */

#include <stdio.h>
#include <stdlib.h>


//create global variable LEN with value 16
//length of reg arrays will be 16
//to represent 16 bit registers
#define LEN 16

//create a new type reg which is just a renaming of char*
typedef char* reg;

//these are the functions you will need to write
void add(reg reg1, reg reg2, reg result_reg);
void subtract(reg reg1, reg reg2, reg result_reg);
void and(reg reg1, reg reg2, reg result_reg);
void or(reg reg1, reg reg2, reg result_reg);
void not(reg reg1, reg result_reg);
void logical_left_shift(reg reg1, int n, reg result_reg);
void arithmetic_right_shift(reg reg1, int n, reg result_reg);

//you do not have to do anything with these functions
//although it may be helpful to understand them and
//their role in the program
//do not modify these functions as we need them to grade your project
//you are encouraged to add your own tests, but please do so in the main function
int str_len(char* s);
int power(int x, int n);
void itoreg(int a, reg r);
short int regtoi(reg r);
void print_status(reg rega, reg regb, reg regc, reg regd);
void run_tests(reg rega, reg regb, reg regc, reg regd);

int main(int argc, char** argv) {
    //check for correct number of command line arguments
    if(argc != 3) {
        printf("Please enter exactly 2 integers as command line arguments.\n");
        printf("You entered %d integers.\n", argc - 1);
        exit(0);
    }

    //assign command line arguments to short ints
    short int a = atoi(argv[1]);
    short int b = atoi(argv[2]);
    short int c = 0;
    short int d = 0;

    //create four 16 bit registers
    reg rega = malloc((LEN + 1) * sizeof(char));
    reg regb = malloc((LEN + 1) * sizeof(char));
    reg regc = malloc((LEN + 1) * sizeof(char));
    reg regd = malloc((LEN + 1) * sizeof(char));

    //initialze the registers with the ints provided by the command line args
    itoreg(a, rega);
    itoreg(b, regb);
    itoreg(c, regc);
    itoreg(d, regd);

    //TODO feel free to add your own tests here,
    //but please delete/comment out your tests before submitting

    //Test your functions
    //Feel free to comment out this part and use your own tests instead
    print_status(rega, regb, regc, regd);
    printf("\n");


    run_tests(rega, regb, regc, regd);

    //always free malloced memory
    free(rega);
    free(regb);
    free(regc);
    free(regd);

    return 0;
}
void flip(reg reg1){//flips the order of the bits, didn't get used ultimately.
  for(int i = 0; i < LEN/2; i++){
    char temp = reg1[i];
    reg1[i] = reg1[LEN-i-1];
    reg1[LEN-i-1] = temp;
  }
}

int char_to_int(char c){//returns a 1 if c is '1' and 0 if c is '0'
  return c - '0';
}

//TODO bitwise add reg1 and reg2, then store the result in result_reg
void add(reg reg1, reg reg2, reg result_reg) {
  int carry = 0;
  for(int i = LEN-1; i >= 0; i--){
    int temp = char_to_int(reg1[i]) + char_to_int(reg2[i]) + carry;
    switch (temp) {
      case 0: //both registers and the carry are zero
        result_reg[i] = '0';
        carry = 0;
        break;
      case 1://one register or the carry is one
        result_reg[i] = '1';
        carry = 0;
        break;
      case 2://two registers and/or the carry is one (pick 2)
        result_reg[i] = '0';
        carry = 1;
        break;
      case 3://both registers and the carry are 1
        result_reg[i] = '1';
        carry = 1;
        break;
      default:
        printf("%d DEFAULT\n",temp);
    }
  }
}

//TODO bitwise subtract reg1 and reg2, then store the result in result_reg
//hint: it may be helpful to use other functions you have created
void subtract(reg reg1, reg reg2, reg result_reg) {
  reg not_reg2 = malloc((LEN + 1) * sizeof(char));
  reg one = malloc((LEN + 1) * sizeof(char));
  reg temp = malloc((LEN + 1) * sizeof(char));
  itoreg(1,one);
  itoreg(0,temp);
  itoreg(0,not_reg2);
  not(reg2, not_reg2);
  add(not_reg2,one,temp); //this and previous line two's compliment the subtractor
  add(reg1,temp,result_reg); //add the subtractee to the subtractor a + (-b)
  free(not_reg2);
  free(one);
  free(temp);

}

//TODO bitwise and reg1 and reg2, then store the result in result_reg
void and(reg reg1, reg reg2, reg result_reg) {
  for(int i = 0; i<LEN; i++){
    if(reg1[i] == reg2[i]){
      result_reg[i] = reg1[i];
    }
    else{
      result_reg[i] = '0';
    }
  }


}

//TODO bitwise or reg1 and reg2, then store the result in result_reg
void or(reg reg1, reg reg2, reg result_reg) {
  for(int i = 0; i<LEN; i++){
    if(reg1[i] == '1' || reg2[i] == '1'){
      result_reg[i] = '1';
    }
    else{
      result_reg[i] = '0';
    }
  }

}

//TODO bitwise not reg1, then store the result in result_reg
void not(reg reg1, reg result_reg) {
  for(int i = 0; i < LEN; i++){
    if(reg1[i] == '0'){
      result_reg[i] = '1';
    }
    else{
      result_reg[i] = '0';
    }
  }
}

//TODO logical left shift reg1 by n, then store the result in result_reg
void logical_left_shift(reg reg1, int n, reg result_reg) {
  for(int i = 0; i < LEN; i++){ //iterate through the shiftable digits (the ones farther to the left)
    if(i < n){
      result_reg[i] = '0';
    }
    else{
      char temp = reg1[i];
      result_reg[i-n] = temp;
    }
  }
  for(int j = LEN-n; j < LEN; j++){//put in zeroes for the digits that don't have a value shifted onto them.
    result_reg[j] = '0';
  }
}

//TODO arithmetic right shift reg1 by n, then store the result in result_reg
void arithmetic_right_shift(reg reg1, int n, reg result_reg) {
  char fill;
  for(int i = LEN-1; i >= 0; i--){//iterate and edit the digits that have a value shifted onto them, and determine the filler digit
    if(i >= LEN-n){
      result_reg[i] = '0';
    }
    else{
      char temp = reg1[i];
      fill = temp;
      result_reg[i+n] = temp;

    }
  }
  for(int j = 0; j < n; j++){//place the filler digit in all places that don't have a value shifted onto them
    result_reg[j] = fill;
  }

}

//you do not have to worry about writing the following functions

//finds the length of s
int str_len(char* s) {
    int l = 0;
    while(s[l] != '\0')
        l++;
    return l-1;
}

//returns x^n
int power(int x, int n) {
    if(n <= 0)
        return 1;
    else
        return x * power(x, n-1);
}

//short for integer to register
//stores the 2s complement version of a in r
void itoreg(int a, reg r) {
    int i = 0;
    int p = LEN - 1;

    //handle whether a is positive or negative
    if(a >= 0) {
        r[i] = '0';
    }
    else {
        r[i] = '1';
        a += power(2, p);
    }
    i++;
    p--;

    //fill in the rest of the register
    while(i < LEN) {
        if(a/power(2, p)) {
            r[i] = '1';
            a -= power(2, p);
        }
        else {
            r[i] = '0';
        }
        i++;
        p--;
    }
    r[LEN] = '\0';
}

//short for register to integer
//returns the integer version of r
short int regtoi(reg r) {
    int p = LEN - 1;
    int i = 0;
    int a = -1 * (r[i] - 48) * power(2, p);
    i++;
    p--;
    while(i < LEN) {
        a += (r[i] - 48) * power(2, p);
        i++;
        p--;
    }
    return a;
}

//prints the values in the registers
void print_status(reg rega, reg regb, reg regc, reg regd) {
    printf("Register status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", regtoi(rega), regtoi(regb), regtoi(regc), regtoi(regd));
    printf("rega: %s\nregb: %s\nregc: %s\nregd: %s\n", rega, regb, regc, regd);
}

//run a series of tests to see if your functions work properly
void run_tests(reg rega, reg regb, reg regc, reg regd) {
    signed short int a, b, c, d;

    //Test add(rega, regb, regc)
    printf("Adding rega to regb and storing the result in regc...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    add(rega, regb, regc);
    c = a + b;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test add(rega, regb, regb)
    printf("Adding rega to regb and storing the result in regb...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    add(rega, regb, regb);
    b = a + b;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test add(rega, regc, rega)
    printf("Adding rega to regc and storing the result in rega...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    add(rega, regc, rega);
    a = a + c;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test subtract(regb, rega, regd)
    printf("Subtracting rega from regb and storing the result in regd...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    subtract(regb, rega, regd);
    d = b - a;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test subtract(regd, regb, regb)
    printf("Subtracting regb from regd and storing the result in regb...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    subtract(regd, regb, regb);
    b = d - b;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test subtract(rega, regc, rega)
    printf("Subtracting regc from rega and storing the result in rega...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    subtract(rega, regc, rega);
    a = a - c;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test and(rega, regc, regd)
    printf("Bitwise and-ing rega and regc and storing the result in regd...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    and(rega, regc, regd);
    d = a & c;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test and(regc, regd, rega)
    printf("Bitwise and-ing regc and regd and storing the result in rega...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    and(regc, regd, rega);
    a = c & d;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test and(rega, regb, rega)
    printf("Bitwise and-ing rega and regb and storing the result in rega...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    and(rega, regb, rega);
    a = a & b;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test or(rega, regb, regd)
    printf("Bitwise or-ing rega and regb and storing the result in regd...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    or(rega, regb, regd);
    d = a | b;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test or(regc, rega, rega)
    printf("Bitwise or-ing regc and rega and storing the result in rega...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    or(regc, rega, rega);
    a = c | a;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test or(regb, regc, regb)
    printf("Bitwise or-ing regb and regc and storing the result in regb...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    or(regb, regc, regb);
    b = b | c;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test not(regb, rega)
    printf("Bitwise not-ing regb and storing the result in rega...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    not(regb, rega);
    a = ~b;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test not(regd, regd)
    printf("Bitwise not-ing regd and storing the result in regd...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    not(regd, regd);
    d = ~d;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test logical_left_shift(rega, 4, regc)
    printf("Logical left shifting rega by 4 and storing the result in regc...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    logical_left_shift(rega, 4, regc);
    c = a << 4;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test logical_left_shift(regb, 6, regb)
    printf("Logical left shifting regb by 6 and storing the result in regb...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    logical_left_shift(regb, 6, regb);
    b = b << 6;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test arithmetic_right_shift(regc, 2, regb)
    printf("Arithmetic right shifting regc by 2 and storing the result in regb...\n");
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    arithmetic_right_shift(regc, 2, regb);
    b = c >> 2;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");

    //Test arithmetic_right_shift(rega, 7, rega)
    printf("Arithmetic right shifting rega by 7 using a negative number and storing the result in rega...\n");
    itoreg(-3945, rega);
    a = regtoi(rega);
    b = regtoi(regb);
    c = regtoi(regc);
    d = regtoi(regd);
    arithmetic_right_shift(rega, 7, rega);
    a = a >> 7;
    printf("Expected status:\n");
    printf("rega: %d\nregb: %d\nregc: %d\nregd: %d\n", a, b, c, d);
    print_status(rega, regb, regc, regd);
    if(regtoi(rega)==a && regtoi(regb)==b && regtoi(regc)==c && regtoi(regd)==d)
        printf("Correct!\n\n");
    else printf("Wrong!\n\n");
}
