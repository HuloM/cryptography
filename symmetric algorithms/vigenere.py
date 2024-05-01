def encrypt(message, key):
    msg_ptr = 0
    key_ptr = 0

    lower_start = ord('a')
    upper_start = ord('A')

    encrypted_msg = ""

    while msg_ptr < len(message):
        if key_ptr >= len(key):
            key_ptr = 0
        if not message[msg_ptr].isspace():
            if message[msg_ptr].islower():
                letter = ord(message[msg_ptr]) - lower_start
                shift = ord(key[key_ptr]) - lower_start

                encrypted_msg += chr((letter + shift) % 26 + lower_start)
            else:
                letter = ord(message[msg_ptr]) - upper_start
                shift = ord(key[key_ptr]) - upper_start

                encrypted_msg += chr((letter + shift) % 26 + upper_start)
        else:
            encrypted_msg += " "
        key_ptr += 1
        msg_ptr += 1

    return encrypted_msg


def decrypt(message, key):
    msg_ptr = 0
    key_ptr = 0

    lower_start = ord('a')
    upper_start = ord('A')

    decrypted_msg = ""

    while msg_ptr < len(message):
        if key_ptr >= len(key):
            key_ptr = 0
        if not message[msg_ptr].isspace():
            if message[msg_ptr].islower():
                letter = ord(message[msg_ptr]) - lower_start
                shift = 26 - (ord(key[key_ptr]) - lower_start)

                decrypted_msg += chr((letter + shift) % 26 + lower_start)
            else:
                letter = ord(message[msg_ptr]) - upper_start
                shift = 26 - (ord(key[key_ptr]) - upper_start)

                decrypted_msg += chr((letter + shift) % 26 + upper_start)
        else:
            decrypted_msg += " "
        key_ptr += 1
        msg_ptr += 1

    return decrypted_msg


def user_input():
    print("please input a key")

    key = input()

    print("please input a message")

    message = input()

    return key, message


def print_messages(message, key):
    encrypted_message = encrypt(message, key)

    print("encrypted text:", encrypted_message)

    print("decrypted text:", decrypt(encrypted_message, key))


def main():
    key, message = user_input()

    while True:
        print_messages(message, key)

        print("would you like to play again? (y/n)")

        choice = input()

        if choice == "y":
            key, message = user_input()
        else:
            exit(1)


if __name__ == "__main__":
    main()
