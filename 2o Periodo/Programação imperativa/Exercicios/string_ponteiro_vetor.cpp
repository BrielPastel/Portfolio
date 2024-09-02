#include <stdio.h>
#include <string.h>

int main(){
	char material[] = "Concreto";
	
	char* p = material;
	printf("%s\n", material);
	
	putchar(*p);
	putchar('\n');
	
	p++;
	putchar(*p);
	putchar('\n');
	
	p = &material[4];
	putchar(*p);
	putchar('\n');
	
	*p = 'l';
	printf("%s\n", material);
}
