
def is_pallendrome(string_to_check):
    if string_to_check == "":
        return True
    if len(string_to_check) == 1:
        return True
    if string_to_check[0] != string_to_check[-1]:
        return False
    return is_pallendrome(string_to_check[1:-1])

def main():
    maybe_pallendrome = input("What string should we check for being a pallendrome:")
    answer = is_pallendrome(maybe_pallendrome)
    if answer:
        print("that was a Pallendrome!")
    else:
        print("Nope")

main()
