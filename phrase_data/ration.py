data = {
    'ration' : {
        'template' : ['You open a {size} {type} and find: {contents}.'],

        'size' : ['small', 'tiny', 'big', 'large', 'medium', 'gigantic'],

        'type' : ['{date} k-ration', 'meal, combat, individual ration',
            '{nationality} c-ration'],

        # because age starts with a vowel and date doesn't
        'date' : ['practically ancient', 'extremely old', 'vintage',
            'well-aged', 'pretty old', 'mostly still edible', 'recentish',
            'brand new', 'nearly expired', 'questionable'],

        'nationality' : ['German', 'Russian', 'Japanese', 'Korean',
            'Norwegian', 'British', 'Italian', 'US', 'Thai',
            'Soviet'],

        'contents' : ['{acc_package}, {meal_package}, {drink}',
            '{acc}, {meal_package}', '{meal_package}, {drink} and {extras}'],

        'coffee' : ['coffee instant {coffee_type}',
            'Taster\'s Choice instant coffee',
            'coffee instant {coffee_type} {coffee_style}', 'instant coffee',
            'Nestlé instant coffee'],
        
        'meal_package' : ['{entree}, {side}, {desert}', '{entree}, {desert}',
           '{entree}', '{substitute_entree}'],

        'coffee_type' : ['type I', 'type II'],

        'coffee_style' : ['style I', 'style II', 'style A'],
        
        'drink' : ['electrolyte {beverage_mix}', '{beverage_mix}', '{tea}'],
        
        'beverage_mix' : ['{flavor} beverage mix', 'beverage mix'],
        
        'flavor' : ['lemon', 'cherry',],

        'tea' : ['tea-flavored drink mix', 'a Nestlé tea bag'],
        
        'acc_package' : ['{acc}, {acc1}, {acc2}, {coffee}'],

        'acc' : ['a spork', 'a spoon', 'a knife'],

        'acc1' : ['a pack of cigarettes', 'chewing gum',
            'a packet of creamer', 'a packet of sugar'],

        'acc2' : ['vitamins', 'toothpaste', 'a toothbrush',
            'water purification tablets', 'toilet paper'],

        'entree' : ['{cans} {entree_meat}',
            '{cans} biscuits', 'a {smell} {entree_meat} bar'],

        'smell' : ['terrible smelling', 'slightly chemical scented', 'rancid'],

        'entree_meat' : ['spaghetti and meatballs', 'bacon', 'cured ham',
            'beef stew', 'liver pâté', 'chicken curry'],
        
        'cans' : ['a can of', 'a {date} can of', 'a rusted-through can of'],

        'side' : ['{cans} peanut butter', '{cans} {fruit}',
            '{cans} {fruit} jelly', 'a {date} jelly bar',
            '{cans} {vegetable}', 'a cheese bar'],

        'fruit' : ['pineapple', 'apple', 'pear', 'lemon', 'lime'],

        'vegetable' : ['corn', 'carrots', 'potatoes', 'cabbage'],

        'desert' : ['a vanilla cream disk', 'a chocolate cream disk',
            'a malted milk-dextrose bar', 'an unnamed hard candy',
            'a roll of Smarties', 'a chocolate bar'],

        'extras' : ['a flameless ration heater', 'a plastic bag',
            'a list of the contents', 'a P-38 can opener'],

        'substitute_entree' : ['3 boullion cubes', 'a compressed food bar',
            'a package of hard candy'],
    },
}
