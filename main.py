import re;

def GetIndexOfFirstVowel(Word):
    CurrentIndex = 0;

    for Letter in Word:
        if Letter in ['a', 'e', 'i', 'o', 'u']:
            return CurrentIndex;
        CurrentIndex += 1;  # CurrentIndex++ is not supported in Python

    return -1;  # Not vowels!


def TransformWord(Word):
    TransformedWord = Word;

    FirstVowelIndex = GetIndexOfFirstVowel(TransformedWord);

    if FirstVowelIndex != 0:  # First letter is consonant if it is not a vowel
        if FirstVowelIndex != -1:  # It contains at least 1 vowel
            Left, Right = TransformedWord[:FirstVowelIndex], TransformedWord[FirstVowelIndex:]
            TransformedWord = f"{Right}{Left}";
        TransformedWord = f"{TransformedWord}ay";

    else:
        TransformedWord = f"{TransformedWord}yay";

    return TransformedWord;


# Execution

InputFileName = "Input";  # This may be changed

OutputFileName = "Output";  # This may be changed

Input = open(f"{InputFileName}.txt", "r");

Output = open(f"{OutputFileName}.txt", "w+");

SplitChars = " | "

for Line in Input.readlines():
    for Word in re.split(" |-", Line):
        Output.write(f"{TransformWord(Word)}\n");

Input.close();

Output.close();

print("Done!");