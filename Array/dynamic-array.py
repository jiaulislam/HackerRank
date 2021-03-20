def dynamicArray(n, queries):
    new_arr=[[] for _ in range(n)]
    result = []
    lastAnswer = 0
    for query in queries:
        index = (query[1]^lastAnswer) % n
        if query[0] == 1:
            new_arr[index].append(query[-1])
        else:
            lastAnswer = new_arr[index][query[-1]%len(new_arr[index])]
            result.append(lastAnswer)
    return result
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))
