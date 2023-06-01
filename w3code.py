def string_similarity(str1, str2):
    count = 0
    for char1 in str1:
        if char1 in str2:
            count += 1
    similarity = count / max(len(str1), len(str2))
    return similarity

string1 = input('Enter string 1: ')
string2 = input('Enter string 2: ')

similarity_score = string_similarity(string1, string2) * 100
print(f"String similarity: {similarity_score}")