#include<stdio.h> 

int main() {
    int n=6778;

    if(n<10){ // checking the condition 
        printf("one digit");
    } 
    else if(n>=10 && n<100) {
        printf("two digit");
    }
    else if(n>=100 && n<1000)
    {
    	printf("Three digit");
	}
    else{
        printf("an integer");
    }
    return 0;
}
