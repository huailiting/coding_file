#funtion :compare the the two string 
#include<stdio.h>
#define SIZE1 100
#define SIZE2 100
void main()
{
 char s1[SIZE1],s2[SIZE2];
 int i=0;
 gets(s1);
 gets(s2);
 while(s1[i]==s2[i]&&s1[i]!='\0'&&s2[i]!='\0')
 i++;
 if (s1[i]>s2[i])
        printf("1\n");
 else if (s1[i]<s2[i])
        printf("-1\n");
 else
        printf("0");

}
