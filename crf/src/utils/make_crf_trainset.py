import codecs  
import sys  
  
def character_tagging(input_file, output_file):  
    input_data = codecs.open(input_file, 'r', 'utf-8')  
    output_data = codecs.open(output_file, 'w', 'utf-8')  
    for line in input_data.readlines():  
        word_list = line.strip().split()  
        for word in word_list:  
            if len(word) == 1:  
                output_data.write(word + "\tS\n")  
            else:  
                output_data.write(word[0] + "\tB\n")  
                for w in word[1:len(word)-1]:  
                    output_data.write(w + "\tI\n")  
                output_data.write(word[len(word)-1] + "\tE\n")  
        output_data.write("\n")  
    input_data.close()  
    output_data.close()

if __name__ == '__main__':
    percents = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for percent in percents:
        character_tagging(f"../../../data/hkcancor_{round(percent * 100)}.txt", f"../../data/hkcancor_{round(percent * 100)}_tagged.txt")
