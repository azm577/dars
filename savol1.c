#include <stdio.h>
#include <stdlib.h>
void hesapmakinesi(float a,float b,float c,char t){
    system("cls");
    printf("\n---Hesap Makinesi---");
    printf("\n                    ");
    printf("\n                    ");
    printf("\n % .1f  %s  %.1f = %.1f", a , t ,  b, c );
    printf("\n                    ");
    printf("\n| 1 || 2 || 3 || + |");
    printf("\n| 4 || 5 || 6 || - |");
    printf("\n| 7 || 8 || 9 || / |");
    printf("\n| 0 ||00 || C || * |");
    printf("\nExit : 1");
    printf("\nContunie : 0");

}

int main()
{
    system("cls");
    
    float a = 0;
    float b =  0;
    char t[0];
    float c = 0;
    int exit = 1;
    while(exit == 1){
    hesapmakinesi(a,b,c, *t);
    printf("\nSonni Kiriting: ");
    scanf("%f", &a);
    printf("\nNima kilish kereligini yozing: ");
    scanf("%s", t);
    printf("\n2. Sonni Kiriting: ");
    scanf("%f", &b);
    switch(t)Ğ
    
    hesapmakinesi(a,b,c,*t);


    scanf("%d", exit);
    }
    
}
