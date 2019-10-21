#include<stdio.h>


#define TRUE 1
#define FALSE 0

typedef int BOOL;

BOOL ChkPrime(int val)
 {
 
   int x=0;
   
   for(int i=2;i<=val/2;i++)
    {    	
       if(val%i==0)
       {    
        x++;    
       	break;
       }	
    }
 
   if (x>0)
   {
    return FALSE; 
   }
   else
   {
    return TRUE;
   }
 
 }
 
 
 int main()
 {
 
   int val=0;
   printf("Enter a val: ");
   scanf("%d",&val);
   BOOL Res=ChkPrime(val);
   
   if(Res==TRUE)
   {
    printf("Given Num is Prime\n");
   }
   else 
   {
    printf("Given Num is Not Prime\n"); 
   }
   
  
  return 0; 
 }
