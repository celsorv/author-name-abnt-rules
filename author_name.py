
#--------------------------------------
# Author's name according to ABNT rules
#--------------------------------------

def author_name(name):

    EXCEPTIONS = ('filho', 'filha', 'neto', 'neta', 'sobrinho', 'sobrinha', 'junior')
    LOWER_CASE = ("da", "de", "do", "das", "dos")

    # list comprehension    
    name_list = [ x.lower() if x.lower() in LOWER_CASE else x.capitalize() for x in name.split() ]

    if len(name_list) > 2 and name_list[-1].lower() in EXCEPTIONS:
        last_name = name_list[-2] + ' ' + name_list[-1]
        name_list.pop()
    else:
        last_name = name_list[-1]
    
    name_list.pop()
    
    return last_name.upper() + (', ' if len(name_list) else '') + ' '.join(name_list)


# ------------------
# using the function

names = (
        'Augusto',                              # AUGUSTO
        'joãO neto',                            # NETO, João
        'Euzebio sAntos Lima Filho',            # LIMA FILHO, Euzebio Santos
        'Eliberto Henrique de Coimbra',         # COIMBRA, Eliberto Henrique de
        'Menescau soBRInho',                    # SOBRINHO, Menescau
        'Giovana Tavarez fERRaz dAs flores',    # FLORES, Giovana Tavarez Ferraz das
        'Giovana Tavarez Ferraz das Flores',    # FLORES, Giovana Tavarez Ferraz das
        'Gerivaldo Antonio do Alabama'          # ALABAMA, Gerivaldo Antonio do
    )

[print(f'{name.ljust(40, ".")} {author_name(name)}') for name in names]

