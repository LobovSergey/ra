import pandas as pd
n = int(input())
arr = [[0] * (n) for _ in range(n)]
col = [i for i in range(1, n+1)]
for i in range(n):
    for j in range(n):
        if i == 0:
            arr[i][j] = j + 1
        elif j == 0:
            arr[i][j] = i + 1
        else:
            arr[i][j] = arr[i][0] * arr[0][j]
df = pd.DataFrame(data=arr, columns=col, index=col)
print(df)
