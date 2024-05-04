#include <iostream>
#include <math.h>
#include <cstring>
#include <queue>
#include <algorithm>

#define MAX 16
#define INF 987654321

using namespace std;

int testcase;
int n,ans;
int S[MAX][MAX];
int selected[MAX];

int getDifference(vector<int> &f1, vector<int> &f2){
    int synergy1 = 0;
    int synergy2 = 0;
    
    for(int i=0; i<n/2; i++){
        for(int j=0; j<n/2; j++){
            if(i==j) continue;
            
            synergy1 += S[f1[i]][f1[j]];
            synergy2 += S[f2[i]][f2[j]];
        }
    }
    
    return abs(synergy1 - synergy2);
}

void dfs(int ind,int cnt){
    if(cnt == n/2){
        vector<int> f1,f2;
        for(int i=0; i<n; i++){
            if(selected[i] == 1) f1.push_back(i);
            else f2.push_back(i);
        }
        
        ans = min(ans,getDifference(f1,f2));
        return;
    }
    
    for(int i=ind; i<n ;i++){
        if(selected[i] == 0){
            selected[i] = 1;
            dfs(i+1,cnt+1);
            selected[i] = 0;
        }
    }
}

int main(int argc, const char * argv[]) {
    // cin,cout 속도향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> testcase;
    
    for(int t=1; t<=testcase; t++){
        cin >> n;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                cin >> S[i][j];
            }
        }
        
        ans = INF;
        dfs(0,0);
        
        cout << "#" << t << " " << ans << "\n";
    }
    
    return 0;
}