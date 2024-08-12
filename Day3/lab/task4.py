import sys

def readfileoperation(filepath, option):
    try:
        # Initialize data to None (though it's not actually used here)
        data = None

        # Open the file in read mode
        with open(filepath, 'r') as file:  
            if option == "all":
                return file.read()
            elif isinstance(option, int):
                return file.read(option)
            elif option == "line":
                return file.readline()
            elif option == "lines":
                return file.readlines()
            else :
                return "error"
            
    except Exception:
        return sys.exc_info()
    
    finally:
        file.close()

def writefileoperation(filepath, content):
    try:
        with open(filepath, 'w') as file:
            if isinstance(content, str):
                file.write(content)
            elif isinstance(content, list):
                for item in content:
                    file.write(item)
            else:
                return "Content must be a string or a list of strings."
        return f"Content written to {filepath}."
    except Exception as e:
        return str(e)



def appendfileoperation(filepath, content):
    try:
        with open(filepath, 'a') as file:
            if isinstance(content, str):
                file.write(content)
            elif isinstance(content, list):
                for item in content:
                    file.write(item)
            else:
                return "Content must be a string or a list of strings."
        return f"Content appended to {filepath}."
    except Exception as e:
        return str(e)
