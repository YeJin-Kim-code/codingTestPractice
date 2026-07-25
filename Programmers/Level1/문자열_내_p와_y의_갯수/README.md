대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.


def solution(s):
    answer = True
    
    return s.lower().count('p') == s.lower().count('y')


핵심 포인트 설명
s.lower(): 대소문자를 구분하지 않기 위해 문자열을 모두 소문자로 변환합니다.
.count('p'): 문자열 내에서 특정 문자('p' 또는 'y')가 몇 개 있는지 바로 세어주는 파이썬 내장 메서드입니다.
== 연산: 두 개수가 같으면 알아서 True를, 다르면 False를 리턴하므로 if문조차 쓸 필요가 없습니다. (참고로 파이썬은 불리언 첫 글자가 대문자 True, False입니다.)
