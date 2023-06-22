import glob
import subprocess
import re

if __name__ == "__main__":
    for f in glob.glob("../data/hkcancor_*_tagged.txt"):
        print(f"Training on {f}")
        match = re.search("hkcancor_([0-9]+)_tagged.txt", f)
        percent = match.group(1)
        subprocess.run(["crf_learn", "-c", "2", "template", f, "-t", f"../results/hkcancor_{percent}.model"]) 
