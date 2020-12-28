'''
Contains all the classes required for the code
'''

NOTES = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
LENGTH = 13
HEIGHT = 400
WIDTH = 800
STRINGS = 6

def decorate(neck):
    '''
        Decorate the output
    '''
    matrix = []
    for i in neck:
        matrix.append(i.copy())

    #Adding the begining and the ending on the fretboard
    for i in matrix:
        i.insert(1,'|')
        i.append('|')
    
    #Making the length of the neck
    length = len(matrix[0])
    dec_lst = []

    for i in range(length):
        dec_lst.append('=')
    
    #Adding the decoration to the matrix
    matrix.insert(0,dec_lst)
    matrix.append(dec_lst)
    
    return matrix


class String:
    '''
        A string with a starting note
    '''
    def __init__(self,start):
        self.start = start


    
    def string_notes(self):
        '''
            A function that arranges the notes on one string based on the start note
        '''
        t_notes = [' ' for i in range(LENGTH)]
        start_note = ' '

        #Sets the index of the start note
        for note in NOTES:
            if note == self.start:
                start_note = int(NOTES.index(note))

        #Adds the elements after it in an array
        count = 0
        p = start_note
        while count<LENGTH:

            if p > len(NOTES) - 1:
                p=0
            t_notes[count] = NOTES[p]
            p += 1
            count += 1

        return t_notes
    


    def check(self):
        '''
            Checks if its a valid note
        '''
        if self.start.isnumeric() or (self.start not in NOTES):
            print('Error!')
            exit(0)





class Guitar():
    '''
        Class guitar that sketches the entire fretboard
    '''

    def __init__(self, tuning):
        '''
            Initializes the fretboard with the provided tuning
        '''
        self.major_key = [0,2,4,5,7,9,11]
        fret_matrix = []

        for i in tuning:
            string = String(i)
            fret_matrix.append(string.string_notes())
        
        self.fret_matrix = fret_matrix

    def show_all_notes(self):
        '''
            Shows all the notes
        '''
        print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in decorate(self.fret_matrix)]))
        
        
    
    def find_notes(self,key):
        '''
            Finds the notes in a key
        '''
        
        notes_in_key = []
        temp = String(key)
        notes = temp.string_notes()
        minor_indices =[1,2,5]

        for i in self.major_key:
            notes_in_key.append(notes[i])
        del temp
        self.notes_in_key = notes_in_key

        #Making a list of keys with major,minor and diminished
        refined_notes = notes_in_key.copy()
        for i in minor_indices:
            refined_notes[i] += 'm'
        refined_notes[-1] += ' Dim' 


        #Display the key information
        print('NOTES :   ' + '~\t~'.join(notes_in_key))
        print('NUMBERS : ' + '\t'.join([str(i+1) for i in range(len(notes_in_key))]))
        print('CHORDS :  ' + '\t'.join(refined_notes))



    def show_key(self,key_number):
        '''
            Shows the entire fretboard with the key numbers
        '''
        final_fretboard = []
        if key_number == '000':
            for i in self.fret_matrix:
                tstring = []
                for j in i:
                    if j in self.notes_in_key:
                        tstring.append(j)
                    else:
                        tstring.append('-')

                final_fretboard.append(tstring)
        else:
            for i in self.fret_matrix:
                tstring = []
                filtered_notes = []

                for x in key_number:
                    filtered_notes.append(self.notes_in_key[int(x)-1])

                for j in i:
                    if j in filtered_notes:
                        tstring.append(j)
                    else:
                        tstring.append(' ')
                
                tstring.append(1)
                final_fretboard.append(tstring)
        
        if key_number != '0':
            print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in decorate(final_fretboard)]))



    
    


        



    



        
        