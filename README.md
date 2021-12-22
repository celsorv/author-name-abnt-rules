
# Author's name according to ABNT rules


## Exploring Python Comprehension Lists.

### Objective:
#### Function that returns the name of the author of a book according to ABNT rules.


```
def author_name(name):

    _EXCEPTIONS = ('filho', 'filha', 'neto', 'neta', 'sobrinho', 'sobrinha', 'junior')
    _LOWERCASE = ("da", "de", "do", "das", "dos")

    # list comprehension    
    name_list = [ x.lower() if x.lower() in _LOWERCASE else x.capitalize() for x in name.split() ]

    if len(name_list) > 2 and name_list[-1].lower() in _EXCEPTIONS:
        last_name = name_list[-2] + ' ' + name_list[-1]
        name_list.pop()     # remove last_name #2
    else:
        last_name = name_list[-1]
    
    name_list.pop()     # remove last_name 1
    
    return last_name.upper() + (', ' if len(name_list) else '') + ' '.join(name_list)
```


### Example outputs:
```

    Euzebio Santos Lima Filho      # LIMA FILHO, Euzebio Santos
    Gerivaldo Antonio do Alabama   # ALABAMA, Gerivaldo Antonio do

```
