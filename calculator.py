logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""




in1 = input("Input first number: ")
in2 = input("input operator:\n+\n-\n*\n/\n")
in3 = input("Input next number: ")


def calc(in1,in2,in3):

    cont = True
    while cont:

        exp = in1 + in2 + in3
        ans = eval(exp)
        print(ans)
        if input(f"Do you want to continue calculating with last value {ans}? y or n: ") == "y":
            in1 = str(ans)
            in2 = str(input("input operator:\n+\n-\n*\n/\n"))
            in3 = str(input("Input next number: "))
            calc(in1,in2,in3)
        else:
            cont = False
            calc(in1,in2,in3)


calc(in1,in2,in3)


        



