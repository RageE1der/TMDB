# imports every thing fom tkinter so I can have the code work like a search engine
from tkinter import *
# imposts the datetime to format them in month day year
import datetime
import json
import urllib.request  # import libraries
import urllib.parse
# starts tkinter
root = Tk()
# using the link from my api to get the id for the move or tv show so i can get more that four items
initialUrl = ("https://api.themoviedb.org/3/search/movie?api_key=69f6da0e5091cf75022dcdf3b06862ee&query=")

# defining ebox so it can be inputs output can be inserted in to the text box
def e_box():
    # for the error handling
    try:
        # assigning a variable for the input
        search_entry = entry_box.get()
        openweatherurl = initialUrl + urllib.parse.quote(search_entry)
        # opens the specified url
        requestURL = urllib.request.urlopen(openweatherurl)

        # read the information from the website and store as a variable
        data = requestURL.read()
        # encodes the data in UTF 8 format
        encoding = requestURL.info().get_content_charset('utf-8')
        # converts the data that is read to a json object
        allthestuff = json.loads(data.decode(encoding))

        # gets the id of the movie or tv show that the movie inputs
        movie_id = str(allthestuff['results'][0]['id'])
        # inserts the id of the movie or tv show to get all the other information
        finalurl1 = ("https://api.themoviedb.org/3/movie/" + (movie_id) + "?api_key=69f6da0e5091cf75022dcdf3b06862ee&language=en-US")
        # opens the specified url
        tmdbUrl = urllib.request.urlopen(finalurl1)
        data = tmdbUrl.read()
        # encodes the data in UTF 8 format
        coding = tmdbUrl.info().get_content_charset('utf-8')
        # converts the data that is read to a json object
        finalurl = json.loads(data.decode(coding))
        # gets the title of the movie or tv show
        originaltitle = finalurl['title']
        # assigns a variable to title of the move or tv show and \n will put any after the title on to a new line
        originaltitle2 = ('Title: ' + (originaltitle) + '\n')
        # gets the average vote of movie and tv show
        vote_average = str(finalurl['vote_average'])
        # assigns a variable to average vote of movie and tv show and \n will put any after the average vote on to a new line
        voteaverage2 = ('Average Vote: ' + (vote_average) + ' out of 10' '\n')
        # gets the release date
        release_date = finalurl['release_date']
        # changes the format of the date from year-month-date to month-date-year
        releasedate3 = datetime.datetime.strptime(release_date, '%Y-%m-%d').strftime("%m-%d-%Y")
        # assigns a variable to release date and \n will put any after the release date on to a new line
        releasedate2 = ('Release Date: ' + (releasedate3) + '\n')

        # gets the description
        overview1 = finalurl['overview']
        # assigns a variable to description and \n will put any after the description on to a new line
        overview2 = ('Description: ' + (overview1) + '\n')

        # gets the genres
        genres1 = finalurl['genres'][0]['name']
        genres4 = finalurl['genres'][1]['name']
        genres3 = finalurl['genres'][2]['name']
        # assigns a variable to genres and \n will put any after the genres on to a new line
        genres2 = ('Genres: ' + (genres1) +', ' + (genres4) +', ' + (genres3) + '\n')

        # gets the runtime
        runtime1 = str(finalurl['runtime'])
        # assigns as variable to runtime and \n will put any after the description on to a new line
        runtime2 = ('Duration: ' + (runtime1) + ' Minutes' '\n')
        # assigns a variable to movie status and \n will put any after the movie status on to a new line
        status = finalurl['status']
        status2 = ('Current Status: ' + (status) + '\n')

        # assigns a variable to every thing and puts every thing on its own line so it doesn't have open braces
        final_insert = ((originaltitle2) + (voteaverage2) + (releasedate2) + (overview2) + (genres2) + (runtime2) + (status2))

        # configures the text box so it can be editable by the output
        textbox.configure(state=NORMAL)
        # deletes the old input so another one can be printed
        textbox.delete(1.0, END)
        # inserts the answers of the input into to the textbox
        textbox.insert(INSERT, final_insert)
        # configures the textbox so it cannot be edited by the user
        textbox.config(state=DISABLED)
    except IndexError :
        # configures the text box so it can be editable by the output
        textbox.configure(state=NORMAL)
        # deletes the old input so another one can be printed
        textbox.delete(1.0, END)
        # inserts the answer of the input into to the textbox
        textbox.insert(INSERT, "There is not movie or tv show that matches your query ")
        # configures the textbox so it cannot be edited by the user
        textbox.config(state=DISABLED)

        # Error handling for pressing the enter button when the text box is empty
    except:
        # configures the text box so it can be editable by the output
        textbox.configure(state=NORMAL)
        # deletes the old input so another one can be printed
        textbox.delete(1.0, END)
        # inserts the answer of the input into to the textbox
        textbox.insert(INSERT, "Please enter something ")
        # configures the textbox so it cannot be edited by the user
        textbox.config(state=DISABLED)

# creates the tkinter box that every thing goes inside
box = Frame(root)
box.pack()

# creates a search box
entry_box = Entry(box, width=50)
# location of the search box
entry_box.pack(side=TOP)

# creates a search button that needs to be pressed for the search
button = Button(box, text='search', command=e_box)
# location of the search button
button.pack(side=TOP)

# inserts a scroll bar that is connected with the text box
y_scroll = Scrollbar(box, orient=VERTICAL)
# location of the scroll bar
y_scroll.pack(side=RIGHT, fill=Y)
# creates a text box 50 wide and 25 high
textbox = Text(box, width=100, height=25, yscrollcommand=y_scroll.set, wrap=WORD,)

# associates the scrollbar to the textbox
y_scroll.config(command=textbox.yview())
# location of the text box
textbox.pack(side=BOTTOM)

# ends tkinter
root.mainloop()