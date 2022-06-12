# https://codeforces.com/problemset/problem/118/A

def main():
    my_str = input()
    my_str = my_str.lower()
    vowel = ['A', 'O', 'Y', 'E', 'U', 'I', 'a', 'o', 'y', 'e', 'u', 'i']
    new_str = ""
    for i in my_str:
        if i in vowel:
            continue
        new_str += "."
        new_str += i
    print(new_str)

if __name__ == "__main__":
    main()