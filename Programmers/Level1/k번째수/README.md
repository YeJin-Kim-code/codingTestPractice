# [Programmers] K번째수 (Python)

## 📝 문제 설명
배열 `array`의 `i`번째 숫자부터 `j`번째 숫자까지 자르고 정렬했을 때, `k`번째에 있는 수를 구하려 합니다.

- **입력**: 1차원 배열 `array`, `[i, j, k]`를 원소로 가진 2차원 배열 `commands`
- **출력**: 각 명령을 적용한 결과들을 담은 1차원 배열

---

## 💡 풀이 접근 방식
파이썬의 **리스트 슬라이싱(Slicing)**과 **정렬(Sorting)** 기능을 활용하여 해결했습니다. 
문제에서 제시하는 순서(1-based index)와 파이썬 리스트의 인덱스(0-based index) 차이를 보정하는 것이 핵심입니다.

1. **배열 자르기**: `i번째`부터 `j번째`까지 자르기 위해 `array[i-1:j]` 슬라이싱을 사용합니다. (파이썬 슬라이싱의 끝 인덱스는 포함되지 않으므로 `j`까지 지정해야 `j-1` 인덱스인 j번째 원소까지 포함됩니다.)
2. **정렬**: 자른 배열을 오름차순으로 정렬합니다.
3. **K번째 수 추출**: 정렬된 배열에서 `k번째` 수인 `k-1` 인덱스의 값을 결과 배열에 추가합니다.

---

## 💻 코드 구현

### 1. 직관적인 풀이 (For 반복문)
```python
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        # 슬라이싱 후 정렬
        sliced = sorted(array[i-1:j])
        # k번째 수 추출
        answer.append(sliced[k-1])
    return answer
```

### 2. 파이써닉한 풀이 (List Comprehension)
```python
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]
```

---

## 🧠 배운 점 (Retrospective)
- 파이썬 슬라이싱 `[start:end]` 구조에서 `start`는 포함되고 `end`는 포함되지 않는 특성을 다시 한번 리마인드할 수 있었습니다.
- 리스트 컴프리헨션(List Comprehension)을 사용하면 반복문과 조건문이 포함된 코드를 훨씬 간결하고 가독성 있게 작성할 수 있음을 배웠습니다.
