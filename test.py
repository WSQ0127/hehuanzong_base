target_chars = [
        "🤔", "♥", "🤓", "Sci", "wsq", "?", "喵呜", "啾", 
        "哟", "去了",  "好吃",  "咿", "呀", "嗯", "哈",  "哼",
       "咕啾", "唔", "快点", "不行", "爽", "不要", "~", "!"
]
target_len = len(target_chars)


class EncryptDecryptSystem:
    def __init__(self):
        self.char_map = {i: target_chars[i] for i in range(target_len)}
        self.reverse_map = {target_chars[i]: i for i in range(target_len)}

    @classmethod
    def encode(cls, input_string):
        if not input_string:
            return ""

        byte_data = input_string.encode('utf-8')

        num = int.from_bytes(byte_data, 'big')
        encoded_result = []

        if num == 0:
            encoded_result.append(target_chars[0])
        else:
            while num > 0:
                digit = num % target_len
                encoded_result.append(target_chars[digit])
                num //= target_len

        return ''.join(reversed(encoded_result))

    def decode(self, encoded_string):
        if not encoded_string:
            return ""

        num = 0
        skip = 0
        for index, char in enumerate(encoded_string):
            if skip:
                skip -= 1
                continue

            for i in range(index, len(encoded_string)):
                if char in self.reverse_map:
                    break
                char += encoded_string[i + 1]
            skip = len(char) - 1

            if char not in self.reverse_map:
                raise ValueError(f"无效字符：{char}")
            num = num * target_len + self.reverse_map[char]

        byte_len = (num.bit_length() + 7) // 8
        byte_data = num.to_bytes(byte_len, 'big')

        return byte_data.decode('utf-8')


if __name__ == '__main__':
    system = EncryptDecryptSystem()

    _input_string = "不该问的少打听"

    encoded = system.encode(_input_string)
    print(f"Encoded: {encoded}")
    print(f"Length: {len(encoded)}")

    decoded = system.decode(encoded)
    print(f"Decoded: {decoded}")

    assert decoded == _input_string, "解码失败"
    print("测试通过：编码与解码一致。")
