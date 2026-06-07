def hex_to_bin(hex_val, bits=64):
    return bin(int(hex_val, 16))[2:].zfill(bits)

def bin_to_hex(bin_val):
    return hex(int(bin_val, 2))[2:].upper().zfill(len(bin_val) // 4)

def permute(input_bits, table):
    return "".join(input_bits[i - 1] for i in table)

def left_circular_shift(bits, n):
    return bits[n:] + bits[:n]

# Tables
IP_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
]

E_TABLE = [
    32,1,2,3,4,5,4,5,6,7,8,9,
    8,9,10,11,12,13,12,13,14,15,16,17,
    16,17,18,19,20,21,20,21,22,23,24,25,
    24,25,26,27,28,29,28,29,30,31,32,1
]

P_BOX = [
    16,7,20,21,29,12,28,17,
    1,15,23,26,5,18,31,10,
    2,8,24,14,32,27,3,9,
    19,13,30,6,22,11,4,25
]

PC1_TABLE = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC2_TABLE = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

S_BOXES = [

# S1
[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
 [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
 [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
 [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],

# S2
[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
 [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
 [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
 [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],

# S3
[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
 [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
 [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
 [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],

# S4
[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
 [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
 [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
 [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],

# S5
[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
 [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
 [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
 [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],

# S6
[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
 [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
 [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
 [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],

# S7
[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
 [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
 [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
 [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],

# S8
[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
 [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
 [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
 [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

]
# INPUT
plaintext = "0123456789ABCDEF"
key = "133457799BBCDFF1"

print("\n INPUT")
print("Plaintext:", plaintext)
print("Key      :", key)

# STEP 1: Initial Permutation
bits = hex_to_bin(plaintext)
ip = permute(bits, IP_TABLE)

print("\n STEP 1: Initial Permutation")
print("IP Output :", bin_to_hex(ip))

lpt = ip[:32]
rpt = ip[32:]

print("L0:", bin_to_hex(lpt))
print("R0:", bin_to_hex(rpt))

# STEP 2: Expansion
expanded_rpt = permute(rpt, E_TABLE)

print("\n STEP 2: Expansion")
print("Expanded R0:", bin_to_hex(expanded_rpt))

# STEP 3: Key Generation
key_bits = hex_to_bin(key)
key56 = permute(key_bits, PC1_TABLE)

print("\n STEP 3: Key Generation")
print("After PC1:", bin_to_hex(key56))

c0 = key56[:28]
d0 = key56[28:]

print("C0:", bin_to_hex(c0))
print("D0:", bin_to_hex(d0))

c1 = left_circular_shift(c0, 1)
d1 = left_circular_shift(d0, 1)

print("C1:", bin_to_hex(c1))
print("D1:", bin_to_hex(d1))

k1 = permute(c1 + d1, PC2_TABLE)
print("K1:", bin_to_hex(k1))

# STEP 4: XOR
xor = bin(int(expanded_rpt, 2) ^ int(k1, 2))[2:].zfill(48)

print("\n⚔ STEP 4: XOR")
print("Expanded R0:", bin_to_hex(expanded_rpt))
print("K1         :", bin_to_hex(k1))
print("XOR Output :", bin_to_hex(xor))

# STEP 5: S-BOX
print("\n STEP 5: S-BOX")

sbox_output = ""
for i in range(8):
    block = xor[i*6:(i+1)*6]
    row = int(block[0] + block[5], 2)
    col = int(block[1:5], 2)
    val = S_BOXES[i][row][col]
    sbox_output += bin(val)[2:].zfill(4)
    print(f"S{i+1} Input:{block} → Output:{bin(val)[2:].zfill(4)}")

print("S-Box Output:", bin_to_hex(sbox_output))

# STEP 6: P-BOX
pbox = permute(sbox_output, P_BOX)

print("\n STEP 6: P-BOX")
print("P-Box Output:", bin_to_hex(pbox))

# STEP 7: FINAL
r1 = bin(int(lpt, 2) ^ int(pbox, 2))[2:].zfill(32)
l1 = rpt

print("\n STEP 7: FINAL ROUND")
print("L1:", bin_to_hex(l1))
print("R1:", bin_to_hex(r1))