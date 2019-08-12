'''Python Program to Remove Punctuation from a String
"Woman, without her man, is nothing" (the sentence boasting about men's importance.)
"Woman: without her, man is nothing" (the sentence boasting about women's importance.)'''
#'''!()-[]{};:'",<>./?@#$%^&*_~'

# splits1 = "Woman, without her man, is nothing"
# list1 = splits1.split(",")
# print(list1)

# for x in list1:
#     print(x ,end="")

# splits1 = "Woman, without her man, is nothing"
# for x in splits1:
#     if (x <= "/" and x >= "!") or (x <= "@" and x >= ":") or (x <= "`" and x >= "[") or (x <= "~" and x >= "{"):
#         continue
#     else:
#         print(x,end="")

splits1 = "Woman, without her man, is nothing"
splits2 = "Woman: without her, man is nothing"
for x in splits1:
    if (x <= "z" and x >= "a") or (x <= "Z" and x >= "A") or x == " ":
        print(x,end= "")
    else:
        continue




