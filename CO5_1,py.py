def read_file_list(path):
    list=[]
    with open(path,'r')as file:
        for  line in file:
            list.append(line.strip())
path="python_file.txt"
read_file_list(path)
            
        
