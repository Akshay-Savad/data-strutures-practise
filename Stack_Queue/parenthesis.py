def isValid(s: str) -> bool:
        temp = []
        for i in s:
            if i in ['(', '[', '''{''']:
                temp.append(i)
            else:
                if len(temp) <= 0:
                    return False
                t = temp.pop()
                if (i == ")" and t != "(") or (i == "]" and t != "[") or (i == '''}''' and t != '''{'''):
                    return False

        if len(temp) > 0:
            return False
        else:
            return True
        
if __name__ == "__main__":
    isValid("""{}""")