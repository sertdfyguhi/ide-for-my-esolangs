def ewplrun(text):
    cell = 0
    toprint = ''
    e = False
    for idx, letter in enumerate(text):
        if letter == '>':
            toprint += chr(cell)
        elif letter == '<':
            toprint += (chr(cell) + '\n')
        elif letter == '+':
            cell += 1
        elif letter == '-':
            cell -= 1
        elif letter == '~':
            cell += 10
        elif letter == '=':
            cell -= 10
        elif letter == '/':
            toprint += str(cell)
        elif letter == '\\':
            toprint += (str(cell) + '\n')
        elif letter == '_':
            cell = 0
        else:
            return f"At {idx + 1}, '{text[idx]}': Error."
            e = True
            break
    if not e:
        return toprint

def pltsrun(text):
    stack = []
    toprint = ''
    e = False
    a = False
    for idx, letter in enumerate(text):
        if not a:
            if letter == '?':
                a = True
                stack.append(text[idx + 1])
            elif letter == '%':
                a = True
                stack.insert(0, text[idx + 1])
            elif letter == '&':
                toprint += stack[-1] + '\n'
            elif letter == '$':
                toprint += stack[0] + '\n'
            elif letter == '#':
                toprint += ''.join(stack) + '\n'
            elif letter == '@':
                toprint += ''.join(stack)[::-1] + '\n'
            elif letter == '<':
                del stack[0]
            elif letter == '>':
                del stack[-1]
            else:
                return f"At {idx + 1}, '{text[idx]}': Error."
                e = True
                break
        else:
            a = False
    if not e:
        s = toprint.rsplit('\n', 1)
        return ''.join(s)

def dotterrun(text):
    stack = []
    toprint = ''
    a = False
    l = text.split('_')
    for idx, item in enumerate(l):
        if item.startswith('..............'):
            stack.append(chr(int(item[14:])))
        elif item.startswith('.............'):
            stack.insert(0, chr(int(item[13:])))
        elif item == '............':
            toprint += ''.join(stack)
        elif item == '...........':
            toprint += ''.join(stack)[::-1]
        elif item == '..........':
            toprint += stack[-1]
        elif item == '.........':
            toprint += stack[0]
        elif item == '........':
            del stack[-1]
        elif item == '.......':
            del stack[0]
        else:
            return f"{idx + 1}: error"
            a = True
            break
    if a == False:
        return toprint