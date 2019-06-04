import json
import sys
import os

def beautifier():
    # Handling the file exceptions
    try:
        filename = input('Enter your filename:')
        fhandle = open(filename,'r')
            # Beautifying the json file
        parsed_content = json.loads(fhandle.read())
        try:
            output_filename = input('Please Enter the output filename: ')
            while True:
                if '.json' in output_filename:
                    pass
                else:
                    output_filename += '.json'
                    
                if os.path.isfile(output_filename):
                    print('{} File already exist!'.format(output_filename))
                    output_filename = input('Please Enter the output filename: ')
                else:
                    break

            with open(output_filename,'w') as f:
                f.write(json.dumps(parsed_content, indent=4, sort_keys=False))
        except FileExistsError as e:
            print()
       
    except FileNotFoundError as e:
        print('[-] {} File Not Found.![-]'.format(filename))
    except IOError:
        print("[-] File is not accessible [-]")
    except KeyboardInterrupt as e:
        sys.exit(0)

if __name__ == "__main__":
    beautifier()