def solution(x, n):
    answer = []
    
    # 1부터 n까지 1씩 증가하며 반복합니다.
    for num in range(1, n + 1):
        # x씩 증가하는 값을 배열에 추가합니다.
        answer.append(x * num)
        
    return answer
