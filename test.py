import re

def do_strip_html2(text):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in text:
        if i == '[':
            skip1c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret

# Example usage
input_string = "僕[ぼく]が正[まさ]しく導[みちび]かないと"
result = do_strip_html2(input_string)
print(result)  # Expected Output: "This is a sample text  and this ."

