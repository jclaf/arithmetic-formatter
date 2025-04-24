def arithmetic_arranger(problems, show_answers=False):
    line1 = line2 = line3 = line4 = ""
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else :
        for i in problems:
            cp = i.split()
            if not cp[0].isnumeric() or not cp[2].isnumeric():
                return 'Error: Numbers must only contain digits.'
            if len(cp[0])>4 or len(cp[2])>4:
                return 'Error: Numbers cannot be more than four digits.'
            if cp[1] != '+' and cp[1] != '-':
                return 'Error: Operator must be \'+\' or \'-\'.'
    
    for index, i in enumerate(problems):
        cp = i.split()
        space = '    ' if index < len(problems) - 1 else ''
        line1 += cp[0].rjust(max(len(cp[0]), len(cp[2]))+2)+space
        line2 += cp[1]+' '+cp[2].rjust(max(len(cp[0]), len(cp[2])))+space
        line3 +='-'*(max(len(cp[0]), len(cp[2]))+2)+space
        if show_answers:
            if cp[1] == '+':
                line4 += str(int(cp[0]) + int(cp[2])).rjust(max(len(cp[0]), len(cp[2]))+2)+space
            else :
                line4 += str(int(cp[0])-int(cp[2])).rjust(max(len(cp[0]), len(cp[2]))+2)+space
            final_problems = line1 + '\n'+line2+'\n'+line3+'\n'+line4
        else :
            final_problems = line1 + '\n'+line2+'\n'+line3
        #print(problems)
    return final_problems

if __name__ == "__main__":
    print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
    print(f'\n{arithmetic_arranger(["24 + 8215", "3801 - 2", "45 + 43", "123 + 49"])}')
    print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
