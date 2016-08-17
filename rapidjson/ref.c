#include <stdio.h>

void quick(int *a,int i,int j) 
{ 
    int m,n,temp; 
    int k; 
    m=i; n=j; k=a[(i+j)/2]; /*选取的参照*/ 
    do { 
        while(a[m]<k&&m<j) m++; /* 从左到右找比k大的元素*/ 
        while(a[n]>k&&n>i) n--; /* 从右到左找比k小的元素*/ 
        if(m<=n) { /*若找到且满足条件，则交换*/ 
            temp=a[m]; a[m]=a[n]; a[n]=temp; 
            m++; n--; 
        } 
    }while(m<=n); 
    if(m + 1 < j) quick(a,m,j); /*运用递归*/ 
    if(n > i + 1) quick(a,i,n); 
} 

static int values[] = { 2, 10, 3, 4, 9, 42, 23 };

int main(void)
{
    unsigned idx;
    quick(values, 0, sizeof(values) / sizeof(values[0]) - 1);
    for (idx = 0; idx < sizeof(values) / sizeof(values[0]); ++idx)
        printf("%d, ", values[idx]);
    printf("\n");
    return 0;
}
