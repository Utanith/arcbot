data = {
  'movie' : {
        'template' : ['{movie}', '{Homage} {Award} "{movie}": {movie}'],
        'movie' : ['{start}: {subtitle}'],

        'protaganist' : ['{Name}', '{Name} and {Name}', '{Formal_title} {Name}'],
        'protag_group_single' : ['The Gang', 'Everyone'],
        'protag_group_plural' : ['The Guys', 'The Girls', 'We'],
        'name' : ['{gen/Username}', 'Alien', 'Andrew', 'arcbot', 'Ben', 'Benji',
            'Celine', 'Chase', 'Chris', 'Elliot', 'Jett', 'Flannery', 'Ian',
            'Jesse', 'Matt', 'Nico', 'Niko', 'Predator', 'Paul Blart', 'Rob',
            'Russell', 'Sarah', 'Jake', 'Stalin', 'Tyler Perry'],
        'famous_person' : ['Don Knotts', 'The Harlem Globetrotters',
            'Carl Sagan', 'Tyler Perry', 'Darth Vader', 'Jar-Jar Binks',
            'Jackie Chan', 'Dendi', 'Brock Samson', 'Hulk Hogan', 'Satan',
            'Steve Buscemi', 'Sean Connery', 'Scott Chadde', 'Nicholas Cage',
            'Dr. Hamdy Soliman', 'Batman', 'Spencer Brown', 'Gaben', 'The Dude',
            'Leonard Nimoy'],
        'creative_person' : ['John Carpenter', 'American McGee', 'Mike Tyson',
            'Crab Nicholson', 'John Madden', 'Tony Hawk', 'Wayne Brady',
            'Joss Whedon', 'H. P. Lovecraft', 'Hideo Kojima', 'George Lucas'],

        'start' : ['{Start} Part {gen/num_either}',
            'The Adventures of {protaganist}', '{protaganist}\'s {subtitle}',
            '{creative_person}\'s {start}',
            '{creative_person} Presents: {start}', '{ominous}'],

        'ominous' : ['{Person} of {Color,Spooky_thing}',
            '{Person} {spooky_status}'],
        'color' : ['red', 'black', 'grey', 'green', 'yellow'],
        'spooky_thing' : ['death', 'doom', 'destruction', 'horror', 'mirrors'],
        'spooky_status' : ['in {Spooky_container}', 'Below', 'Watching',
            'Above', 'Ascending'],
        'spooky_container' : ['{color}', 'the {room}', 'hell'],
        'room' : ['{color} {room}', '{room} of {color,spooky_thing}', 'attic',
            'basement', 'foyer'],
        'person' : ['woman', 'man', 'girl', 'boy', 'king', 'queen', 'god'],

        'subtitle' : ['{sub_premade}', '{Name} vs. {Name}', '{Hype_noun}',
            'The Search for {Item}', '{Title}, Where\'s My {Item}?',
            '{Name} Joins the {Organization}', '{Name} Visits {Place}',
            '{Name} and {Name} Go To {Place}', 'Escape From {Place}', 
            '{Name}\'s Last Stand', 'The Return of {Name}',
            '{Protag_group_single} Meets {Famous_person}',
            '{Protag_group_plural} Meet {Famous_person}', '{Fake_profession}'],
        'sub_premade' : ['Destroy All Monsters', 'The Finale',
            'There and Back Again', 'No Gay Shit'],

        'homage' : ['sequel to', 'remake of', 'prequel to', 'inspired by'],
        'award' : ['critical darling', 'classic', 'last year\'s {award}',
            'cult classic', 'buddy comedy', 'hit of the year', 'award-winning'],

        'title' : ['{informal_title}', '{formal_title}'],
        'informal_title' : ['Dude', 'Doc', 'Bro', 'Broseph'],
        'formal_title' : ['Doctor', 'Rabbi', 'Reverend', 'Officer'],

        'profession_modifier' : ['mall', 'evil', 'master', 'super', 'baby',
            'magic', 'bad', 'disco', 'future'],
        'real_profession' : ['cop', 'doctor', 'rabbi', 'nanny', 'priest',
            'teacher', 'chef', 'grandma', 'santa'],
        'fake_profession' : ['{profession_modifier} {real_profession}'],

        'organization' : ['army', 'navy', 'government', 'Ku Klux Klan', 'Klan',
            'bronies', 'Illuminati', 'Stone Masons', 'Na\'Vi'],
        'place' : ['Washington', 'the Congo', 'Space', 'Russia', 'Prison',
            'Guantanamo Bay', 'West Hall', 'Alta 209', 'White Castle'],
        'item' : ['{item_mod} {item}', 'money', 'dosh', 'pussy', 'dick',
            'robot', 'pot', 'car', 'sex', 'porn', 'booze', 'dildo',
            'fleshlight'],
        'item_mod' : ['more', 'extreme', 'awesome', 'sweet', 'sick'],
        'hype_noun' : ['Excitement', 'Showdown', 'Arena', 'Reckoning',
            'Electric Boogaloo', 'XXX', 'Triple X'],
    },
}
