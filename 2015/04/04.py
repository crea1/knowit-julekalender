#!/usr/bin/env python
dna = 'TAACGAGTCTGCCACTAGATAGCCCGCGCTATTAATGGGATGTTCTAGGTCTTCACCTCGACCTATACAAGACGAGAATTCTGGTTCAGCCGGTCCGGGGTCGGGAGTTTGGCTTCATAACACAATTGCAGGCGTCAGAGGCCATACCTTAAACCCATCATACGACCGGTACGAAAATCCATGTCACAGACTAATGATCCCTGCTAAGAGATCGTAGCAACCGTTCTGGATCCAAGCAGCTAATAAGTTAGCAAGCTGGTGTGTTTTTGATATTTGCAGTGGCAAACTGTTGCCTGGGTCGGTCCGATGGTCCTCATCGGACGCTGATGACGGACTTTGCACGGTCGCAAGTCGCTGATAGAAGGTGACTCTCGTGCACGATTTAGACCGGCAGTGCTGCGTGAAGGGGGCTCCCTTATCTGATATGCGCAGACTATTTCGGCGTGGAATGCACATGTTCCCCGACCACTTCAACCCTCATGTTGAGGACTTCCTGCCATAACAACAGGGTAACTTAACTCAGGATGTCTTAAAAAAATAGGCTTCTCATGTGCTCACATTTGGGACCGTATGTGCTAAACGGTGTACTATACGCGGTGGAATTTGGAATGGCAAACTTAACAGCAGGTCTAACCGTAGAAGACGTTACGAGTAAGTGTCAAGTCAGCATTGGCGGATCACGGCGTCGCTATGCCGTCAAGCTCTTTTGCGGATATGATCTAAATCAGATTACGAGCGACGCCTGTTTCTAAAATGACCAATGGTACGCAACACGCTGGTAGGATCTGAGCGAGCAAAGCATAAATAGACCCATCGTGTCGCCTGTAAATTGCAAGAGTACCAAGAACCCCGCAATTACGTTGGGTTCGCTATAGTTGAAAGTTACCGATAAACTACCTTTCGCGACCCGTTTTATAACATAACTAGCATTATTACTCAAGGTGCTCTGATTCCCAGAATACCCAAGAACTAGCGCGTTTTTATTTCTTTGGGGAGGTCTTGTCATGATGTTCATACTTGTCGCCTAGGTTTGCCGACTTGTCCTTCTCTTACACTATTCCGAAATCGCAGTTGCACCACGATCGATGAGCATGGTAGTTACTTAAATATTCAAGAGTCCTGGTCCTCGAAATGGCATATGCTTGCAGGTGCCCCCGATCAGATAGAAGACCGCGGCCGAGGAGGTAGTCCGGTACTGTGCGTTTGGTGCCTTTGACTCTTTACGCACTACTGGACCGGCCTTCGAGGTCTAAGGCTACGTCCTTTAACGCTTTTACTATACAATAGAAGGTGTTCTACACACTGCGTGTCGCTGGATTGGCCTTCGACACGCCTTAGCGGCATGTATCAAGCTATCAGGGAGCCCATTGTGGGCGGTTACTCGTCGTTTGCACAACATCAGACCATTCACTATTAAGCTCATCCCCGAAGAAGGCACCCTACCGTTGTAAGTGCGACTTTGGAACCTCTCGGTAATGCCGGTTGCGGCACTTTCAACGTACATTCCGACCTAGTGCAGAAGAATGGATAGCGAGCTGTTTTTCGAGCTCTACCTAATCGGCTCGAATCTACTCGACGTGTCGAGCGTCCTGTCGCATGGCTCGAAGCGGTATCGAGTCAGTCCCCCAGGGGCGCCGACACGTAGTGAGGTGAAAACATCGACATGTGCTTTTGATGTATATGGCTGAGCTTCAATGCGTGGCTAAAGTGGTCAATCCACTCAGGGCATGGATACTCGGCTCAACATAGTAAATTGTCTCCGCGTCCGATAGGCGGGGGTCAATCCGCCGCACTGGTGGGTCACCCGTGATGCTAGGTCTATAGCAGGGCCCCGACCGTAAACTTCAAGCTTTCCCGGTTGCTGTTGTTTTTTGAGCACAGGGAAACGAGCAGTATTGAATCTGAAGGGGGATAGGCGTTTAATTATTCAGAAGTAGTGCGAAGGGCTCCATATGACACTAGTCGTAGTAAGCACATGCTGGAGGTCTGGACTTCCTTCG'
a = c = g = t = 0

for char in dna:
    a += 1 if char == 'A' else 0
    c += 1 if char == 'C' else 0
    g += 1 if char == 'G' else 0
    t += 1 if char == 'T' else 0

print 'A{0}, C{1}, G{2}, T{3}'.format(a, c, g, t)