# Credit to From James Waldby - jwpat7: https://stackoverflow.com/a/16467849
# My intuitions on how to handle looking at all 24 possible rotations without
# changing the handedness of the coordinates was not great, so googled around
# looking for something like the output of this code.
def roll(v): return (v[0],v[2],-v[1])
def turn(v): return (-v[1],v[0],v[2])
def sequence (v):
    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            yield(v)           #    Yield R
            for i in range(3): #    Yield TTT
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v)))  # Do RTR

p = sequence(( 1, 2, 3))
for i in p:
    print(i)