#! /usr/bin/env python

import twitter
import random

api = twitter.Api(consumer_key = xxxxxx,
                  consumer_secret = xxxxxx,
                  access_token_key = xxxxxx,
                  access_token_secret = xxxxxx)

name_list = ['Spot the Cat', 'Sarek of Vulcan', 'Picard', 'Data', 'Worf', 'Dr Pulaski', 'Nurse Ogawa', 'Troi', 'Riker', 'Geordi', 'Wesley', 'Dr Crusher', 'Q', 'Tasha Yar', 'Guinan', 'Chief OBrien', 'Reg Barclay', 'Moriarty', 'Alexander', 'Lwaxana Troi']
verb_list = ['upsets', 'awakens', 'explodes', 'irradiates', 'eats', 'talks philosophy with', 'entertains', 'is forced to fight', 'raises the child of', 'finds', 'is caught in a phaser duel with' , 'makes love to', 'starts a war with', 'creates a Holo-sim of', 'gets married to', 'gets stuck in a mind-meld with', 'shares a tender moment with', 'has dreams about']
noun_list = ["the entire ship's crew.", 'a naked Chess match.', 'a chicken sandwich.', 'a poorly-concealed analogy of the Cold War.', 'the human concept of love.', 'God.', 'time-travelling shoe salesmen.', 'xenophobic goat-men.', "Admiral Chakotay's favourite notebook.",  'the slug-people of Rylor IX.', 'an obscene Ferengi fertility statue.', 'a cup of tea.', "a Cardassian captain's dog.", "the ship's replicators.", "this year's science fair.", 'an intelligent gaseous cloud.', 'galactic megastar Raylot Hyperswift.', 'the Warp Drive.', 'a Borg nose-hair trimmer.', 'a horrific transporter accident.', "Boothby's dungarees.", 'their alternate-reality counterparts.', 'a hitchhiker from Risa.']
end_list = ['has been posted to DS9.', "has made the galaxy's Most Wanted list.", 'has turned invisible.', 'wants off this crazy train.', 'is in contract negotiations.', 'cries.', 'is on holiday.', 'is painting.', 'writes a song.', 'goes space-crazy.', 'has mind-melded with a turkey.', 'releases the hounds.', 'is waiting for a phone call.', 'tells an amusing anecdote about fish.', 'finds, then loses, religion.', "can't be mentioned for legal reasons.", 'bets it all on black.', 'hides.', 'gets a haircut.', 'whistles.', 'has lunch.', 'gets revenge.', 'smells.', 'is there.', 'has a rash.', 'learns about trust.', 'eats pie.']

def get_followers():
    """
    Automatically follows all new followers, and sends them a welcome message.
    """
    following = api.GetFriendIDs()
    followers = api.GetFollowerIDs()

    not_following_back = []
    
    for f in followers:
        if f not in following:
                not_following_back.append(f)

    print not_following_back    

    for user_id in not_following_back:
        try:
            api.CreateFriendship(user_id)
            user = api.GetUser(user_id)
            api.PostUpdate('@' + user.GetScreenName() + ' Live long and be assimilated.')
        except Exception as e:
            print("error: %s" % (str(e)))

    
def post_update():
    """
    Posts status message to Twitter.
    """
    try:
        api.PostUpdate(create_status())
    except Exception as e:
        print("error: %s" % (str(e)))
    
def create_status():
    """
    Creates a status message based on random choices from word lists.
    """
    status = ''
    second_name_list = []
    name_index = 0
    name_index = random.randrange(0,len(name_list))
    second_name_list = name_list[:name_index] + name_list[name_index + 1:]
    status = name_list[name_index] + ' ' + random.choice(verb_list) + ' ' +  random.choice(noun_list) + ' ' + random.choice(second_name_list) + ' ' +  random.choice(end_list)
    return status

def start():
    """
    Starts the program.
    """
    post_update()
    get_followers()

start()
