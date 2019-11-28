# Retesting from Exam 2

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

# New Stuff

* File management
  * python os, shutil and sys modules (what is what?)
  * Command Line (CMD==Windows and SH==Mac/Linux) vs. Python
    * Get Current Directory
      * CMD: cd, SH: pwd
      * Python: os.getcwd()
    * Change Directory
      * CMD or SH: cd [path]
      * Python: os.chdir()
    * List Directory Contents
      * (current) CMD: dir, SH: ls
      * (other)  CMD: dir [path], SH: ls [path]
      * Python: os.listdir() -- for single directory
                os.walk() -- for whole directory tree
    * Copy Files
      * CMD: copy [file] [newfile], SH: cp [file] [newfile]
      * Python: shutil.copyfile()
    * Copy Whole Directory
      * CMD: xcopy /s [dir] [newdir], SH cp -r [dir] [newdir]
      * Python: shutil.copytree()
    * Move or Rename File
      * (rename) CMD: move [file] [newfile], SH: mv [file] [newfile]
      * (move)  CMD: move [file] [newdir], SH: mv [file] [newdir]
      * Python: shutil.move()
    * Delete File
      * CMD: del [file], SH: rm [file]
      * Python: os.remove()
    * Make Directory
      * CMD or SH: mkdir [newdir]
      * Python: os.mkdir()
    * Delete Directory
      * (if empty) CMD or SH: rmdir [dir]
      * (if full)  CMD: rmdir /s [dir], SH: rm -r [dir]
      * Python: shutil.rmtree()
  * Must KNOW the CMD for cd, pwd, dir, copy, move, del, mkdir
  * Must RECOGNIZE the Python and the rest

* External Modules
  * We learned about five useful external python modules
    * csv
    * openpyxl
    * requests
    * beautifulsoup4
    * json
  * Know what each module is used for
  * When similar, know differences
  * Analyze a scenario and understand the most appropriate module(s) to bring to bear to solve a specific problem

* csv
  * CSV is a common, standardized TEXT file format
  * Used with "tabular" data (rows/columns/cells)
  * Module creates a "wrapper" around a file stream (what is that??)
  * Can read or write
    * Only "forward"
    * Only one row at a time
    * NO "random access" to specific "cells"

* openpyxl
  * Works directly with Excel files (XLSX)
  * Complex, BINARY file format
  * Also used with "tabular" data (rows/columns/cells)
    * BUT adds a TON of other stuff like formulas, formatting, images, etc.
  * openpyxl creates or opens XLSX files
    * "Workbook" contains 1 or more "Worksheet"
    * "Worksheet" contains "Cells"
      * Cells are arranged in "Rows" (numbered) and "Columns" (lettered)
  * Can read or write
    * "Random access": can access any part of a Workbook in any order
    * Access individual cell, cell range, row or column at a time

* requests
  * Use Python to "pretend" to be a web browser
    * Access web pages, images, files, etc. over the web
  * Issues HTTP requests and receives responses
    * Each requests and responses are a "conversation" between a web client and a web server
    * Generally a "GET" request is used to retrieve a resource (web page, file, data, etc) FROM a web server
    * Generally a "POST" request is used to send data TO a web server

* beautifulsoup4 (bs4)
  * Used for "web scraping"
    * Retrieve a standard web page and "parses" it
    * Turns HTML into a "Document Object Model" or "DOM"
  * Most Common "Process":
    1. Use requests module to download a web page:
    `resp = requests.get(URL)`
    2. Get the text of the response...this will be HTML:
    `html = resp.text`
    3. Create a "soup" (DOM) object by passing in the HTML to BeautifulSoup() constructor
    `soup = bs4.BeautifulSoup(html)`
    4. Use the "soup" object to find element(s) you are interested in:
    `elem = soup.select_one('h1')`
    5. Get the text of the element(s)
    `my_var = elem.get_text()`
  * Challenge is to find HTML you are interested in
    * DOM is hierarchical "tree" (parent, children, siblings, etc.)
    * DOM is "walkable" (go up, go down, go sideways)
    * DOM is "searchable" (find element(s) by type/attribute)
    * DOM is "selectable" (find element(s) by CSS Selector)
  * .select() method is nice because it reuses CSS rules YOU SHOULD KNOW
    * EXAMPLE HTML:
      ```
      <div id="my_sample">
        <h3>Dumb List</h3>
        <ul>
          <li class="odd_item">item 1</li>
          <li>item 2</li>
          <li class="odd_item">item 3</li>
        </ul>
      </div>
      ```
    * SELECT EXAMPLES (should know these selectors at a minimum):
      * Element selectors
        * Use JUST the name of the element: div, h3, ul, li, etc.
        * soup.select('h3') finds the `<h3>Dumb List</h3>` header ONLY
        * soup.select('li') finds ALL THREE `<li>` elements
      * Class selectors
        * HTML elements can have class attributes
        * If they do, you can find element(s) with that class
        * Selector will have the class name preceded by a PERIOD ('.')
        * soup.select(".odd_item") finds TWO of the three `<li>` elements...only those with `class="odd_item"`
      * ID selectors
        * HTML elements can have id attributes
        * If they do, you can the ONE element with that id
        * Selector will have the id preceded by a POUND SIGN ('#') ("hashtag" for the hipsters)
        * soup.select("#my_sample") finds the `<div>` element
          * Note that because the div contains everything else, you've effectively found the entire HTML snipped in this example
          * But very useful in "real" challenges
          * Can call select() on the returned object to find "sub" elements, e.g.,: `soup.select("#my_sample").select("h3")`
      * Don't get confused. These select NOTHING from the above example:
        * soup.select(".div")
        * soup.select("my_sample")
        * soup.select_one("#odd_item")
        
* json
  * JSON is "JavaScript Object Notation"
  * Used to store the value (state) of objects in JavaScript
  * Also used EXTENSIVELY to transmit data across the Internet
  * Looks almost EXACTLY like Python dictionary syntax
    * really a combination of list and dictionary syntax
    * the people_list example from above is 100% valid JSON, just without the assignment to the people_list variable:
      ```
      [
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
  * CAN be used to save and load data from local files
  * Most commonly used with Web API to read data
  * API = Application Programming Interface
    * Most JSON is provided over the web
    * Must register with API "provider"
    * Usually just a standard HTTP "get" request that returns JSON
  * json module behaves _almost exactly like lists and/or dictionaries_ in Python
  * Most Common "Process" (web API):
    1. Use requests module to download a JSON file from API:
    `resp = requests.get(URL)`
    2. Parse the response text (JSON):
    `js = json.reads(resp.text)`
    3. Access the data you need using standard dictionary obj[key] syntax:
    `a_name = js[0]["first_name"]`
