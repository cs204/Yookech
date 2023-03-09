def Convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x
def main():
    x = input()
    s = Convert(x)
    print (s)
main()