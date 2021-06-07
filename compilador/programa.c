#include<stdio.h>

typedef char literal[256];

int main(void){

	int T0;
		int T1;
	int T2;
	int T3;
	int T4;
	literal Y; 
	int B; 
	double A; 
	double C; 
	int D; 
	
	
	
	printf("%s", "ola"); 
	scanf("%lf", &A); 
	scanf("%d", &B); 
	T0 = B > 2; 
	if (T0){ 
		T1 = B <= 4; 
		if (T1){ 
			printf("%s", "..."); 
		} 
	} 
	T2 = B + 1; 
	B = T2; 
	T3 = B + 2; 
	B = T3; 
	T4 = B + 3; 
	B = T4; 
	D = B; 
	C = 5; 
	printf("%s", ""); 
	printf("%d", D); 

	return 0;
}