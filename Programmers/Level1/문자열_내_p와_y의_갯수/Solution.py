#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int len = s.length();
    int countP = 0;
    int countY = 0;
    for(int i=0; i<len; i++)
    {
        if(s[i] == 'p' ||s[i] == 'P')
        {
            countP++;
        }
        else if(s[i] == 'y' ||s[i] == 'Y')
        {
            countY++;
        }
    }

    if(countP!=countY)
    {
        answer = false;
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    //cout << answer << endl;

    return answer;
}
