# string with escape seq
essay = "The \'/slash\' is often incorrectly called a backslash, especially when a Web address is spoken not \\ \"backslash\". \n A slash is used in text to separate alternatives and to separate lines of poetry."

print(essay)#the complete essay is printed

# Escape sequence 
print("\nEscape Sequence:")
print("Horizontal Tab space:", "Hello\tWorld")  # Using hori tab space
print("Carriage Return:","\rC:/Users/Admin/Documents/") #printing path without restirction on the C:
print("New line:", "Hello\nWorld")  # Using new line
print("Backslash:", "Path\\to\\file")  # Using backslash
print("Single quote:", "file\'s path")  # Using single quote
print("Double quote:", "file\"path\"")  # Using double quote

# Indexing
print("\nIndexing:")
print("1.1st character:", essay[0])  #From first character->T
print("2.3rd character:", essay[3]) #-> (space)
print("3.6th character:", essay[6]) #->s
print("4.8th character:", essay[8]) #->a
print("5.9th character:", essay[9]) #->s
print("6.17th character:", essay[17]) #->f
print("7.12th character:", essay[12]) #-> (space)
print("8.16th character:", essay[16]) #->o
print("9.20th character:", essay[20]) #->n

print("10.Last character:", essay[-1])  #From last character->.
print("11.Last 11 character:", essay[-11])#-> (space)
print("12.Last 8 character:", essay[-8])#-> (space)
print("13.Last 5 character:", essay[-5])#->e
print("14.Last 9 character:", essay[-9])#->f
print("15.Last 12th character:", essay[-12])#->s
print("16.Last 10th character:", essay[-10])#->o
print("17.Last 7th character:", essay[-7])#->p


# Slicing 
print("\nSlicing :")
print("18.First 2 characters:", essay[:2])  # Slicing the first 2 characters->Th
print("19.First 5 characters:", essay[:5])  # ->The '
print("20.First 4 characters:", essay[:4])  #->The 
print("21.First 7 characters:", essay[:7])  #->The '/s
print("22.First 9 characters:", essay[:9])  #->The '/sl
print("23.First 3 characters:", essay[:3])  #->The
print("24.First 10 characters:", essay[:10]) #->The '/slas
print("25.First 13 characters:", essay[:13]) #->The '/slash' 
print("26.First 19 characters:", essay[:19]) #->The '/slash' is oft
print("\n")

print("27.Last 2 characters:", essay[-2:])  # Slicing the last 2 characters->y.
print("28.Last 4 characters:", essay[-4:])  #->try
print("29.Last 5 characters:", essay[-5:])  #->etry.
print("30.Last 7 characters:", essay[-7:])  #->poetry.
print("31.Last 10 characters:", essay[-10:])#->of poetry.
print("32.Last 14 characters:", essay[-14:]) #->nes of poetry.
print("33.Last 15 characters:", essay[-15:]) #->ines of poetry.
print("34.Last 18 characters:", essay[-18:]) #->e lines of poetry.
print("\n")

print("35.Characters from index 2 to 4:", essay[2:4])  # Slicing from index 2 to 4 -> e 
print("36.Characters from index 1 to 10:", essay[1:10]) #->he '/slas
print("37.Characters from index 3 to 13:", essay[3:13])#-> '/slash'
print("38.Characters from index 4 to 15:", essay[4:15])#->'/slash' is
print("39.Characters from index 1 to 5:", essay[1:5])#->he '
print("40.Characters from index 2 to 10:", essay[2:10]) #->e '/slas
print("41.Characters from index 9 to 21:", essay[9:21])#->sh' is often
print("42.Characters from index 20 to 29:", essay[20:29])#->n incorre
print("43.Characters from index 30 to 38:", essay[30:38])#->tly call


# slicing with steps
print("\n Slicing Examples:")
print("44.Extract it every 2 steps",essay[0:10:2])#2 steps form 0 till 10-> Te'sa
print("45.Extract it every 4 steps",essay[2:10:4])#-> es
print("46.Extract it every 3 steps",essay[8:29:3])#-> a'sfnnr
print("47.Extract it every 8 steps",essay[15:31:8])#-> n
print("48.Extract it every 9 steps",essay[9:60:9])#->strlce
print("49.Extract it every 6 steps",essay[11:50:6])#->'fncaas

print("\nSlicing Characters")
print("50.Every 2nd character with 1st letter:", essay[::2])# Slicing every 2nd character->Te'sah sotnicretycle  (2space)akls,epcal hnaWbadesi pknnt\"akls"   ls sue ntx osprt lentvsadt eaaelnso oty
print("51.Every 3rd character with 1st letter:", essay[::3])#->T ss  t crt ld clheeayh W dsisk t ass. ssiudne  pa tnisntsatleopt.
print("52.Every 4th character with 1st letter:", essay[::4])#->T'a onceyl al,pa nWaeipnt"ks ssenxoptlnvateals t
print("53.Every 5th character with 1st letter:", essay[::5])#->T/h nota cssawa esko"s"As  (2space)eoa rvn rl o.
print("54.From 113th character to the end:", essay[113::]) #->since new line\n
 #A slash is used in text to separate alternatives and to separate lines of poetry.
print("55.From 110th character to the end:", essay[110::]) #->". 
 #A slash is used in text to separate alternatives and to separate lines of poetry.
print("56.From 3rd character to the end:", essay[3::]) #->  '/slash' is often incorrectly called a backslash, especially when a Web address is spoken not \ "backslash". 
 #A slash is used in text to separate alternatives and to separate lines of poetry.
