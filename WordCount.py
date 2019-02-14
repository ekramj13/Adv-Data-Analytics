##Word Count

import pandas as pd 
import numpy as np


#insert data using 3 quotation marks to insert multiple lines as one string 
text= '''A CerTaiN kING HaD a bEaUtIFul gaRDEn, ANd IN THe GarDen StooD A trEe 
whICH bORe GoLDeN ApPlEs. THesE aPples WerE alwAyS CoUntEd, aNd abOuT
tHE TiMe WheN tHEY BEgAn tO grow RipE IT wAs foUND THat EVeRY NIgHT ONE
OF THeM Was gOne. thE kiNg bECAMe veRy ANGRy at thiS, aND ORDEred the
GarDEneR TO KEeP WAtch ALL NIgHT uNDER the tREE. tHE gardener sEt hIs
ELdEsT SoN to WATCH; buT ABout TweLve O’clOCK He fELL ASlEEp, And in
the morNIng aNOTheR Of thE aPPLes Was mIssinG. tHEn THE sECONd Son waS
oRdERED to waTch; aNd AT mIDniGhT he tOO FELl ASleEP, aND iN thE mOrNIng
ANoThER AppLE WaS gOne . TheN THe thIrd Son oFfeREd tO KeEp wATCh; buT
thE garDENer At First WoULd NoT LET Him, FOr fEaR sOMe HArM ShOuLD cOME
To hIM: hoWeveR, at lAST hE coNSEnteD, AND tHE YouNg MAN laID HimSELf
uNDER tHE tREe TO wAtch. AS tHE clocK STRuCk tweLvE He Heard A rustlinG  
NoISe IN ThE aIr, And a biRd CAME FlYing ThAt was Of PUre gOLd; AND as 
IT WAs SNApPING At onE oF ThE aPpleS wIth iTS BeaK, tHE GArDEner’S son
jUMpED UP And SHOT AN aRrOw at iT. But THE arrOw DID thE BiRD nO HaRm;
ONlY iT dRoPPEd a GoLDEn FEather FROM iTS tAiL, aND THEN FLEw AwaY.
the gOLdEN FEAthER WAS bRoUght to THe KinG IN THE MOrNING, AnD aLL ThE
cOunCil WAs called TogETHER. EVERYoNE aGREed ThAt it wAS wORth MoRe THAn
aLl The weAltH Of tHE kIngDOm: But THE KiNg sAID, ‘One FeatHeR Is Of NO
use tO me, I MusT HaVE ThE wHOLE BIRD .'''


#remove punctuations and replace with space 
for char in '-:; .,\n':
    text=text.replace(char,' ')
    
#remove ’ from o’clock to make it one word
for char in '’\n':
    text2=text.replace(char,'')
    
#change everything to lowercase
wordlist = text2.lower()
print(wordlist)


#split breaks the large string into different strings
WordList = wordlist.split()
print(WordList)


#count the number of words using len function
num_words = len(WordList)
print("The number of words in the text is: ", num_words)