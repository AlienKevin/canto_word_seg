import evaluate
import json
import pycantonese
import cantoseg
from tqdm import tqdm
import re
import pygtrie
import functools

def flatten_list(l):
    return [item for sublist in l for item in sublist]


def tokens_to_tags(tokens):
    return flatten_list([["B"] if len(token) == 1 else list("B" + "I" * (len(token) - 1)) for token in tokens])


def pycantonese_seg(sent):
    sent = re.sub(r'(?<=[a-zA-Z0-9.]) (?=[a-zA-Z0-9.])', r'空', sent)
    return pycantonese.segment(sent)


def cantoseg_seg(sent):
    sent = re.sub(r'(?<=[a-zA-Z0-9.]) (?=[a-zA-Z0-9.])', r'空', sent)
    return cantoseg.cut(sent)


def presegment_alphanum(s):
    pattern = r'\s*([a-zA-Z0-9-]+)\s*'
    segmented = re.sub(pattern, r' \1 ', s).strip()
    tokens = segmented.split()
    return tokens

@functools.cache
def get_cybercan_dict(ltr: bool = True):
    dict = pygtrie.CharTrie()
    with open("data/CyberCan.dict", "r") as f:
        for line in f:
            word, freq = line.rstrip().split(' ')
            dict[word if ltr else word[::-1]] = int(freq)
    return dict


def cybercan_seg(s: str, ltr: bool = True):
    s = re.sub(r'(?<=[a-zA-Z0-9.]) (?=[a-zA-Z0-9.])', r'空', s)
    tokens = []
    preseg_tokens = presegment_alphanum(s)
    preseg_tokens = preseg_tokens if ltr else preseg_tokens[::-1]
    for token in preseg_tokens:
        if re.match(r'^[a-zA-Z0-9-]+$', token) or token == " ":
            tokens.append(token)
        else:
            token = token if ltr else token[::-1]
            while token:
                p = get_cybercan_dict(ltr).longest_prefix(token)
                if p:
                    n = len(p.key)
                    tokens.append(token[:n] if ltr else token[:n][::-1])
                    token = token[n:]
                else:
                    tokens.append(token[0])
                    token = token[1:]
    tokens = tokens if ltr else tokens[::-1]
    return tokens


def diff_labels(pred_label, gold_label):
    if len(pred_label) != len(gold_label):
        raise ValueError("Sequences must have the same length")

    b_indices = []
    i_indices = []

    for i in range(len(pred_label)):
        if pred_label[i] == 'B' and gold_label[i] == 'I':
            b_indices.append(i)
        if pred_label[i] == 'I' and gold_label[i] == 'B':
            i_indices.append(i)

    return (b_indices, i_indices)

def highlight_string_diff(string, diff_indices):
    highlighted_string = ""
    (b_indices, i_indices) = diff_indices

    for i in range(len(string)):
        if i in b_indices:
            highlighted_string += "\033[91m" + string[i] + "\033[0m"  # Red color
        elif i in i_indices:
            highlighted_string += "\033[94m" + string[i] + "\033[0m"  # Green color
        else:
            highlighted_string += string[i]

    return highlighted_string


def test_performance(gold_file):
    metric = evaluate.load("seqeval")

    gold_labels = []
    pred_labels = []
    wrong_labels = []

    with open(gold_file, "r") as f:
        lines = f.readlines()
        for line in tqdm(lines):
            json_line = json.loads(line)
            sent = "".join(json_line["words"]).replace("\u3000", " ") # replace full-width space with half-width space
            pred_label = tokens_to_tags(cybercan_seg(sent, ltr=False))
            gold_label = json_line["ner"]
            if len(pred_label) != len(gold_label):
                print(sent)
                print(pred_label)
                print(gold_label)
                print()
            pred_labels.append(pred_label)
            gold_labels.append(gold_label)
            if pred_label != gold_label:
                wrong_labels.append((sent, pred_label, gold_label))
    result = metric.compute(predictions=pred_labels, references=gold_labels)
    print("=== " + gold_file + " performance ===")
    print(result)
    # for (sent, pred_label, gold_label) in wrong_labels:
    #     diff_indices = diff_labels(pred_label, gold_label)
    #     print(highlight_string_diff(sent, diff_indices))

if __name__ == '__main__':
    # print(cybercan_seg("我今日去香港大學。"))
    # print(cybercan_seg("Shopping? 唔好啦，上年shop過一次，差啲過唔到年!"))
    # print(cybercan_seg("hea吓hea吓，唔好咁hea，hea咗成日"))
    # print(cybercan_seg("Wiki最頂果度可以揀香港繁體同台灣正體"))

    # print(cybercan_seg("我今日去香港大學。", ltr=False))
    # print(cybercan_seg("Shopping? 唔好啦，上年shop過一次，差啲過唔到年!", ltr=False))
    # print(cybercan_seg("hea吓hea吓，唔好咁hea，hea咗成日", ltr=False))
    # print(cybercan_seg("Wiki最頂果度可以揀香港繁體同台灣正體", ltr=False))
    test_performance("data/finetune_hkcancor.json")
    test_performance("data/finetune_cityu.json")
