#include<iostream>
#include<vector>
using namespace std;

long long fun_c(long long n){
    return (n - 1) * n / 2;
}

int main(){
    int N,D;
    cin >> N >> D;
    long long count = 0;
    vector<int> res(N);
    for(int end = 0, begin = 0; end < N; end++){
        cin >> res[end];
        while (res[end] - res[begin] > D){
            begin++;
        }
        count += fun_c(end - begin);
    }
    cout << count % 99997867;
}