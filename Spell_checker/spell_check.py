from spellchecker import SpellChecker

spell = SpellChecker()

if __name__=="__main__":
    word=input("Enter the paragraph :")
    word=word.split()
    for i in word:
        print(spell.correction(i),end=' ')
