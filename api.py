import random 
import string
import warnings
version = "1.0.0"

class PasswordGenerator:
    def __init__(self, avoid: str = None, fixed_length: bool = True, length: int = 13):
        if not fixed_length and not isinstance(length, range):
            raise ValueError("When password has no fixed length, lenght should be a range object")
        self.to_avoid = avoid
        if fixed_length:
            self.lengths = [length]
        else:
            self.lengths = list(length)
    
    def _get_random(self):
        try:
            return random.SystemRandom()
        except:
            return random


    def _get_chars(self) -> str:
        chars = string.ascii_letters + string.digits
        try:
            chars -= self.to_avoid
        except (ValueError, TypeError) as e:
            if self.to_avoid is not None:
                warnings.warn(
                    "Could not filter {} from password, Unknown type".format(self.to_avoid), 
                    UserWarning)
        return chars


    def _get_length(self, ran = random):
        return ran.choice(self.lengths) 


    def _generate(self):
        r = self._get_random()
        length = self._get_length(r)
        chars = self._get_chars()
        result = ""
        for i in range(length):
            result += r.choice(chars)
        return result
        

    def generate(self, count: int):
        for i in range(count):
            yield self._generate()


    def generate_one(self):
        return self._generate()
    
    def generate_one2(self):
        r = self._get_random()
        length = self._get_length(r)
        chars = self._get_chars()
        for i in range(length):
            yield r.choice(chars)
