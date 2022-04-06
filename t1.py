pioneers="Asimov%Isaac#Shelley%Mary#Gibson%William"
num = pioneers.count("%")
num = num + pioneers.count("#") + 2
print(pioneers[len(pioneers)-num:].lower())

names = pioneers.split('#')
m = names[1]
print(m[-4]+'. '+m[:7])
