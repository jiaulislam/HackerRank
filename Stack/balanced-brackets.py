def check_validity(string):
    open_brackets = ["(", "[", "{"]
    close_brackets = [")", "]", "}"]
    stack = []

    for char in string:
        if char in open_brackets:
            stack.append(char)
        else:
            if not stack:
                return "NO"
            current_char = stack.pop()
            if current_char == open_brackets[0]:
                if char != close_brackets[0]:
                    return "NO"
            if current_char == open_brackets[1]:
                if char != close_brackets[1]:
                    return "NO"
            if current_char == open_brackets[2]:
                if char != close_brackets[2]:
                    return "NO"
    if stack:
        return "NO"
    else:
        return "YES"

if __name__=="__main__":
    n = int(input())
    for _ in range(n):
        string = input()
        print(check_validity(string))
