'''
string formatting
    HETLAND CHAPTER 3 !!!!!!!
    string methods
        upper()
        lower()
        center()
        strip()
        right()
        format()  # HETLAND DAMMIT
        f-string  # string interpolation
            f"{anumber:<10s} {astring:^50s} {avalue:>10.2f}"
            align       < ^ >
            size        number
            precision   .number
            datatype    s f d
string FINDING:
    if 'abc' in "gabcdeeeadf":  # in
    x = 'abc'
    x.find('b') # number
    Regular Expressions
        what and why
        really basic syntax rules
            The ? matches zero or one of the preceding group.
            The * matches zero or more of the preceding group.
            The + matches one or more of the preceding group.
            The . matches any character, except newline characters.
            \d, \w, and \s match a digit, word, or space character, respectively.
            \D, \W, and \S match anything except a digit, word, or space character, respectively.
            [abc] matches any character between the brackets (such as a, b, or c).
Dictionaries
    what are they
    dictionary vs list
    dictionary vs class
    key vs value
    Access an value : Add a value : Change a value : Remove a value
    Iteratate over a dictionary
        # LISTS
        for idx in range(0, len(lst)):
            value = lst[idx]

        # DICTIONARIES
        for key in dict:
            print(key)
            value = dict[key]

Classes
    Vocab (Inheritance, Encapsulation, Polymorphism)
    HETLAND CHAPTER 7 !!!!!!!!!
    Classes vs. Objects
    Functions vs. Methods
        object state / self (what is self)

File i/o:
    open modes      r w a
    with / as
    streams i/o (what are streams / implications)
    relative vs absolute file paths !!!!!!!!
    stdio  -  stdin stdout
    argv
    output redirection     > write   >> append
    for example:     dir > file     or     dir >> file
    piping:   output from one as input to another
    for example:    dir | findstr "stuff"
'''