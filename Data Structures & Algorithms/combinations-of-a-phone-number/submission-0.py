class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits)==0:
            return []

        digit_to_alpha = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }

        result = [""]

        for digit in digits:
            new_result = []
            for vals in result:
                for alpha in digit_to_alpha[digit]:
                    new_result.append(vals+alpha)
            result = new_result


        return result
        