#include <stdio.h>
#define p 1000000007
void multiply(long F[2][2], long M[2][2]);
 
void power(long F[2][2], long n);

long fib(long n)
{
  long F[2][2] = {{1,1},{1,0}};
  if (n == 0)
    return 0;
  power(F, n-1);
  return F[0][0];
}

void power(long F[2][2], long n)
{
  if( n == 0 || n == 1)
      return;
  long M[2][2] = {{1,1},{1,0}};
 
  power(F, n/2);
  multiply(F, F);
 
  if (n%2 != 0)
     multiply(F, M);
}
 
void multiply(long F[2][2], long M[2][2])
{
  long x =  (F[0][0]*M[0][0] + F[0][1]*M[1][0])%p;
  long y =  (F[0][0]*M[0][1] + F[0][1]*M[1][1])%p;
  long z =  (F[1][0]*M[0][0] + F[1][1]*M[1][0])%p;
  long w =  (F[1][0]*M[0][1] + F[1][1]*M[1][1])%p;
  F[0][0] = x;
  F[0][1] = y;
  F[1][0] = z;
  F[1][1] = w;
}
 
int main()
{
    long t;
    long n;
    scanf("%d",&t);
    while(t-->0)
    {
        scanf("%ld",&n);
        printf("%ld\n",fib(n));
    }
  return 0;
}