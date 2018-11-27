
import json


class GanjaScene:

    def __init__(self):
        self.internal_list = []

    def add_object(self, mv_array, color=int('AA000000', 16), label=None, static=True):
        if label is not None:
            try:
                assert isinstance(label, str)
                self.internal_list.append(label)
            except:
                raise ValueError('Labels must be strings')
        self.internal_list.append(color)
        self.internal_list.append([i for i in mv_array])

    def add_objects(self, mv_list, color=int('AA000000', 16), label=None, static=True):
        if label is not None:
            try:
                assert isinstance(label, str)
                self.internal_list.append(label)
            except:
                raise ValueError('Labels must be strings')
        self.internal_list.append(color)
        static_list = []
        for mv_array in mv_list:
            if static:
                static_list.append([i for i in mv_array])
            else:
                self.internal_list.append([i for i in mv_array])
        if static:
            self.internal_list.append({'data': static_list})

    def __repr__(self):
        new_str = str.replace(json.dumps(self.internal_list), '''"data": ''', 'data:')
        new_str = str.replace(new_str, ']}', """].map(x=>x.length==32?new Element(x):x)}""")
        return new_str

    def save_to_file(self, filename):
        with open(filename, 'w') as fobj:
            print(self, file=fobj)

