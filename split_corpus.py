import random
import pycantonese
import json

from finetune_hkcancor import tag_hkcancor

if __name__ == '__main__':
    percents = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    hkcancor = pycantonese.hkcancor()
    lines = hkcancor.tokens(by_utterances=True)
    random.Random(42).shuffle(lines)
    for percent in percents:
        with open("data/hkcancor_" + str(percent) + ".txt", "w") as o:
            for i in range(int(len(lines) * percent / 100)):
                o.write(" ".join([token.word for token in lines[i]]) + "\n")
    with open("data/hkcancor_test.jsonl", "w") as o:
        tagged_entries = tag_hkcancor(lines[int(len(lines) * percent / 100):])
        for entry in tagged_entries:
            json.dump(entry, o, ensure_ascii=False)
            o.write('\n')
