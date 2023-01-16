def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    ans=0
    for i in data:
        if i.isalpha():
            ans+=1
        if i=='\n':
            ans+=1

    xxx=0
    for i in data:
        if i.isdigit():
            xxx+=1


    return [xxx,ans]
f=open('txt_file/data05.txt').read()
# Read data from file
print(main(f))