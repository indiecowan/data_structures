import time

''' already searched whole thing... do we need to search whole thing again? make set of needed complements for next round and check if new one is in the set??? '''
def solution(a, m, k):
    # optimize by including all arrays containing winners after winners found
    # print("a:", a)
    # print("m:", m)
    # print("k:", k)
    result = 0
    last_match_start = -1 # start of last found valid pair
    for sub_start in range (len(a) - m + 1):
        sub_end = sub_start + m - 1
        print("_____________newloop_____________")
        print("sub_start:", sub_start, "   sub_end:", sub_end)
        print("last_match_start:", last_match_start)
        if last_match_start >= sub_start:
            print("RESULT + 1") 
            result += 1
            continue
        # optimize by looking for specific matching value
        seen_set = set()
        for i in range(sub_end, sub_start - 1, -1):
            print("i:", i, "   a[i]:", a[i])
            print("seen_set:", seen_set)
            complement = k - a[i]
            if complement in seen_set:
                last_match_start = i
                print("RESULT + 1")
                result += 1
                break
            seen_set.add(a[i])
            time.sleep(2)
                
    return result

def test_solution():
    # Test case for the provided example
    assert solution([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 4, 10) == 5
    assert solution([15, 8, 8, 2, 6, 4, 1, 7], 2, 8) == 2

    # Edge case: smallest array with m = a.length
    assert solution([1, 2], 2, 3) == 1
    assert solution([1, 2], 2, 4) == 0

    # Edge case: largest value in the array
    assert solution([10**9, 10**9], 2, 2*10**9) == 1
    assert solution([10**9, 10**9], 2, 10**9 - 1) == 0

    # Edge case: k = 0 with repeated zeros and distinct numbers
    assert solution([0, 0, 1, 2, 3], 3, 0) == 1
    assert solution([0, 5, 0, 1, 2, 3], 3, 0) == 1
    assert solution([1, 2, 3, 4, 5], 3, 0) == 0

    print("All tests passed!")

import time

def test_solution_large_inputs():
    # Generate a large array of sequential integers
    large_array = list(range(10**5))
    
    # Edge case: largest array, m = a.length
    # start_time = time.time()
    # solution(large_array, 10**5, 10**9)
    # end_time = time.time()
    # print(end_time - start_time)
    # assert end_time - start_time < 4

    # Edge case: largest array, m is half the size
    start_time = time.time()
    solution(large_array, 10**5 // 2, 10**9)
    end_time = time.time()
    print(end_time - start_time)
    assert end_time - start_time < 4

    # Edge case: largest array, m is a small constant
    start_time = time.time()
    solution(large_array, 3, 10**9)
    end_time = time.time()
    print(end_time - start_time)
    assert end_time - start_time < 4
    
    print("All large input tests passed within time limits!")



# Run the test
# test_solution()
# Run the large input tests
test_solution_large_inputs()
