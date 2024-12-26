import os
import argparse

parser = argparse.ArgumentParser("Word Counter")
parser.add_argument('-p','--path',help='Path of Text File',required=True)
parser.add_argument('-c','--character',help='Count Characters',action='store_true')
parser.add_argument('-l','--line',help='Count Lines',action='store_true')
parser.add_argument('-w','--word',help='Count Words',action='store_true')
parser.add_argument('-m', '--mode', help='Mode of Operation', choices=['bytes', 'lines', 'words'], default='bytes')


args = vars(parser.parse_args())


# Open file path with specified encoding and read the file
with open(args['path'], 'r', encoding='utf-8') as file: 
        
        # Step - 01: return the number of bytes in the file
        if args['character']:
            print(os.stat(args['path']).st_size)

        # Step - 02: return the number of lines in the file
        elif args['line']:
            print(len(file.readlines()))

        # Step - 03: return the number of words in the file
        elif args['word']:
            print(len(file.read().split()))
        
        # Step - 04: return the number of bytes, lines, or words in the file
        elif args['mode'] == 'bytes':
            print(os.stat(args['path']).st_size)
        elif args['mode'] == 'lines':
            print(len(file.readlines()))
        elif args['mode'] == 'words':
            print(len(file.read().split()))
        
        


