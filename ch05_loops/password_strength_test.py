# DESCRIPTION:  Making a program that tests the strength of passwords and adds suggestions 
# Note: this is kind of messy 


def main():

    print("===== PASSWORD STRENGTH CHECKER =====")
    print("This tool analyzes your password and rates its strength.")
    print(" ")
    password = input("Enter a password to check: ")
    print(" ")


    # ----------------------
    # varibles to track each character list
    uppercase = 0
    lowercase = 0
    digits = 0
    special = 0 

    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"


    # ----------------------
    #   counting score up for total 
    betterstop = 0
    while betterstop < len(password):
        letter = password[betterstop]

        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1
        elif letter.isdigit():
            digits += 1
        elif letter in special_chars:
            special += 1
        
        betterstop += 1


    # ----------------------
    # calculating score board below


    # ----------------------
    # length strength test 
    length = len(password)
    if length >= 12:
        length_score = 25
    elif length >= 8:
        length_score = 15
    elif length >= 6:
        length_score = 10
    else:
        length_score = 0


    # ----------------------
    # charatcer score board
    variety_score = 0
    if uppercase > 0:
        variety_score += 15
    if lowercase > 0:
        variety_score += 15
    if digits > 0:
        variety_score += 15
    if special > 0:
        variety_score += 15


    # ----------------------
    # bonus score 
    type_diversity = 0
    if uppercase > 0:
        type_diversity += 1
    if lowercase > 0:
        type_diversity += 1
    if digits > 0:
        type_diversity += 1
    if special >0:
        type_diversity += 1
        
    bonus_score = 15 if type_diversity >= 3 else 0

    total_score = length_score + variety_score + bonus_score    # note: used microscoft copilot for total_score part needed more organized variables


    # ----------------------
    # printing board for password analysis with variables above 
    print("===== PASSWORD ANALYSIS =====")
    print(f"Length: {length} characters")
    print(f"Uppercase letters: {uppercase}")
    print(f"Lowercase letters: {lowercase}")
    print(f"Digits: {digits}")
    print(f"Special characters: {special}")
    print("")
    print(f"Security Score: {total_score}/100")


    # ----------------------
    # strength test 
    if total_score >= 80:
    #    print(f"Security Score: {total_score}")
        print("Strength Assessment: STRONG")
    elif total_score >= 60:
        print("Strength Assessment: MODERATE")
    elif total_score >= 40:
        print("Strength Assessment: WEAK")
    else:
        print("Strength Assessment: VERY WEAK")
    
    print(" ")


    # ----------------------
    # improvement section 
    print("===== IMPROVEMENT SUGGESTIONS =====")
    if length < 12:
        print("- Use at least 12 characters for better security")
    if uppercase < 1:
        print("- Add uppercase letters (A-Z)")
    if lowercase < 1:
        print("- Add lowercase letters (a-z)")
    if digits < 1:
        print("- Add numbers (0-9)")
    if special < 1:
        print("- Add special characters (!@#$%^&*)")
    if total_score == 100:
        print("- Excellent password! Remember to use different passwords for different accounts.")
        
main()