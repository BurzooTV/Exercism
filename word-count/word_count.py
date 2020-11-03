import re

def count_words(sentence: str):
  word_counter = {}
  sentence = sentence.lower()

  pattern = re.compile("([a-z0-9]+(?:['][a-z]+)?)")

  for w in re.findall(pattern, sentence):
      if w in word_counter:
          word_counter[w] += 1
      else:
          word_counter[w] = 1
          
  return word_counter

