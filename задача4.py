# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

# encode
data = "ddddfffrrrgkdooowwiiienrnnnnn"
pre_symbol = data[0]
count = 1
result_encode = ''
for i in data[1:]:
    if i == pre_symbol:
        count += 1
    else:
        result_encode += str(count) + pre_symbol
        pre_symbol = i
        count = 1
result_encode += str(count) + pre_symbol
print(result_encode)

# decode
char = ''
result_decode = ''
for i in result_encode:
    if i.isdigit():
        char += i
    else:
        result_decode += i*int(char)
        char = ''
print(result_decode)


""" with open("text1.txt", "r") as t1:
    s = str(t1)
    pre_symbol = s[0]
    count = 1
    result_encode = []
    for i in s[1:]:
        if i == pre_symbol:
            count += 1
        else:
            result_encode.append(str(count) + pre_symbol)
            pre_symbol = i
            count = 1
    result_encode.append(str(count) + pre_symbol)
with open("text2.txt", "w") as t2:
    t2.writelines(result_encode) """


# char = ''
# result_decode = ''
# for i in result_encode:
#     if i.isdigit():
#         char += i
#     else:
#         result_decode += i*int(char)
#         char = ''
# print(result_decode)
