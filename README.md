
# Author's name according to ABNT rules


## Exploring Python Comprehension Lists.

### Objective:
#### Function that returns the name of the author of a book according to ABNT rules.


```
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
```


<blockquote>
<br>
    Euzebio sAntos Lima Filho      --->> LIMA FILHO, Euzebio Santos<br>
    Gerivaldo Antonio do Alabama   --->> ALABAMA, Gerivaldo Antonio do
<br>
</blockquote>
