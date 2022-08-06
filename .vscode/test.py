import re
 
def clean_text(inputString):

    sentences = inputString.split(' ')
    a = []
    for sent in sentences:
        if '_' in sent: # 부록 양식에 해당
            sent = sent.replace(',', '') # 반점(,)이 있을 경우 바꿔서 정리
            a.append(sent)
            filtered = list(set(a))
    print(filtered,111)
    dict = {(i + 1): filtered[i] for i in range(0, len(filtered))}
    print(dict)
    return a

#   text_rmv = re.sub(someWords, '변환 ', inputString)
#   text_rmv = ' '.join(text_rmv.split())

input = 'Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously.[ some_paper_a, some_paper_b ] We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions.[ some_book_a, some_paper_a ] We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. [ some_book_b ]'
string = clean_text(input)
# print(string)