import sys

jpg_end_line = 'FFD9'
png_end_line = b'\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82'

ACTIONS = {
    'WRITE': 'ab',
    'READ': 'rb'
}

def handle_file_msg(file_name, action, cancel=False):
    try:
        if action == ACTIONS['WRITE']:
            msg = input("Insert your message and press enter to confirm. If you want to begin a new paragraph type \\n \n")
            with open(file_name, 'ab') as f:# I keept 'ab' instead of using the action param bc the IDE returns a warning
                f.write(bytes(msg, 'utf-8'))
        elif action == ACTIONS['READ']:
            with open(file_name, 'rb+') as f:
                content = f.read()
                marker = bytes.fromhex("FFD9") if ".jpg" in file_name else png_end_line
                offset = content.index(marker)
                f.seek(offset + len(marker))
                if cancel:
                    f.truncate()
                    print("Content cancelled")
                else:
                    print(f.read())
    except FileNotFoundError as e:
        print("Either wrong file name, or file is not placed into the same directory as main.py\nYou may close this action when you want with 'Ctrl + c'")
        return handle_file_msg(file_name, action)

def handle_user_input():
    r_or_w_or_c = input("Read (r) or Write (w) or Cancel (c)? ")
    if r_or_w_or_c != "r" and r_or_w_or_c != "w" and r_or_w_or_c != "c":
        print("Must type either 'r' or 'w' or 'c'")
        return handle_user_input()
    else:
        return r_or_w_or_c

if __name__ == '__main__':
    file = sys.argv[1]
    read_or_write = handle_user_input()
    if read_or_write == 'r':
        handle_file_msg(file, ACTIONS['READ'])
    elif read_or_write == "w":
        handle_file_msg(file, ACTIONS['WRITE'])
    elif read_or_write == "c":
        handle_file_msg(file, ACTIONS['READ'], cancel=True)
    sys.exit(0)


