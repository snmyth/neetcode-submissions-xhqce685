class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return "^EMPTY_STRING^"
        if not strs:
            return ""
        else:
            encoded_string = 'sanmit'.join(list(map(lambda x: ''.join(reversed(x)),strs)))
            return encoded_string   

    def decode(self, s: str) -> List[str]:
        if s == "^EMPTY_STRING^":
            return [""]
        if not s:
            return []
        else:
            enc = list(s.split("sanmit"))
            decoded_string = list(map(lambda x:''.join(reversed(x)),enc))
            return decoded_string