#def abcListloop():
#    abc=["e","J","O","T","Y"]
#    for letter in abc:
#       print(letter)
#abcListloop()
alphabet_main = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"," W", "X", "Y", "Z"]
alphabet_Greek =["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω"]
numberList=range(0,100)
def abcListloop(alphabet):
    for letter in range(0,len(alphabet),4):
        print(f"number of letters in alphabet: {len(alphabet)}")
        print(alphabet[letter])

abcListloop(alphabet_Greek)