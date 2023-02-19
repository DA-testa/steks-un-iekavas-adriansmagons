# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    
    for i, next in enumerate(text):
        # enumerate atdod gan kartas nr gan simbolu
        if next in "([{":
            
            opening_brackets_stack.append(Bracket(next,i+1))
            
        
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()   
    if(not opening_brackets_stack):
        return "Success"
    else:
        return opening_brackets_stack[-1].position
    
    


def main():
    print("Input method:")
    tekstaievade = input()
    if tekstaievade.__contains__("I"):
        print("Input string:")
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)
    elif tekstaievade.__contains__("F"):
        print("Input path to file:")
        failapath = input()
        with open(failapath) as f:
            saturs = f.read()
        mismatch = find_mismatch(saturs)
        print(mismatch)


    
    
   

if __name__ == "__main__":
    main()
