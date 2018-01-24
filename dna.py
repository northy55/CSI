rf = open('dna.txt', 'r+')
lines = rf.read()

# dna database
hair = {
    'Black': 'CCAGCAATCGC',
    'Brown': 'GCCAGTGCCG',
    'Blonde': 'TTAGCTATCGC'
}

face = {
    'Square': 'GCCACGG',
    'Round': 'ACCACAA',
    'Oval': 'AGGCCTCA'
}

eye = {
    'Blue': 'TTGTGGTGGC',
    'Green': 'GGGAGGTGGC',
    'Brown': 'AAGTAGTGAC'
}

gender = {
    'Female': 'TGAAGGACCTTC',
    'Male': 'TGCAGGAACTTC'
}

race = {
    'White': 'AAAACCTCA',
    'Black': 'CGACTACAG',
    'Asian': 'CGCGGGCCG'
}

# Dna of the suspect
suspect = {
    'Gender': '',
    'Race': '',
    'Hair color': '',
    'Eye color': '',
    'Face shape': ''
}

# list of suspects
Eva = {
    'Gender': 'Female',
    'Race': 'White',
    'Hair color': 'Blonde',
    'Eye color': 'Blue',
    'Face shape': 'Oval'
}

Larisa = {
    'Gender': 'Female',
    'Race': 'White',
    'Hair color': 'Brown',
    'Eye color': 'Brown',
    'Face shape': 'Oval'
}

Matej = {
    'Gender': 'Male',
    'Race': 'White',
    'Hair color': 'Black',
    'Eye color': 'Blue',
    'Face shape': 'Oval'
}

Miha = {
    'Gender': 'Male',
    'Race': 'White',
    'Hair color': 'Brown',
    'Eye color': 'Green',
    'Face shape': 'Square'
}
# Compare DNA database to Your DNA
if gender['Female'] in lines:
    print('Suspect is Female')
    suspect['Gender'] = 'Female'
elif gender['Male'] in lines:
    print('Suspect is Male')
    suspect['Gender'] = 'Male'

if race['White'] in lines:
    print('Suspect is White')
    suspect['Race'] = 'White'
elif race['Black'] in lines:
    print('Suspect is African American')
    suspect['Race'] = 'Black'
elif race['Asian'] in lines:
    print('Suspect is Asian')
    suspect['Race'] = 'Asian'

if hair['Black'] in lines:
    print('Suspect has Black hair')
    suspect['Hair color'] = 'Black'
elif hair['Brown'] in lines:
    print('Suspect has Brown hair')
    suspect['Hair color'] = 'Brown'
elif hair['Blonde'] in lines:
    print('Suspect has Blond hair')
    suspect['Hair color'] = 'Blonde'

if eye['Blue'] in lines:
    print('Suspect has Blue eyes')
    suspect['Eye color'] = 'Blue'
elif eye['Green'] in lines:
    print('Suspect has Green eyes')
    suspect['Eye color'] = 'Green'
elif eye['Brown'] in lines:
    print('Suspect has Brown eyes')
    suspect['Eye color'] = 'Brown'

if face['Square'] in lines:
    print('Suspect has Square face')
    suspect['Face shape'] = 'Square'
elif face['Round'] in lines:
    print('Suspect has Round face')
    suspect['Face shape'] = 'Round'
elif face['Oval'] in lines:
    print('Suspect has Oval face')
    suspect['Face shape'] = 'Oval'

# compare suspects Characteristics to supsects list
print('\n')
if suspect == Eva:
    print('Eva ate the IceCream')
elif suspect == Larisa:
    print('Larisa ate the IceCream')
elif suspect == Matej:
    print('Matej ate the IceCream')
elif suspect == Miha:
    print('Miha ate the IceCream')
