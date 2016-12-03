def find_in_dict(buffer, dictionary):
    shift = len(dictionary)
    substring = ""

    for character in buffer:
        substring_tmp = substring + character
        shift_tmp = dictionary.rfind(substring_tmp)

        if shift_tmp < 0:
            break

        substring = substring_tmp
        shift = shift_tmp

    return len(substring), len(dictionary) - shift


def compress(message, buffer_size=4, dictionary_size=12):
    dictionary = ""
    buffer = message[:buffer_size]

    output = []
    while len(buffer) != 0:
        size, shift = find_in_dict(buffer, dictionary)

        dictionary += message[:size + 1]
        dictionary = dictionary[-dictionary_size:]

        message = message[size:]
        last_character = message[:1]
        message = message[1:]

        buffer = message[:buffer_size]
        output.append((shift, size, last_character))
    return output


def decompress(compressed_message):
    message = ""
    for part in compressed_message:
        message = message + message[-part[0]:][:part[1]] + part[2]
    return message
