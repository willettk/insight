import numpy as np

N = 10                  # Number of trials to run

n_people = 15           # Number of individual people to schedule
n_groups = 5            # Number of groups per day
n_days = 5              # Number of days with scheduled groups
n_inarow = 3            # Number of days in a row in which two people are grouped to count as success

# Set up the initial schedule
people = range(n_people)
modval = n_people//n_groups
sched = np.mgrid[0:n_days,0:n_people][1,:,:]

def breakline():

    print "----------------------------" 

def print_example(s):
    breakline()
    header = ["Day {:d}\t".format(x+1) for x in range(n_days)]
    print ' '.join(header)
    for idx,row in enumerate(s.T):
        if not idx % modval:
            breakline()
        print "{}\t{}\t{}\t{}\t{}\t".format(*row)
    breakline()

def run_trials(N,verbose=False):

    foundone = 0

    for i in range(N):
    
        # Randomly shuffle the groups in place for each day
        map(np.random.shuffle,sched)
    
        # Set if successful match was found in this trial
        threeinarow = False
    
        # Keep looking through possible pairs until one is found
        keep_looking = True
        while keep_looking:
            for person1 in people:
    
                # Groups for Person #1
                groups_p1 = [list(row).index(person1)//modval for row in sched]
    
                for person2 in people:
                    # Can't compare to oneself
                    if person1 != person2:
                        # Groups for Person #2
                        groups_p2 = [list(row).index(person2)//modval for row in sched]
    
                        # Look over each sliding window of N days for a match
                        for j in range(n_days - n_inarow + 1):
                            sumarr = [x-y for x,y in zip(groups_p1,groups_p2)]
    
                            # Check if conditions match
                            if all(s is 0 for s in sumarr[j:j+n_inarow]):
                                threeinarow = True
    
                                if verbose:
                                    print "\nPersons {} and {} on Days {}-{}".format(person1,person2,j+1,j+n_inarow)
                                    print_example(sched)
    
                                # Found a match; can stop looking in this trial
                                keep_looking = False
    
            # No pairs on consecutive days found in this trial; exit the loop.
            keep_looking = False
    
        # Mark that this trial was successful
        if threeinarow:
            foundone += 1

    return foundone

# Run trials and report result

if __name__ == "__main__":
    successes = run_trials(N,verbose=True)
    print "\n{:.1f}% of the time, two people are in the same group at least three days in a row.\n".format(successes /float(N)*100.)

