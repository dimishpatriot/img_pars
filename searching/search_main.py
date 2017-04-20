from tools import check_tools


class Search:
    def __init__(self, path):
        self.path = path

    def q_search_text(self):
        print('Write, what you are looking for')
        self.text = input('# ')

    def q_quantity(self, maximum):
        print('How many images do you need (max: {})'.format(maximum))
        while True:
            n_pict = input('# ')

            if not check_tools.is_num(n_pict, max_value=maximum):
                print('Input correct value!')
            else:
                break
        self.quantity = int(n_pict)
