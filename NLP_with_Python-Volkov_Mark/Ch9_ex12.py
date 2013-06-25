#presented by Volkov Mark PRLc 11
# Chapter 9, Ex.12

>>>nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')
% start S
# ###################
# Grammar Productions
# ###################
# S expansion productions
S -> NP VP[TENSE=?t]
# NP expansion productions
NP ->DetN
# VP expansion productions
VP[TENSE=?t] -> IV[TENSE=?t] Det N P N
VP[TENSE=?t] -> IV[TENSE=?t] N P Det N 
# ####### ############
# LexicalProductions
# ###################
Det -> 'The'| 'the'
N -> ' farmer ' | ' cart ' | 'sand' 
IV[TENSE=past] -> 'loaded' | 'filled'
P-> ' into ' | 'with '