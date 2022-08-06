# @input
# Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously.[ some_paper_a, some_paper_b ] We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions.[ some_book_a, some_paper_a ] We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. [ some_book_b ]

# @output
# Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously.[ 1, 2 ] We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions.[ 1, 3 ] We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. [ 4 ]
# [1] some_paper_a
# [2] some_paper_b
# [3] some_book_a
# [4] some_book_b

import re
 
def clean_text(inputString):

    sentences = inputString.split(' ')
    appendix = []
    for word in sentences:
        if '_' in word: # 부록 양식에 해당
            word = word.replace(',', '') # 반점(,)이 있을 경우 바꿔서 정리
            appendix.append(word)
            # appendix에서 중복되는 key 제외하고 list로 만듦.
            new_list = list(dict.fromkeys(appendix))      # new_list = list(set(appendix)) # set은 중복은 제거하지만 순서는 마음대로여서 사용X
    final_list = {(i + 1): new_list[i] for i in range(0, len(new_list))}   # list에 index를 붙임.
    for (value,key) in zip(final_list.values(), final_list.keys()) :       # zip으로 두 개의 list 묶음.
        if value in inputString:
            inputString = inputString.replace(value, str(key))   
    print(inputString)    
    for (value,key) in zip(final_list.values(), final_list.keys()) : 
        print( '['+str(key)+'] '+value) 
    
input = 'Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously.[ some_paper_a, some_paper_b ] We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions.[ some_book_a, some_paper_a ] We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. [ some_book_b ]'
string = clean_text(input)

# 아쉬운 점 str 값이 아니라 int로 받고 정렬하는 방법은 없을까?

