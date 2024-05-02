import random


def encrypt_decrypt(msg, key):
    altered_msg = ""

    for i in range(0, len(msg)):
        altered_chr = ord(msg[i]) ^ key[i]
        altered_msg += chr(altered_chr)
    return altered_msg


def key_generation(seed, msg_len):
    random.seed(seed)
    key = []
    for i in range(msg_len):
        key.append(random.randint(0, 255))
    return key


def user_input():
    print('please input a message')

    message = input()

    print('please input a number for the seed')

    seed = int(input())

    return seed, message


def print_messages(seed, message):
    key = key_generation(seed, len(message))

    encrypted = encrypt_decrypt(message, key)
    print(encrypted)
    decrypted = encrypt_decrypt(encrypted, key)
    print(decrypted)
    print(key)


def main():
    seed, message = user_input()

    while True:
        print_messages(seed,message)

        print("would you like to try again (y/n)")

        choice = input()

        if choice == 'y':
            seed, message = user_input()
        else:
            exit(1)


if __name__ == '__main__':
    main()
