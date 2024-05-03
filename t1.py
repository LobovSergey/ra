i = int(input())
ends = {
    1: "",
    2: "а",
    5: "ов"
}
os = i % 20
if os == 1:
    res = 1
elif 2 <= os < 5:
    res = 2
else:
    res = 5
st = f"компьютер{ends[res]}"
print(i, st)
