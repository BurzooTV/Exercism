def distance(strand_a, strand_b):
    diffrent = 0
    
    if not strand_a and not strand_b:
        return 0
    if not strand_a:
        raise ValueError("The strand_a cannot be empty!")
    if not strand_b:
        raise ValueError("The strand_b cannot be empty!")
    if len(strand_a) != len(strand_b):
        raise ValueError("The strands must be equal!")

    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            diffrent += 1

    return diffrent 
