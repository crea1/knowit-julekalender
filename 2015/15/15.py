#!/usr/bin/env python
treasure_map = {
    '11': '34', '12': '21', '13': '32', '14': '41', '15': '25',
    '21': '14', '22': '42', '23': '43', '24': '14', '25': '31',
    '31': '54', '32': '45', '33': '52', '34': '42', '35': '23',
    '41': '33', '42': '15', '43': '51', '44': '31', '45': '35',
    '51': '21', '52': '52', '53': '33', '54': '13', '55': '23'
}


def directions(position):
    map_directions = [position]
    while position != treasure_map[position]:
        position = treasure_map[position]
        map_directions.append(position)
    return map_directions

print(','.join(directions('11')))
