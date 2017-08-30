import csv


class MoonData:
    def __init__(self):
        self.data = {}

    def empty(self):
        self.data = {}

    def import_raw(self, string):
        assert string is not None or ''
        lines = string.split('\n')

        moon_name = ''
        for line in lines:
            if line.startswith('  '):
                ore_info, ore_amount = tuple(line.lstrip().split('    '))
                self.data[moon_name][ore_info] = ore_amount
            else:
                moon_name = line
                self.data[moon_name] = {}

    def import_file(self, filename):
        with open(filename) as f:
            raw = f.read()
            assert raw is not None
            self.import_raw(raw)

    def export_csv(self, filename):
        keys = [
            'moon',
            'Bitumens',  # ubiquitous
            'Coesite',
            'Sylvite',
            'Zeolites',
            'Cobaltite',  # common
            'Euxenite',
            'Scheelite',
            'Titanite',
            'Chromite',  # uncommon
            'Otavite',
            'Sperrylite',
            'Vanadinite',
            'Carnotite',  # rare
            'Cinnabar',
            'Pollucite',
            'Zircon',
            'Loparite',  # exceptional
            'Monozite',
            'Xenotime',
            'Ytterbite'
        ]

        # add normal ores too.
        for _, v in self.data.items():
            for i, _ in v.items():
                if i not in keys:
                    keys.append(i)

        # write info to csv file
        with open(filename, 'w+', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys, extrasaction='ignore')
            writer.writeheader()
            for k, v in self.data.items():
                row = {'moon': k}
                row.update(v)
                writer.writerow(row)


if __name__ == '__main__':
    m = MoonData()
    m.import_file('new 1.txt')
    m.export_csv('data')
