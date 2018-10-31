from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import re
import csv
driver = webdriver.Chrome(r'C:\Users\Bird_\Desktop\selenium\chromedriver.exe')
movies_search = ['Halloween (2018)',
 'A Star Is Born (2018)',
 'Venom (2018)',
 'First Man (2018)',
 'The Hate U Give (2018)',
 'Smallfoot (2018)',
 'Night School (2018)',
 'Bad Times at the El Royale (2018)',
 'The Old Man & the Gun (2018)',
 'The House with a Clock in Its Walls (2018)',
 'Free Solo (2018)',
 'The Sisters Brothers (2018)',
 'Colette (2018)',
 'Crazy Rich Asians (2018)',
 'The Nun (2018)',
 'Beautiful Boy (2018)',
 'A Simple Favor (2018)',
 'Mid90s (2018)',
 'The Oath (2018)',
 'Incredibles 2 (2018)',
 'Can You Ever Forgive Me? (2018)',
 'The Meg (2018)',
 'Hotel Transylvania 3: Summer Vacation (2018)',
 'The Wife (2017)',
 'Peppermint (2018)',
 'The Predator (2018)',
 'Christopher Robin (2018)',
 'The Guilty (2018)',
 'The Happy Prince (2018)',
 'Alpha (2018)',
 'Ant-Man and the Wasp (2018)',
 'Fahrenheit 11/9 (2018)',
 'Slender Man (2018)',
 'White Boy Rick (2018)',
 'Studio 54 (2018)',
 'Mandy (2018)',
 'What They Had (2018)',
 'Unbroken: Path to Redemption (2018)',
 'Monsters and Men (2018)',
 '1945 (2017)',
 'Wings of Desire (1987)',
 'Searching (2018)',
 'Love, Gilda (2018)',
 'Matangi/Maya/M.I.A. (2018)',
 'Juliet, Naked (2018)',
 'Pick of the Litter (2018)',
 'Mad Max: Fury Road (2015)',
 'Wonder Woman (2017)',
 'Logan (2017)',
 'Star Wars: The Force Awakens (2015)',
 'Baby Driver (2017)',
 'Zootopia (2016)',
 'Seven Samurai (1954)',
 'Up (2009)',
 'Lawrence of Arabia (1962)',
 'War for the Planet of the Apes (2017)',
 'Spider-Man: Homecoming (2017)',
 'Captain America: Civil War (2016)',
 'Moana (2016)',
 'Aliens (1986)',
 'The Lego Movie (2014)',
 'WALL·E (2008)',
 'Star Wars: Episode IV - A New Hope (1977)',
 'Kubo and the Two Strings (2016)',
 'Mission: Impossible - Rogue Nation (2015)',
 'The African Queen (1951)',
 'The Avengers (2012)',
 'Star Wars: Episode V - The Empire Strikes Back (1980)',
 'The French Connection (1971)',
 'Hunt for the Wilderpeople (2016)',
 'Iron Man (2008)',
 'All Is Lost (2013)',
 'Assault on Precinct 13 (1976)',
 'No Country for Old Men (2007)',
 'The Lord of the Rings: The Two Towers (2002)',
 'Looper (2012)',
 'The Right Stuff (1983)',
 'The Fugitive (1993)',
 'Crouching Tiger, Hidden Dragon (2000)',
 'Who Framed Roger Rabbit (1988)',
 'One False Move (1992)',
 'Catch Me If You Can (2002)',
 'Sicario (2015)',
 'In the Line of Fire (1993)',
 'Dr. No (1962)',
 'Raiders of the Lost Ark (1981)',
 'X-Men: Days of Future Past (2014)',
 'From Russia with Love (1963)',
 'Apollo 13 (1995)',
 'Superman (1978)',
 'Embrace of the Serpent (2015)',
 'The Lord of the Rings: The Return of the King (2003)',
 'Close Encounters of the Third Kind (1977)',
 'The Curse of the Were-Rabbit (2005)',
 'The Bourne Ultimatum (2007)',
 'Spider-Man 2 (2004)',
 'Hero (2002)',
 'Enter the Dragon (1973)',
 'Drive (2011)',
 'Inside Out (2015)',
 'Snow White and the Seven Dwarfs (1937)',
 'Toy Story 3 (2010)',
 'Toy Story 2 (1999)',
 'Finding Nemo (2003)',
 'Pinocchio (1940)',
 'Finding Dory (2016)',
 'Toy Story (1995)',
 'Shaun the Sheep Movie (2015)',
 'Ratatouille (2007)',
 'Only Yesterday (1991)',
 'How to Train Your Dragon (2010)',
 'The Incredibles (2004)',
 'Yellow Submarine (1968)',
 'Chicken Run (2000)',
 'Beauty and the Beast (2017)',
 'My Life as a Zucchini (2016)',
 '101 Dalmatians (1996)',
 'The Nightmare Before Christmas (1993)',
 'Monsters, Inc. (2001)',
 'The Lego Batman Movie (2017)',
 'The Iron Giant (1999)',
 'Song of the Sea (2014)',
 'Tower (2016)',
 'The Lion King (1994)',
 'Anomalisa (2015)',
 'Your Name. (2016)',
 'Waltz with Bashir (2008)',
 'Persepolis (2007)',
 'The Red Turtle (2016)',
 'The Secret World of Arrietty (2010)',
 'Aladdin (1992)',
 'Ernest & Celestine (2012)',
 'Fantastic Mr. Fox (2009)',
 'Antz (1998)',
 'Frozen (2013)',
 'Ghost in the Shell (2017)',
 'Coraline (2009)',
 'How to Train Your Dragon 2 (2014)',
 'Big Hero 6 (2014)',
 "A Bug's Life (1998)",
 'Arthur Christmas (2011)',
 'Boy and the World (2013)',
 'Ponyo (2008)',
 'Bolt (2008)',
 'Tangled (2010)',
 'The Simpsons Movie (2007)',
 'Shrek (2001)',
 'Shrek 2 (2004)',
 'The Wind Rises (2013)',
 'Frankenweenie (2012)',
 'When Marnie Was There (2014)',
 'The Peanuts Movie (2015)',
 'Kung Fu Panda (2008)',
 'Rango (2011)',
 'Corpse Bride (2005)',
 'Sausage Party (2016)',
 'Mulan (1998)',
 'Lilo & Stitch (2002)',
 "The Emperor's New Groove (2000)",
 'Chico & Rita (2010)',
 'Puss in Boots (2011)',
 'Anastasia (1997)',
 'Brave (2012)',
 'Get Out (2017)',
 'All About Eve (1950)',
 'It Happened One Night (1934)',
 'Modern Times (1936)',
 "Singin' in the Rain (1952)",
 'The Big Sick (2017)',
 "A Hard Day's Night (1964)",
 'The Philadelphia Story (1940)',
 'La La Land (2016)',
 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964)',
 'Cool Hand Luke (1967)',
 'Monty Python and the Holy Grail (1975)',
 'Paterson (2016)',
 'Before Midnight (2013)',
 "It's a Wonderful Life (1946)",
 'La Dolce Vita (1960)',
 'To Be or Not to Be (1942)',
 'Annie Hall (1977)',
 'Love & Friendship (2016)',
 'Mary Poppins (1964)',
 'The Artist (2011)',
 'The Nice Guys (2016)',
 'Paddington (2014)',
 'Spy (2015)',
 'Logan Lucky (2017)',
 'Airplane! (1980)',
 'The Player (1992)',
 'The Princess Bride (1987)',
 'Some Like It Hot (1959)',
 'Big (1988)',
 "Don't Think Twice (2016)",
 'Life of Brian (1979)',
 'Before Sunrise (1995)',
 'Back to the Future (1985)',
 'The Grand Budapest Hotel (2014)',
 'Groundhog Day (1993)',
 'Sideways (2004)',
 'Tangerine (2015)',
 'The Edge of Seventeen (2016)',
 'What We Do in the Shadows (2014)',
 'Bull Durham (1988)',
 'Moonrise Kingdom (2012)',
 'Sense and Sensibility (1995)',
 'Enough Said (2013)',
 'Lost in Translation (2003)',
 'Brazil (1985)',
 'Broadcast News (1987)',
 "The Band's Visit (2007)",
 'The Muppets (2011)',
 'The Wizard of Oz (1939)',
 'Citizen Kane (1941)',
 'The Third Man (1949)',
 'The Cabinet of Dr. Caligari (1920)',
 'Metropolis (1927)',
 'Casablanca (1942)',
 'Psycho (1960)',
 'Nosferatu (1922)',
 'King Kong (2005)',
 'The Adventures of Robin Hood (1938)',
 'North by Northwest (1959)',
 'Sunset Boulevard (1950)',
 'Rear Window (1954)',
 'Touch of Evil (1958)',
 'A Streetcar Named Desire (1951)',
 'Vertigo (1958)',
 "Rosemary's Baby (1968)",
 'Rebecca (1940)',
 'Frankenstein (2011)',
 'On the Waterfront (1954)',
 'The Grapes of Wrath (1940)',
 'Roman Holiday (1953)',
 'The Last Picture Show (1971)',
 'Chinatown (1974)',
 'Rio Bravo (1959)',
 'Sweet Smell of Success (1957)',
 'Invasion of the Body Snatchers (1978)',
 'Moonlight (2016)',
 'Spotlight (2015)',
 'Selma (2014)',
 'The Godfather (1972)',
 'Boyhood (2014)',
 'The Battle of Algiers (1966)',
 'Arrival (2016)',
 '12 Years a Slave (2013)',
 'Argo (2012)',
 'Gravity (2013)',
 'Alien (1979)',
 'Bicycle Thieves (1948)',
 'Taxi Driver (1976)',
 'Manchester by the Sea (2016)',
 'M (1931)',
 'The Treasure of the Sierra Madre (1948)',
 'Hell or High Water (2016)',
 'Army of Shadows (1969)',
 'The Night of the Hunter (1955)',
 'Brooklyn (2015)',
 'The Babadook (2014)',
 'The Conformist (1970)',
 'The Dark Knight (2008)',
 'The Wrestler (2008)',
 'L.A. Confidential (1997)',
 'Sorcerer (1977)',
 'Jaws (1975)',
 'Carol (2015)',
 'Creed (2015)',
 'Harry Potter and the Deathly Hallows: Part 2 (2011)',
 'The Hurt Locker (2008)',
 'The Godfather: Part II (1974)',
 'Whiplash (2014)',
 'Hidden Figures (2016)',
 'Room (2015)',
 'Gone with the Wind (1939)',
 'The Searchers (1956)',
 'Nightcrawler (2014)',
 'Star Trek ',
 'Things to Come (2016)',
 'Her (2013)',
 "Schindler's List (1993)",
 'Double Indemnity (1944)',
 'Let the Right One In (2008)',
 'Once Upon a Time in the West (1968)',
 'Mudbound (2017)',
 'Mr. Turner (2014)',
 'Apocalypse Now (1979)',
 'It Follows (2014)',
 'Night of the Living Dead (1968)',
 'The Witch (2015)',
 "Pan's Labyrinth (2006)",
 'Evil Dead II (1987)',
 'The Birds (1963)',
 'The Silence of the Lambs (1991)',
 'Godzilla (2014)',
 "Don't Look Now (1973)",
 'The Innocents ',
 'The Cabin in the Woods (2012)',
 'A Girl Walks Home Alone at Night (2014)',
 'Drag Me to Hell (2009)',
 'Carrie (1976)',
 'The Evil Dead (1981)',
 'Young Frankenstein (1974)',
 'Re-Animator (1985)',
 'The Loved Ones (2009)',
 'Train to Busan (2016)',
 'Nosferatu the Vampyre (1979)',
 'The Love Witch (2016)',
 'Room 237 (2012)',
 'A Nightmare on Elm Street (1984)',
 'The Host (2013)',
 'The Fly (1986)',
 'Shaun of the Dead (2004)',
 'Zombieland (2009)',
 "Bram Stoker's Dracula (1992)",
 'What Ever Happened to Baby Jane? (1962)',
 'It Comes at Night (2017)',
 'Dawn of the Dead (2004)',
 'The Phantom of the Opera (1925)',
 "Don't Breathe (2016)",
 'We Are Still Here (2015)',
 'The Wicker Man (1973)',
 'The Texas Chain Saw Massacre (1974)',
 'The Blair Witch Project (1999)',
 'The Conjuring (2013)',
 'The Exorcist (1973)',
 'The Dead Zone (1983)',
 'Let Me In (2010)',
 '28 Days Later... (2002)',
 'Misery (1990)',
 'The Shining (1980)',
 'Cronos (1993)',
 'Bone Tomahawk (2015)',
 'The Orphanage (2007)',
 "The Devil's Candy (2015)",
 "Gerald's Game (2017)",
 'Chronicle (2012)',
 'An American Werewolf in London (1981)',
 'Near Dark (1987)',
 'Poltergeist (1982)',
 'Henry: Portrait of a Serial Killer (1986)',
 'The Descent (2005)',
 'The Omen (1976)',
 'Ginger Snaps (2000)',
 'Slither (2006)',
 'The Autopsy of Jane Doe (2016)',
 'A Field in England (2013)',
 'Backcountry (2014)',
 'Altered States (1980)',
 'Goodnight Mommy (2014)',
 'The House of the Devil (2009)',
 'Spring (2014)',
 'Gremlins (1984)',
 'Paranormal Activity (2007)',
 'The Thing (1982)',
 'We Are What We Are (2013)',
 'They Live (1988)',
 'Beetlejuice (1988)',
 'The Conjuring 2 (2016)',
 'Dressed to Kill (1980)',
 'The Others (2001)',
 'I Am Not Your Negro (2016)',
 'Man on Wire (2008)',
 'Life Itself (2018)',
 '20 Feet from Stardom (2013)',
 'The Last Waltz (1978)',
 'Judging Amy ',
 'Taxi to the Dark Side (2007)',
 'The Cat in the Hat (2003)',
 'Into the Badlands ',
 'The Manchurian Candidate (2004)',
 'Eyes Without a Face (1960)',
 'The Conversation (1974)',
 'Goldfinger (1964)',
 'Eye in the Sky (2015)',
 'Casino Royale (2006)',
 'Blood Simple. (1984)',
 'Bridge of Spies (2015)',
 'The Road Warrior (1981)',
 'Burlesque (2010)',
 'Jurassic Park (1993)',
 'Elevator to the Gallows (1958)',
 'Ex Machina (2014)',
 'Three Colors: Blue (1993)',
 'In the Heat of the Night ',
 'Blue Ruin (2013)',
 'Blue Velvet (1986)',
 'To Catch a Thief (1955)',
 'The Imitation Game (2014)',
 'Gone Girl (2014)',
 'Wild Tales (2014)',
 '10 Cloverfield Lane (2016)',
 'Children of Men (2006)',
 'The Crying Game (1992)',
 'The Dark Knight Rises (2012)',
 'The Umbrellas of Cherbourg (1964)',
 'Sing Street (2016)',
 'Once (2007)',
 'Anvil: The Story of Anvil (2008)',
 'West Side Story (1961)',
 'Waste Land (2010)',
 'Amadeus (1984)',
 'Afghan Star (2009)',
 'Hairspray (2007)',
 'Sound City (2013)',
 'We Are the Best! (2013)',
 'Everyday Sunshine: The Story of Fishbone (2010)',
 'My Fair Lady (1964)',
 'Bill Cunningham: New York (2010)',
 'Beware of Mr. Baker (2012)',
 "Keep on Keepin' On (2014)",
 'Wordplay (2006)',
 'Muscle Shoals (2013)',
 'The Full Monty (1997)',
 'Marley (2012)',
 'Searching for Sugar Man (2012)',
 'The Beaches of Agnès (2008)',
 'Exit Through the Gift Shop (2010)',
 '20,000 Days on Earth (2014)',
 'Nashville ',
 'Crumb (1994)',
 'Marina Abramovic: The Artist Is Present (2012)',
 'Los Angeles Plays Itself (2003)',
 '49 Up (2005)',
 'Straight Outta Compton (2015)',
 'Lagaan: Once Upon a Time in India (2001)',
 'Hedwig and the Angry Inch (2001)',
 'Crazy Heart (2009)',
 'My Kid Could Paint That (2007)',
 'End of the Century (2003)',
 "Dave Chappelle's Block Party (2005)",
 'The Sapphires (2012)',
 'U2 3D (2007)',
 'A Band Called Death (2012)',
 'Florence Foster Jenkins (2016)',
 'The Sound of Music (1965)',
 'Scratch (2001)',
 'Shine (1996)',
 'Caesar Must Die (2012)',
 'Sid and Nancy (1986)',
 'Five Easy Pieces (1970)',
 'Buena Vista Social Club (1999)']
#Create CSV file
csv_file = open('IMDBbudget.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_file)
#create new dict
news_dict = {}
#create column for dictionary
news_dict['title'] = 'title'
news_dict['budget'] = 'budget'
news_dict['grossUSA'] = 'grossUSA'
news_dict['realgrossUSA'] = 'realgrossUSA'
writer.writerow(news_dict.values())
#write the row and add the columnname to the csv file
#movies_title = []
#movies_budget = []
for movies in movies_search:
    #Dumb everything and Start the new dictionary
    news_dict = {}
    #go to imdb.com
    driver.get("https://www.imdb.com/")
    #select filter only title
    selectTitle = driver.find_element_by_xpath('//*[@id="nb_search"]/div[1]/select/option[2]').click()
    #find the search box
    search_box = driver.find_element_by_id("navbar-query")
    #search the name based on the list above
    search_box.send_keys(movies)
    #submit the key
    submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
    #click submit button
    submit_button.click()
    #click the movie filter on the search result page
    #**TRY TO SELECT THE FIRST RESULT
    selectfirst = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a')
    selectfirst.click()
    try:
        title = driver.find_element_by_xpath('//div[@class = "title_block"]/div/div[2]/div[2]/h1').text
        print(title)
    except:
        print("NA")
        continue
    try:
        budget = driver.find_element_by_xpath('//div[@id = "titleDetails"]/div[7]').text
        print(budget)
    except:
        print("NA")
        pass
    try:
        grossUSA = driver.find_element_by_xpath('//div[@id = "titleDetails"]/div[8]').text
        print(grossUSA)
    except:
        print("NA")
        pass
    try:
        realgrossUSA = driver.find_element_by_xpath('//div[@id = "titleDetails"]/div[9]').text
        print(realgrossUSA)
    except:
        print("NA")
        continue
    news_dict['title'] = title
    news_dict['budget'] = budget
    news_dict['grossUSA'] = grossUSA
    news_dict['realgrossUSA'] = realgrossUSA
    writer.writerow(news_dict.values())
#IMDBbudget = pd.DataFrame(movies_title, movies_budget)
#IMDBbudget.to_csv('experimentbudget.csv')
driver.close()