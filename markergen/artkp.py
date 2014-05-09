# -*- coding: utf-8 -*-

"""
Generates patterns for the "simple" AR tag scheme from ARToolkitPlus.

See src/core/arBitFieldPattern.cxx in ARToolkitPlus
"""

import numpy as np

# Size of marker images
id_pattern_width = 6
id_pattern_height = 6

# Number of bits for marker ID
id_bits = 9

id_mask = (np.int64(1) << id_bits) - 1
id_max = (np.int64(1) << id_bits) - 1
patt_bits = id_bits * 4

# XOR masks
xor_masks = [np.int64(0x0027),
             np.int64(0x014e),
             np.int64(0x0109),
             np.int64(0x00db)]

pos_mask = [(i * id_bits) for i in range(4)]

# Full mask that is used to XOR raw pattern image
full_mask = np.int64(0)
for i in range(4):
    full_mask |= xor_masks[i] << pos_mask[i]

class SimplePattern:
    def __init__(self, id_number):
        self.shape = (6, 6)
        tmp_pat = np.int64(id_number) & id_mask
        self.pattern = np.int64(0)        
        for i in range(4):
            self.pattern |= tmp_pat << pos_mask[i]
        self.pattern ^= full_mask
    
    def __getitem__(self, position):
        x, y = position
        i = y * 6 + x
        return not ((self.pattern >> (35 - i)) & 1) == 0
    
    def print(self):
        def box_char(x, y):
            return "□" if self[x, y] else "■"
        for i in range(self.shape[1]):
            print(" ".join([box_char(i, j) for j in range(self.shape[0])]))
