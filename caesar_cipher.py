def caeser_cipher(text,shift,mode):
    result=""
    
    if mode=='decrypt':
        shift=-shift
    for ch in text:
        if ch.isalpha():
            base=ord('A') if ch.isupper() else ord('a')
            shifted=(ord(ch)-base + shift)%26 +base
            result +=chr(shifted)
        else:
            
            result +=ch
            
    return result

def main():
    print("=" * 40)
    print("      CAESAR CIPHER PROGRAM")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("  1. Encrypt")
        print("  2. Decrypt")
        print("  3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == '3':
            print("Goodbye!")
            break
        elif choice not in ['1', '2']:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        mode = 'encrypt' if choice == '1' else 'decrypt'
        message = input("Enter your message: ")
        
        while True:
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    break
                else:
                    print("Please enter a number between 1 and 25.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        output = caeser_cipher(message, shift, mode)
        print(f"\n{'Encrypted' if mode == 'encrypt' else 'Decrypted'} message: {output}")


if __name__ == "__main__":
    main()