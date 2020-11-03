class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split('\n')

        if students == None:
            self.students = {'Alice': 0, 'Bob': 2, 'Charlie': 4, 'David': 6,
                             'Eve': 8, 'Fred': 10, 'Ginny': 12, 'Harriet': 14,
                             'Ileana': 16, 'Joseph': 18, 'Kincaid': 20, 'Larry': 22}
        else:
            index = 0
            self.students = dict()
            for name in sorted(students):
                self.students[name] = index
                index += 2

        self.seeds = {'V': 'Violets',
                      'G': 'Grass',
                      'R': 'Radishes',
                      'C': 'Clover'}


    def plants(self, student):
        plants_output = list()

        plants_output.append(self.diagram[0][self.students[student]])
        plants_output.append(self.diagram[0][self.students[student] + 1])
        plants_output.append(self.diagram[1][self.students[student]])
        plants_output.append(self.diagram[1][self.students[student] + 1])

        return [self.seeds[p] for p in plants_output]