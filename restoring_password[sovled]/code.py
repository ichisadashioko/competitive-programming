from __future__ import print_function
import sys

if __name__ == "__main__":
#     '''input
# 01001100100101100000010110001001011001000101100110010110100001011010100101101100
# 0100110000
# 0100110010
# 0101100000
# 0101100010
# 0101100100
# 0101100110
# 0101101000
# 0101101010
# 0101101100
# 0101101110
# '''
    encryted_password = input()
    n = 10
    split_password = [encryted_password[i:i+n]
                      for i in range(0, len(encryted_password), n)]

    num_code_list = []

    for i in range(10):
        num_code_list.append(input())

    decryted_password = ""

    for i in range(len(split_password)):
        for j in range(len(num_code_list)):
            if split_password[i] == num_code_list[j]:
                decryted_password += str(j)

    print(decryted_password)