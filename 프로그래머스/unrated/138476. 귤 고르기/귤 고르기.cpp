#include <string>
#include <vector>
#include <algorithm>
#define MAX 10000001
using namespace std;


int solution(int k, vector<int> tangerine) {
    int answer = 0;
    vector<int> kind(MAX);
    
    for (int t: tangerine) {
        kind[t]++;
    }
    
    sort(kind.begin(), kind.end(), greater<int>());
    
    for (int i=0; i<kind.size(); i++) {
        if (k > 0) {
            answer += 1;
            k -= kind[i];
        } else {
            break;
        }
    }
    return answer;
}