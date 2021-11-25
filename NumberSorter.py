print("Hello! Im your number sorter!")
print("Give me 4 random numbers and I'll arrange it from Highest to Lowest.")

First = int(input("FirstNumber: "))
Second = int(input("SecondNumber: "))
Third = int(input("ThirdNumber: "))
Fourth = int(input("FourthNumber: "))

if First <= Second and Second <= Third and Third <= Fourth:
    print(f"The Descending order is {Fourth}, {Third}, {Second}, {First}.")
else: 
    if First <= Second and Second <= Fourth and Fourth <= Third:
        print(f"The Descending order is {Third}, {Fourth}, {Second}, {First}.")
    else:
        if First <= Third and Third <= Second and Second <= Fourth:
            print(f"The Descending order is {Fourth}, {Second}, {Third}, {First}.")
        else:
            if First <= Third and Third <= Fourth and Fourth <= Second:
                print(f"The Descending order is {Second}, {Fourth}, {Third}, {First}.")
            else:
                if First <= Fourth and Fourth <= Second and Second <= Third:
                    print(f"The Descending order is {Third}, {Second}, {Fourth}, {First}.")
                else:
                    if First <= Fourth and Fourth <= Third and Third <= Second:
                        print(f"The Descending order is {Second}, {Third}, {Fourth}, {First}.")
                    else:
                        if Second <= First and First <= Third and Third <= Fourth:
                            print(f"The Descending order is {Fourth}, {Third}, {First}, {Second}.")
                        else:
                            if Second <= First and First <= Fourth and Fourth <= Third:
                                print(f"The Descending order is {Third}, {Fourth}, {First}, {Second}.")
                            else:
                                if Second <= Third and Third <= First and First <= Fourth:
                                    print(f"The Descending order is {Fourth}, {First}, {Third}, {Second}.")
                                else:
                                    if Second <= Third and Third <= Fourth and Fourth <= First:
                                        print(f"The Descending order is {First}, {Fourth}, {Third}, {Second}.")
                                    else:
                                        if Second <= Fourth and Fourth <= First and First <= Third:
                                            print(f"The Descending order is {Third}, {First}, {Fourth}, {Second}.")
                                        else:
                                            if Second <= Fourth and Fourth <= Third and Third <= First:
                                                print(f"The Descending order is {First}, {Third}, {Fourth}, {Second}.")
                                            else:
                                                if Third <= First and First <= Second and Second <= Fourth:
                                                    print(f"The Descending order is {Fourth}, {Second}, {First}, {Third}.")
                                                else:
                                                    if Third <= First and First <= Fourth and Fourth <= Second:
                                                        print(f"The Descending order is {Second}, {Fourth}, {First}, {Third}.")
                                                    else:
                                                        if Third <= Second and Second <= First and First <= Fourth:
                                                            print(f"The Descending order is {Fourth}, {First}, {Second}, {Third}.")
                                                        else:
                                                            if Third <= Second and Second <= Fourth and Fourth <= First:
                                                                print(f"The Descending order is {First}, {Fourth}, {Second}, {Third}.")
                                                            else:
                                                                if Third <= Fourth and Fourth <= First and First <= Second:
                                                                    print(f"The Descending order is {Second}, {First}, {Fourth}, {Third}.")
                                                                else:
                                                                    if Third <= Fourth and Fourth <= Second and Second <= First:
                                                                        print(f"The Descending order is {First}, {Second}, {Fourth}, {Third}.")
                                                                    else:
                                                                        if Fourth <= First and First <= Second and Second <= Third:
                                                                            print(f"The Descending order is {Third}, {Second}, {First}, {Fourth}.")
                                                                        else:
                                                                            if Fourth <= First and First <= Third and Third <= Second:
                                                                                print(f"The Descending order is {Second}, {Third}, {First}, {Fourth}.")
                                                                            else:
                                                                                if Fourth <= Second and Second <= First and First <= Third:
                                                                                    print(f"The Descending order is {Third}, {First}, {Second}, {Fourth}.")
                                                                                else:
                                                                                    if Fourth <= Second and Second <= Third and Third <= First:
                                                                                        print(f"The Descending order is {First}, {Third}, {Second}, {Fourth}.")
                                                                                    else:
                                                                                        if Fourth <= Third and Third <= First and First <= Second:
                                                                                            print(f"The Descending order is {Second}, {First}, {Third}, {Fourth}.")
                                                                                        else:
                                                                                            if Fourth <= Third and Third <= Second and Second <= First:
                                                                                                print(f"The Descending order is {First}, {Second}, {Third}, {Fourth}.")
