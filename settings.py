FPS=60 #képfrissítés per másodperc
BG_COLOR=(255,255,255) #háttérszín
DESERT=(220,165,40)
VIOLET=(143,0,255)
RED=(100,30,50)
BG_IMAGE='img/BG.png' #háttérkép

tile_size=64 #csempek szélessége/magassága pixelben

#pálya szerkezete string listában
level_map = [
{'data': [
    '                                                                                                                ',
    '                                                      np                                                        ',
    '    C135EC          T2          C135EC     T2               C135EC          T2          C135EC     T2           ',
    '     noop           np           noop      np                noop           np           noop      np           ',
    '                        np                         np                                                           ',
    '1T          CE1E45TC        1T          CE1E45TC        1T          CE1E45TC        1T          CE1E 5TC        ',
    'np           noooop         np           noooop         np           noooop         np           noooop       np',
    '                                                                                                                ',
    '431 25T    232    2T  322T1C431E25TC   232    2T  32 T  431 25T    232    2T  322T1C431E25TC   232    2P  324T  ',
    'abbbbbc   2abbcT  ac  abbbc abbbbbc   2abbcT  ac  abbbc abbbbbc   2abbcT  ac  abbbc abbbbbc   2abbcT  ac  abbbc ',
    'deeeeef   aheejc  df  deeejcdeeeeef   aheejc  df  deeejcdeeeeef   aheejc  df  deeejcdeeeeef   aheejc  df  deeejc'
]},
{'data': [
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '      T1                        T3                      ',
    '      np            C135EC      np       C 135EC        ',
    '     abbc           abbbc      abbc       abbbc         ',
    '                                                        ',
    '431T25T    232    2T  322T1C431E25TC   232    2P  322T1 ',
    'abbbbbc   2abbcT  ac  abbbc abbbbbc   2abbcT  ac  abbbc ',
    'deeeeef   aheejc  df  deeejcdeeeeef   aheejc  df  deeejc'
]}
]


"""
  terrain: a-p
  cactus: 1
  plant: 2
  rock: 3
  skeleton: 4
  tree: 5
  crate: T
  player: P
  enemy: E
"""

others = { #különböző pályaelemek kódjai
'1': 'cactus',
'2': 'plant',
'3': 'rock',
'4': 'skeleton',
'5': 'tree'
}  

WIDTH=1200 #képernyő szélessége
HEIGHT=len(level_map[0]['data'])*tile_size #pálya magassága (sorok a listában) * a pixel számmal