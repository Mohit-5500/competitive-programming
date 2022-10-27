from collections import defaultdict, Counter
https://www.hackerrank.com/challenges/game-of-thrones/problem?isFullScreen=true



input_string=input()
reverse_input_string=input_string[::-1]


if input_string==reverse_input_string:
    print("YES")
else:
    my_dict = {}
    for letter in input_string:
        my_dict[letter] = my_dict.get(letter, 0) + 1
    count=0
    for i in my_dict.values():
        if i%2==1:
            count=count+1
    if count>1:
        print("NO")
    else:
        print("YES")
    

  





