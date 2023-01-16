def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    ans=0
    for i in data:
        if i.isalpha():
            ans+=1
        if i=='\n':
            ans+=1
    return ans
f=open('txt_file/data02.txt').read()
# Read data from file
print(main(f))