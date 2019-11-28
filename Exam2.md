* __HETLAND CHAPTER 3!!!__
* String Formatting
  * methods:
    * upper()
    * lower()
    * center()
    * rjust()
    * strip()
    * rstrip()
    * format()
  * f-string (string interpolation + formatting)
    ```
    f"{var:>20s}"
    f"{var:>5d}"
    f"{var:10.2f}
    ```
    * alignment   < ^ >
    * digits      number
    * precision   .number
    * data type   s d f

* String FINDING
  ```
  if 'ab' in 'Crab':  # true or false
  'Crab'.find('ab')   # returns index of 'ab'
  ```
  * Regular Expressions (RegEx) (CHAPTER 7)
    * What are they, why are they useful?
    * Basic syntax rules, including:
      * The ? matches zero or one of the preceding group.
      * The * matches zero or more of the preceding group.
      * The + matches one or more of the preceding group.
      * The . matches any character, except newline characters.
      * \d, \w, and \s match a digit, word, or space character, respectively.
      * \D, \W, and \S match anything except a digit, word, or space character, respectively.
      * [abc] matches any character between the brackets (such as a, b, or c).
      * (abc|123) parens form a "group" of characters and the | says match either/or (so here you match "abc" OR "123")

* Dictionaries
  * what are they?
  * Dictionary vs. List
  * Dictionary vs. Class
  * key vs value
  * Basic operations:
    * Initialize, e.g.,:
      ```
      empty_dict = {}
      person = {
        "first_name": "Paul",
        "last_name": "York"
      }
      people_list = [
        {
          "first_name": "Paul",
          "last_name": "York"
        },
        {
          "first_name": "Steve",
          "last_name": "Weldon"
        }
      ]
      ```
      * Note that people_list is ACTUALLY a LIST of dictionaries
    * Access a value
    * Add a value
    * Change a value
    * Remove a value
    * Iteratate over a dictionary
      ```
      # LIST
      for idx in range(0, len(lst)):
          val = lst[idx]

      # DICTIONARIES
      for key in dict:
          # can use both key AND value
          print(key)
          val = dict[key]  # Access a value
          print(val)
      ```

* Classes & Objects
  * CONCEPTS & VOCAB
  * HETLAND CHAPTER 7!!!!!!
  * Inheritance, Encapsulation, Polymorphism
  * Class vs. Object (Instance)
  * Functions vs. Methods
    * What is object state?
    * What is "self"

* File I/O
  * Open modes -- r / w / a
  * with / as  (what? why?)
  * Files are opened as "Streams"
    * GENERALLY "one way" (forward-only)
  * "Special" Console I/O Streams
    * stdin is input stream -- READ
    * stdout is output stream -- APPEND

* Command Line Concepts
  * relative vs. abs paths!!!!!!!!
    * / or \ between dirs
    * . and .. "special" dirs
    * / or \ at the beginning moves to "root" and makes it "absolute" path
  * piping `|` -- output of one command as input to another
    ```
    output | input
    dir | grep "2019"   (PIPES `dir` output as input to `grep`)
    ```
  * output redirection `>` or `>>` -- output of a command saved to a file
    ```
    dir > new_file.txt  (OVERWRITES new_file.txt with output of `dir`)
    dir >> a_file.txt   (APPENDS output of `dir` to a_file.txt)
    ```