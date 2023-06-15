import pycantonese

if __name__ == '__main__':
    with open("data/common_voice_sentences.txt", "r") as f, open("data/common_voice_gold.txt", "w") as o:
        for line in f.readlines():
            line.replace("/", "／")
            o.write("/".join(pycantonese.segment(line)) + "\n")
