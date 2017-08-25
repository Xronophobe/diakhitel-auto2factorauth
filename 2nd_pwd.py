import sys

if __name__ == "__main__":
    try:
        passchars = sys.argv[1]
        authchars = map(int, sys.argv[2:])
    except IndexError:
        print("No passchars or selected characters were given.")
        print("usage: python 2nd_pwd.py <character set> <space separated "
              "required characters>")

    for ac in authchars:
        print(passchars[ac],end="")
    print("\n")
    print("I hope I made your life somewhat easier by automatizing the "
          "dumbest two factor authentication ever made. ")

