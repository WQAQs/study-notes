#include<iostream>  
#include<algorithm>  
using namespace std;  
#define maxn 100  
int num[maxn];  

template<class Type>  
void Merge(Type a[],Type b[],int left,int mid,int right)  
{  
     int i=left;                
     int j=mid+1;  
     int k=left;  
     while(i<=mid && j<=right)  
     {  
           if(a[i]<a[j])    
                b[k++]=a[i++];  
           else   
                b[k++]=a[j++];  
     }     
     if(i>mid)   
          for(int z=j;z<=right;z++)  
               b[k++]=a[z];  
     else  
          for(int z=i;z<=mid;z++)  
               b[k++]=a[z];  
}   


//合并大小为s的相邻子数组    
template<class Type>  
void MergePass(Type x[],Type y[],int s,int n)  
{  
     int i=0;  
     while(i+2*s-1<n)  
     {  
           Merge(x,y,i,i+s-1,i+2*s-1);  
           //合并大小为s的相邻2段子数组   
           i+=2*s;       
     }   
     if(i+s<n)
     //剩下的元素个数m满足：s<= m <2*s   
           Merge(x,y,i,i+s-1,n-1);  
     else                              
     //剩下的元素个数m满足：m<s  
           for(int j=i;j<=n-1;j++)  
                y[j]=x[j];  
}      
template<class Type>  
void MergeSort(Type c[],int n)  
{  
     Type *d=new Type [n];   
     int  s=1;  
     while(s<n)  
     {  
           MergePass(c,d,s,n);  //合并到数组d   
           s+=s; 
           //就像图中有序的两个合并为一个 
           MergePass(d,c,s,n);  //合并到数组c   ?????
           s+=s;                
     }
     delete[] b;  
}   
int  main()  
{   
    int n;  
    //  while(cin>>n)  
    //  {  
    //       for(int i=0;i<n;i++)  
    //            cin>>num[i];      
    //       MergeSort(num,n);     
    //       for(int i=0;i<n;i++)  
    //            cout<<num[i]<<endl;                         
    //  }   
    int nums[5] = {3,1,4,2,6};
    n = 5;
    MergeSort(nums,n);
    return 0;         
}   
/* 
8 
8  3  2  6  7  1  5  4  

7 
49 38 65 97 76 13 27 

5 
49  38  65  97  76 
*/  