

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# letter = 'Ю'
# number_test = alphabet.find(letter.lower())
# print(number_test)
# new_nomer = number_test % len(alphabet)
# print(new_nomer)
# print(34%33-1)
# print(alphabet[0])


class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = []
        for letter in text:
            position = self.alphabet.find(letter.lower())
            if position == -1:
                result.append(letter)
                continue
            if is_encrypt:
                new_position = position + shift
                if new_position % len(self.alphabet) >= 0:
                    new_position2 = new_position % len(self.alphabet)
                    result.append(self.alphabet[new_position2])
                else:
                    result.append(self.alphabet[new_position])
            else:
                new_position = position - shift
                if new_position % len(self.alphabet) >= 0:
                    new_position2 = new_position % len(self.alphabet)
                    result.append(self.alphabet[new_position2])
                else:
                    result.append(self.alphabet[new_position])
        return ''.join(result)



# Проверка:
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))

# class CipherMaster:
#     # Не изменяйте и не перемещайте эту переменную
#     alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

#     def cipher(self, original_text, shift):
#         # Метод должен возвращать зашифрованный текст
#         # с учетом переданного смещения shift.
#         result = []
#         for letter in original_text:
#             position = self.alphabet.find(letter.lower())
#             if position == -1:
#                 result.append(letter)
#             else:
#                 letter_number = position + shift
#                 if letter_number % len(self.alphabet) >= 0:
#                     new_position = letter_number % len(self.alphabet)
#                     result.append(self.alphabet[new_position])
#                 else:
#                     result.append(self.alphabet[letter_number])
#         return ''.join(result)

#     def decipher(self, cipher_text, shift):
#         # Метод должен возвращать исходный текст
#         # с учётом переданного смещения shift.
#         result = []
#         for letter in cipher_text:
#             position = self.alphabet.find(letter.lower())
#             if position == -1:
#                 result.append(letter)
#             else:
#                 letter_number = position - shift
#                 if letter_number % len(self.alphabet) >= 0:
#                     new_position = letter_number % len(self.alphabet)
#                     result.append(self.alphabet[new_position])
#                 else:
#                     result.append(self.alphabet[letter_number])
#         return ''.join(result)
