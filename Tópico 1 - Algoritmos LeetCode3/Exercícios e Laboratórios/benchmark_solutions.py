import time
import random
import string

# 1. Solução Força Bruta: O(N³)
def brute_force(s: str) -> tuple[int, int]:
    n = len(s)
    max_len = 0
    ops = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            ops += len(sub) # Custo de verificar duplicatas
            if len(set(sub)) == len(sub):
                max_len = max(max_len, len(sub))
    return max_len, ops

# 2. Solução Sliding Window com Set: O(2N) = O(N)
def sliding_window_set(s: str) -> tuple[int, int]:
    char_set = set()
    left = 0
    max_len = 0
    ops = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            ops += 1 # Passos extras de remoção
        char_set.add(s[right])
        ops += 1
        max_len = max(max_len, right - left + 1)
    return max_len, ops

# 3. Solução Sliding Window com Hash Map (Pulo Direto): O(N) Estrito
def sliding_window_map(s: str) -> tuple[int, int]:
    char_map = {}
    left = 0
    max_len = 0
    ops = 0
    for right, char in enumerate(s):
        ops += 1
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1 # Salto em O(1)
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len, ops

def run_benchmarks():
    sizes = [100, 500, 1000, 5000, 20000, 50000]
    results = []

    print(f"{'Tamanho (N)':<12} | {'Força Bruta O(N³)':<22} | {'Sliding Window Set':<22} | {'Sliding Window Map (Nossa)':<25}")
    print("-" * 90)

    for N in sizes:
        # Gera string aleatória com alfabeto de 26 letras
        random.seed(42)
        test_str = ''.join(random.choices(string.ascii_lowercase, k=N))

        # Mede Força Bruta (apenas para N <= 1000 para não travar)
        if N <= 1000:
            t0 = time.perf_counter()
            ans_bf, ops_bf = brute_force(test_str)
            t_bf = time.perf_counter() - t0
            bf_str = f"{t_bf*1000:.2f} ms ({ops_bf:,} ops)"
        else:
            # Projeção matemática para N > 1000
            t_est = (N / 1000)**3 * 0.12 # baseado no tempo de N=1000
            ops_est = (N**3) // 6
            if t_est > 60:
                bf_str = f"~{t_est/60:.1f} min ({ops_est:,} ops)"
            else:
                bf_str = f"~{t_est:.1f} s ({ops_est:,} ops)"

        # Mede Sliding Window Set
        t0 = time.perf_counter()
        ans_set, ops_set = sliding_window_set(test_str)
        t_set = time.perf_counter() - t0
        set_str = f"{t_set*1000:.3f} ms ({ops_set:,} ops)"

        # Mede Sliding Window Map
        t0 = time.perf_counter()
        ans_map, ops_map = sliding_window_map(test_str)
        t_map = time.perf_counter() - t0
        map_str = f"{t_map*1000:.3f} ms ({ops_map:,} ops)"

        print(f"{N:<12} | {bf_str:<22} | {set_str:<22} | {map_str:<25}")

if __name__ == "__main__":
    run_benchmarks()
