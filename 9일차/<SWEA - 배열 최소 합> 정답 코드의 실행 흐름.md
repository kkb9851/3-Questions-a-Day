이 코드는 **백트래킹(DFS) 알고리즘**을 활용하여 **N x N 행렬에서 각 행에서 하나씩 숫자를 선택하되, 열이 중복되지 않도록 하면서 합이 최소가 되는 경우를 구하는 문제**를 해결합니다.

주로 **순열을 이용한 최소 비용 문제**(예: 작업 순서, 배정 문제)에서 사용됩니다.

---

### 코드 구조 및 동작 설명

#### 1. **함수 정의: `dfs(n, total)`**

```python
def dfs(n, total):
    global answer
```

* `n`: 현재 선택한 행의 인덱스.
* `total`: 지금까지 선택한 숫자의 합.
* `answer`: 최소 합을 저장하는 전역 변수.

---

#### 2. **가지치기 (Pruning)**

```python
    if answer <= total:
        return
```

* 현재까지의 합 `total`이 이미 `answer`보다 크거나 같다면 더 이상 탐색하지 않고 가지를 자릅니다. (**효율성 증가**)

---

#### 3. **종료 조건**

```python
    if n == N:
        answer = min(answer, total)
        return
```

* 모든 행을 다 탐색한 경우(`n == N`), 현재 합 `total`이 최소라면 `answer`를 갱신.

---

#### 4. **DFS 탐색**

```python
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, total + arr[n][j])
            visited[j] = 0
```

* 열 인덱스 `j`를 순회하면서 아직 선택하지 않은 열(`visited[j] == 0`)에 대해:

  * 방문 표시 후, 다음 행 탐색 (`dfs(n+1, total + arr[n][j])`)
  * 탐색 후 방문 표시 해제(백트래킹)

> 이 부분은 N개의 열 중 중복되지 않게 하나씩 선택하는 **순열 탐색**을 의미합니다.

---

### 전체 실행 흐름

```python
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 100  # 충분히 큰 수로 초기화
    visited = [0]*N  # 열 사용 여부 체크
    dfs(0, 0)  # DFS 탐색 시작 (행 인덱스 0부터 시작)

    print(f"#{test_case} {answer}")
```

* 각 테스트 케이스마다:

  * `N x N` 행렬 입력을 받고,
  * `dfs(0, 0)` 호출로 탐색 시작.
  * 최솟값을 구해 출력.

---

### 예시

입력:

```
1
3
1 2 3
4 5 6
7 8 9
```

DFS는 아래와 같은 조합을 탐색:

* 1 + 5 + 9
* 1 + 6 + 8
* 2 + 4 + 9
* ...
  모든 행에서 하나씩 선택하면서 열 중복 없이 합이 최소가 되는 경우를 찾음.

---

### 요약

* **문제 유형**: 순열 + 백트래킹 + 최소 합
* **사용한 기법**:

  * DFS
  * 가지치기 (Pruning)
  * 백트래킹
* **복잡도**: O(N!) (N이 작을 때만 사용 가능)

