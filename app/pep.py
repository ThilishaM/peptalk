def pep():
    c1 = ['Champ','Fact:','Everybody says','Dang...','Check it:','Just saying...','Superstar,',
    'Tiger,','Self,','Know this:','News alert:','Girl,','Ace,','Excuse me but','Experts agree',
    'In my opinion,','Hear ye, hear ye:','Listen up,']

    c2 = ['there mere idea of you','your soul','your hair today','everything you do','your personal style',
    'every thought you have','that sparkle in your eye','your presence here','what you got going on',
    'the essential you','your lifes journey','that saucy personality','your DNA','that brain of yours',
    'your choice of attire','the way you roll','whatever your secret is,','all of yall']

    c3 = ['has serious game,','rains magic,','deserves the Nobel Prize,','raises the roof','breeds miracles',
    'is paying off big time,','shows mad skills,','just shimmers,','is a national treasure,','gets the party hopping,',
    'is the next big thing,','roars like a lion,','is a rainbow factory,','is made of diamonds,','makes birds sing,',
    'should be taught in school,','makes my world go round,','is 100 percent legit,']

    c4 = ['24/7','can I get an amen?','and thats a fact','so treat yoself','you feel me?','thats just science',
    'would I lie?','for reals','mic drop.','you hidden gem.','period','now lets dance.','high five.','say it again!','according to CNN',
    'so get used to it']

    from random import randrange
    num1 = randrange(17)
    num2 = randrange(17)
    num3 = randrange(17)
    num4 = randrange(15)

    pep = c1[num1] + " " + c2[num2] + " " + c3[num3] + " " + c4[num4]

    return pep

