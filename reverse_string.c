#funtion: reverse the string
#include<stdio.h>
#include<string.h>
#define SIZE1 100
#define SIZE2 100
void main()
{
        char s1[SIZE1],s2[SIZE2];
        int i,j;
        printf("input the string:\n");
        scanf("%s",&s1[0]);
        for(i=0;s1[i]!=0;i++);
        for(j=0;s1[j]!=0;j++)
                s2[i-j-1]=s1[j];
         s2[i]='\0';
        printf("%s",s2);

}
~                                                                               
~   