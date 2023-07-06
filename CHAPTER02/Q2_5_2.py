# パターン1
answer = """○●●●
●○●●
●●○●
●●●○

"""
print(answer)

# パターン2
w = "○"
b = "●"
answer = (
    w + b * 3 + "\n" + b + w + b * 2 + "\n" + b * 2 + w + b + "\n" + b * 3 + w + "\n\n"
)
print(answer)

# パターン3
w = "○"
b = "●"
answer = ""
for i in range(4):
    for j in range(4):
        if i == j:
            answer += w
        else:
            answer += b
    answer += "\n"
print(answer)
