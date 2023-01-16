def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    for i in data:
        if i.isdigit():

         list.append(i)
    return list
f=open('txt_file/data03.txt').read()
print(main(f))
# Read data from file