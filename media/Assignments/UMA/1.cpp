#include <stdio.h>
#include <string.h>
int max( char B[])
{
	int max=0;
	for (int i = 1; i < 10; ++i)
	{
		if(B[max]<B[i])
		{
			max=i;
		}
	}
	return max;
}
int main()
{
	char B[10], A[10][30]={	
{"Raguvanshi"},
{"M Radhakrishnan"},
{"Pauline Haddow"},
{"Sunil Chandran"},
{"Uma Gopinath"},
{"Soma Raju"},
{"T V Gopala Krishnan"},
{"Sudha Raghunath"},
{"Rajarshi Pal"},
{"Karthikeyan"}

				};
	for (int i = 0; i < 10; ++i)
	{	
		B[i]=strlen(A[i]);
		printf("%s \n",A[i]);

	}
	int k=max(B);
	printf("%s\n",A[k]);
	return 0;
}