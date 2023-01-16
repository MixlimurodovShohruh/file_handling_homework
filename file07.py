def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    ans=0
    for i in data:
        if i.isdigit():
            ans+=int(i)
    return ans

print(main(open('txt_file/data07.txt').read()))
# Read data from file