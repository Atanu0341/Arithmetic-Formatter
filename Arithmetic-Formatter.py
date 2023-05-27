def arithmetic_arranger(problems , show_answers=False):
    # check numbers in the problem
    if len(problems)>5:
        return "Error: Too many problems"

    arranged_problems=[]
    operators=[]
    answers=[]


    for problem in problems:
            # split problem into components
            operand1, operator, operand2 = problem.split()
    
            # check the operators
            if operator not in ('+','-'):
                return "Error: Operator must be '+' or '-'"
    
            # check whether the operands r digit or not
            if not operand1.isdigit() or not operand2.isdigit():
                return "Error: Numbers must only contain digits" 
            
            # check operand length
            if len(operand1)>4 or len(operand2)>4:
                 return "Error: Numbers cannot be more than four digits"
            
            # determine width for arranging vertically
            width=max(len(operand1)),max(len(operand2)) + 2

            # arrange problem vertically
            arranged_problem=operand1.rjust(width)
            operator_line=operator+operand2.rjust(width-1)
            dash_line='-'*width

            # calculate the answer if show_answers is true
            if show_answers:
                 if operator=='+':
                      answer=str(int(operand1) + int(operand2))
                 else:    
                      answer=str(int(operand1) - int(operand2))
                 answer_line=answer.rjust(width)
                 answers.append(answer_line)

            arranged_problems.extend([arranged_problem, operator_line, dash_line])
    # join the arranged problems, operators, and answers
    arranged_output='   '.join(arranged_problems)
    if show_answers:
         arranged_output += '\n'+'   '.join(answers)

    return arranged_output


        