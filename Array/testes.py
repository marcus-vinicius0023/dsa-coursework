import bisect
import random
import traceback

from exponential_search import exponential_search, binary_search

def expected_index_sorted(arr, target):
    """Retorna o índice esperado (ou None) para array crescente."""
    i = bisect.bisect_left(arr, target)
    return i if i < len(arr) and arr[i] == target else None

def assert_result_ok(arr, target, result, *, allow_any_duplicate_index=False):
    """Valida (index, steps)."""
    assert isinstance(result, tuple) and len(result) == 2, f"Retorno não é tupla (idx, steps): {result}"
    idx, steps = result
    assert isinstance(steps, int) and steps >= 0, f"steps inválido: {steps} (target={target}, arr_len={len(arr)})"

    exp = expected_index_sorted(arr, target)

    if exp is None:
        assert idx is None, f"Esperado None, mas veio idx={idx} (target={target})"
        return

    # target existe
    assert idx is not None, f"Esperado um índice, mas veio None (target={target})"
    assert 0 <= idx < len(arr), f"Índice fora do array: idx={idx}, len={len(arr)}"
    assert arr[idx] == target, f"Índice não aponta para o target: arr[idx]={arr[idx]} target={target}"

    # Se o array tiver duplicatas, você pode aceitar qualquer ocorrência.
    # Nos testes fuzz eu uso arrays únicos, então dá pra exigir igualdade exata do índice esperado.
    if not allow_any_duplicate_index:
        assert idx == exp, f"Índice diferente do esperado: idx={idx} exp={exp} target={target}"

def run_deterministic_tests(exponential_search, binary_search):
    cases = [
        # vazios / 1 elemento
        ([], 10),
        ([5], 5),
        ([5], 4),
        ([5], 6),

        # pequenos
        ([1, 3], 1),
        ([1, 3], 3),
        ([1, 3], 2),
        ([1, 3], 0),
        ([1, 3], 4),

        ([1, 2, 3, 4, 5], 1),
        ([1, 2, 3, 4, 5], 5),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 0),
        ([1, 2, 3, 4, 5], 6),

        # caso que historicamente pega bug de "right > len(arr)" no inverted (target bem menor)
        ([10, 20, 30, 40, 50, 60, 70], -100),

        # caso com gaps grandes
        ([10, 100, 1000, 10000, 100000], 10000),
        ([10, 100, 1000, 10000, 100000], 9999),

        # duplicatas (aqui aceitamos qualquer ocorrência)
        ([1, 2, 2, 2, 3, 4], 2),
        ([1, 2, 2, 2, 3, 4], 5),
    ]

    for arr, target in cases:
        # binary (seu retorno pode pegar qualquer ocorrência em duplicatas, mas em geral ok)
        res_b = binary_search(arr, target)
        allow_dups = (len(arr) != len(set(arr)))
        assert_result_ok(arr, target, res_b, allow_any_duplicate_index=allow_dups)

        # exponential normal
        res_e = exponential_search(arr, target, inverted=False)
        assert_result_ok(arr, target, res_e, allow_any_duplicate_index=allow_dups)

        # exponential invertido
        res_i = exponential_search(arr, target, inverted=True)
        assert_result_ok(arr, target, res_i, allow_any_duplicate_index=allow_dups)

    print("Deterministic tests: OK")

def run_fuzz_tests(exponential_search, binary_search, *, seed=1234, rounds=500):
    rng = random.Random(seed)

    for _ in range(rounds):
        n = rng.randint(0, 300)

        # gera valores únicos e ordena (evita o detalhe de duplicatas nos asserts)
        pool = set()
        while len(pool) < n:
            pool.add(rng.randint(-2000, 2000))
        arr = sorted(pool)

        # escolhe alvos: alguns dentro, alguns fora
        for __ in range(30):
            if n > 0 and rng.random() < 0.6:
                target = arr[rng.randrange(n)]
            else:
                target = rng.randint(-3000, 3000)

            # Comparar com "expected" (via bisect)
            try:
                res_b = binary_search(arr, target)
                assert_result_ok(arr, target, res_b)

                res_e = exponential_search(arr, target, inverted=False)
                assert_result_ok(arr, target, res_e)

                res_i = exponential_search(arr, target, inverted=True)
                assert_result_ok(arr, target, res_i)

            except Exception as e:
                print("\nFalha no fuzz test!")
                print(f"arr_len={len(arr)} target={target}")
                print("arr (primeiros 50):", arr[:50])
                print("binary:", res_b if 'res_b' in locals() else None)
                print("exp normal:", res_e if 'res_e' in locals() else None)
                print("exp inverted:", res_i if 'res_i' in locals() else None)
                traceback.print_exc()
                raise e

    print("Fuzz tests: OK")

def run_all_tests(exponential_search, binary_search):
    run_deterministic_tests(exponential_search, binary_search)
    run_fuzz_tests(exponential_search, binary_search)


run_all_tests(exponential_search, binary_search)