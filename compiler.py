def run_brainfuck(code):
    memory = [0] * 30000  # 30,000 memory cells
    pointer = 0
    code_pointer = 0
    output = ""

    while code_pointer < len(code):
        command = code[code_pointer]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            memory[pointer] += 1
        elif command == '-':
            memory[pointer] -= 1
        elif command == '.':
            output += chr(memory[pointer])
        elif command == ',':
            # Ignore input in this example, as it's not needed for Hello World
            pass
        elif command == '[':
            if memory[pointer] == 0:
                open_brackets = 1
                while open_brackets != 0:
                    code_pointer += 1
                    if code[code_pointer] == '[':
                        open_brackets += 1
                    elif code[code_pointer] == ']':
                        open_brackets -= 1
        elif command == ']':
            if memory[pointer] != 0:
                close_brackets = 1
                while close_brackets != 0:
                    code_pointer -= 1
                    if code[code_pointer] == ']':
                        close_brackets += 1
                    elif code[code_pointer] == '[':
                        close_brackets -= 1

        code_pointer += 1

    return output

bf_code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."


# Run the code and print the result
print(run_brainfuck(bf_code))
