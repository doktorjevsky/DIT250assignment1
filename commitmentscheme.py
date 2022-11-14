from hashlib import sha256
import bitarray


"""
Returns the x first entries of an iterable s
"""
def com_trunc(s, x):
    return s[:x]

"""
:param v: the message to be commited
:param k: the key used
:param x: the index at which the hash digest should be truncated

commits v with key k by hashing (v + k) and then truncates the
hash digest at index x

"""
def commit(v, k, x):
    bh = bitarray.bitarray()
    h = sha256((v + k).encode())
    bh.frombytes(h.digest())
    return com_trunc(bh.to01(), x)

"""
help function that returns the binary representation of an int
if padding is set to true, the string will be padded to contain 
16 entries.
"""
def get_bin_string(n, padding=False):
    bs = bin(n)[2:]
    if padding:
        p_len = max(16 - len(bs), 0)
        pad = "".join('0' for _ in range(p_len))
        return pad + bs
    return bs

"""
commits the whole domain for X in range(start, stop + 1)
returns a list of f-strings, containing the results
results are three entries: total commits, total unique commits and X
"""
def conduct_test(start, stop):
    output = []
    for x in range(start, stop + 1):
        commits = []
        for k in range(2**16):
            for v in range(2):
                c = commit(get_bin_string(v), get_bin_string(k, True), x)
                commits.append(c)
        out_string = f'Total commits: {len(commits)}     Total unique commits: {len(set(commits))}     X = {x}'
        output.append(out_string)
    return output


outs = conduct_test(0, 30)

for result in outs:
    print(result)
