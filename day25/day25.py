

def snafu_to_dec(snafu: str) -> int:
    ret = []
    for i,c in enumerate(snafu[::-1]):
        if c.isnumeric():
            base = int(c)
        elif c == '-':
            base = -1
        elif c == '=':
            base = -2
        else:
            raise RuntimeError(f'unrecognized char {c}')
        ret.append(base * (5**i))

    return sum(ret)

def dec_to_snafu(dec: int) -> str:
    ret = ''

    while dec: 
        last_digit = dec % 5 # if least significant digit base 5 is less than 3, then it can be represented in this str
        
        if last_digit < 3:
            ret += str(last_digit)
            dec //= 5
        else:
            # otherwise 4 -> -1 and 3 -> -2, and carry 1 since
            # 4*5 - (-1*5) = 25 and 3*5 - (-2*5) = 25 so the digit in the 5^2's place is incremented
            if last_digit == 4:
                ret += '-'
            else:
                ret += '='
            dec = (dec // 5) + 1

    return ret[::-1]

with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

    ans = []
    for line in data:
        ans.append(snafu_to_dec(line))

    temp = sum(ans)
    print(temp)
    ans = dec_to_snafu(temp)
    print(ans)