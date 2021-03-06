# passwordgen.py
#https://www.facebook.com/exploitsec.gov
#Password Generator
#No Dictionary words only scrambled numbers,symbols, and letters
# ~dwulf

import random

print "################################################################################################"
print "# Expl0it																		     		                                           "
print "# Exploit Security                                                                              "
print "# Merry Christmas to all										                              						           "
print "# Remember christmas is not all about presents its about family so forget about those gift. :)  "
print "################################################################################################"
print " "

LOWERCASE_CHARS = tuple(map(chr, xrange(ord('a'), ord('z')+1)))
UPPERCASE_CHARS = tuple(map(chr, xrange(ord('A'), ord('Z')+1)))
DIGITS = tuple(map(str, range(0, 10)))
SPECIALS = ('!','~', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '{', '}', '[', ']', '/', '>', '<', '.', ',', ':', ';', '~EXPL0IT', 'Exploit Security')
            
SEQUENCE = (LOWERCASE_CHARS,
            UPPERCASE_CHARS,
            DIGITS,
            SPECIALS,
            )

def generate_random_password(total, sequences):
    r = _generate_random_number_for_each_sequence(total, len(sequences))

    password = []
    for (population, k) in zip(sequences, r):
        n = 0
        while n < k:
            position = random.randint(0, len(population)-1)
            password += population[position]
            n += 1
    random.shuffle(password)
    
    while _is_repeating(password):
        random.shuffle(password)
        
    return ''.join(password)

def _generate_random_number_for_each_sequence(total, sequence_number):
    """ Generate random sequence with numbers (greater than 0).
        The number of items equals to 'sequence_number' and
        the total number of items equals to 'total'
    """
    current_total = 0
    r = []
    for n in range(sequence_number-1, 0, -1):
        current = random.randint(1, total - current_total - n)
        current_total += current
        r.append(current)
    r.append(total - sum(r))
    random.shuffle(r)

    return r

def _is_repeating(password):
    """ Check if there is any 2 characters repeating consecutively """
    n = 1
    while n < len(password):
        if password[n] == password[n-1]:
            return True
        n += 1
    return False

if __name__ == '__main__':
    print generate_random_password(random.randint(10, 20), SEQUENCE)
