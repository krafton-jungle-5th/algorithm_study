import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    # list는 in연산자 사용시 for문을 한번 도는것과 같음(O(n))
    # set은 in연산자 사용시 시간복잡도는 O(1)
    # https://dong-hyeok.tistory.com/entry/Python-List-Set-Dict-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84Big-O
    n_list = set(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))

    for i in m_list:
        if i in n_list:
            print("1")
        else:
            print("0")


solution()
