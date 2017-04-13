def yes_or_no(answer):
    d = ('y', 'Y', 'yes', 'Yes', 'YES')
    yes = False
    if d.count(answer):
        yes = True
    return yes


def is_num(num, min_value=0, max_value=100):
    ans=False
    try:
        if min_value <= int(num) <= max_value:  # Одновременная проверка на диапозон и на int
            ans = True
    except:
        ans = False
    return ans


def link_is_pic(link):
    ext_dict = ('jpg', 'jpeg', 'png', 'gif')
    ext = link.split('.')[-1]

    ans = (ext_dict.count(ext) > 0)

    return ans