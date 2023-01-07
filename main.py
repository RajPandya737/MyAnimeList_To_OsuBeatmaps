from collections import defaultdict
import requests
import webbrowser
import bs4
from selenium import webdriver
import json

# dictionary of all the songs with the anime they are from, may need to expand to a SQL if 
# artist name is needed
anime_songs = [{"Tokyo Ghoul": "Unravel"},
        {"My Hero Academia": "Peace sign "},
        {"Gintama": "I Wanna Be"},
        {"Cowboy Bebop": "Tank!"},
        {"Jojo's Bizarre Adventure": "Bloody Stream"},
        {"Shingeki no Kyojin" : "Guren no Yumiya"},
        {"Fate/Stay Night: Unlimited Blade Works": "Brave Shine"},
        {"Kiseijuu": "Let Me Hear"},
        {"Nanastu no Taizai": "Netsujou no Spectrum"},
        {"Overlord": "Clattanoia "},
        {"Shigatsu wa Kimi no Uso": "Hikaru Nara"},
        {"Guilty Crown": "My Dearest"},
        {"Sword Art Online": "Crossing Field"},
        {"Dragon Ball Z": "Cha La Head Cha La"},
        {"One Piece": "We Are!"},
        {"Haikyuu!!": "Imagination"},
        {"Shokugeki no Souma": "Rising Rainbow"},
        {"No Game No Life": "This Game"},
        {"Kuroku no Basket": "The Other Self"},
        {"Fullmetal Alchemist: Brotherhood": "Rain"},
        {"Durarara!!": "Stepping Out"},
        {"Death Note": "The World"},
        {"Black Clover": "Black Rover"},
        {"Fairy Tale": "Snow Fairy"},
        {"Bleach": "Veloncia"},
        {"Naruto Shippuden": "Sign"},
        {"Rakudai Kishi no Cavalry": "Identity"},
        {"Neon Genesis Evagngelion": "A Cruel Angels Thesis"},
        {"Re:Hamatora": "Sen on Tsubasa"},
        {"Mob Psycho 100": "99"},
        {"Shingeki no Kyojin": "Shinzou wo Sasageyo!"},
        {"Death Parade": "Flyers"},
        {"Hunter X Hunter 2011": "Departure!"},
        {"Noragami Aragoto": "Kyouran Hey Kids!!"},
        {"The Promised Neverland": "Touch Off"},
        {"Bakemonogatari": "Renai Circulation"},
        {"Slam Dunk": "Kimi Ga Suki Da To Sakebitai"},
        {"Angel Beats!": "My Soul, Your Beats!"},
        {"Re:Zero": "Redo  "},
        {"Magi:The Labyrinth of Magic": "V.I.P"},
        {"Fullmetal Alchemist: Brotherhood": "Perio"},
        {"Dragon Ball Super": "Genkai Toppa x Survivor"},
        {"Naruto": "Go!!!"},
        {"Code Geass": "Colours"},
        {"Jojo's Bizarre Adventure": "Jojo~Sono Chi no Sadame~"},
        {"Samurai Champloo": "Battlecry"},
        {"Black Clover": "Black Catcher"},
        {"Blue Exorcist": "Core Pride"},
        {"Yu Yu Hakusho": "Hohoemi no Bakudan"},
        {"Haikyuu!!": "Hikari E"}]

cur = {"Tokyo Ghoul": "Unravel"}

# def get_results_test(search_term):
#     res = requests.get(f'https://www.google.com/search?q={search_term}')
#     res.raise_for_status()
#     soup = bs4.BeautifulSoup(res.text, "html.parser")
#     linkElements = soup.select('.kCrYT > a') 
#     #print(linkElements)
#     linkToOpen = min(3, len(linkElements))
#     to_return = []
#     for i in range(linkToOpen):
#         to_return.append('https://www.google.com'+linkElements[i].get('href'))
#     return to_return    

def login(username, password):
    #https://osu.ppy.sh/session

    url = 'https://osu.ppy.sh/forum/ucp.php?mode=login'

    with requests.session() as session:
        response = session.post(url, auth=(username, password))
        print(response.text)
        with open ('index.html', 'w') as f:
            f.write(response.text)

login('notsus0223', 'OsuWebScrappers')


def get_link(anime_name, song, mode='any'):
    link = 'https://osu.ppy.sh/beatmapsets?g=3'
    if mode == 'osu':
        link += '?m=0'
    elif mode == 'osutaiko':
        link += '?m=1'
    elif mode == 'osu!catch':
        link+= '?m=2'
    elif mode == 'osumania':
        link += '?m=3'
    link+=f'&q={song}'
    return link

def get_results(anime_name, song, mode='any'):
    link = get_link(anime_name, song, mode)
    print(link)
    url = requests.get(link)
    url.raise_for_status()
    soup = bs4.BeautifulSoup(url.text, "html.parser")
    links = soup.find("a", attrs={"class": "navbar-mobile__logo"})

    return links

    # soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # linkElements = soup.select('div#main > div > div > div > a') 
    # linkToOpen = min(3, len(linkElements))
    # sites = []
    # for i in range(linkToOpen):
    #     sites.append('https://www.google.com'+linkElements[i].get('href'))
    # return sites


def get_song(link):
    print(link)
    url = requests.get(link)
    url.raise_for_status()
    soup = bs4.BeautifulSoup(url.text, "html.parser")
    links = soup.find_all("span", attrs={"class": "theme-song-title"})
    print(links)
# get_song('https://myanimelist.net/anime/918')


# print(get_results('Tokyo Ghoul', 'Unravel', 'osu'))