# Variable declarations
a, b, c = 'xyz', 12, 34.5

# Basic print
print(a, b, c)
# Output: xyz 12 34.5

# Labeled variables
print("a=", a, "b=", b, 'c=', c)
# Output: a= xyz b= 12 c= 34.5

# New lines between labels
print("a=", a, "\nb=", b, '\nc=', c)
# Output:
# a= xyz 
# b= 12 
# c= 34.5

# Separator: comma
print(a, b, c, sep=',')
# Output: xyz,12,34.5

# Separator: underscore
print(a, b, c, sep='_')
# Output: xyz_12_34.5

# Separator: tab
print(a, b, c, sep='\t')
# Output: xyz	12	34.5

# Separator: newline
print(a, b, c, sep='\n')
# Output:
# xyz
# 12
# 34.5

# Default newline ending
print(a, b, c)
# Output: xyz 12 34.5

# Custom end: double newline
print(a, b, c, end='\n\n')
# Output:
# xyz 12 34.5
# (extra line)

# Custom end: with @
print(a, b, c, end='@')
# Output: xyz 12 34.5@

# Custom end: with dots
print(a, b, c, end='.....')
# Output: xyz 12 34.5.....

# --- f-string formatting ---
print(f'{a}{b}{c}')
# Output: xyz1234.5

print(f'a={a}b={b}c={c}')
# Output: a=xyzb=12c=34.5

print(f'a={a}\tb={b}\tc={c}')
# Output: a=xyz	b=12	c=34.5

print(f'a={a}\nb={b}\nc={c}')
# Output:
# a=xyz
# b=12
# c=34.5

# --- format() method ---
print('{}{}{}'.format(a, b, c))
# Output: xyz1234.5

print('{}{}{}'.format(b, c, a))
# Output: 1234.5xyz

print('{0}{1}{2}'.format(a, b, c))
# Output: xyz1234.5

print('{0}\t{1}\t{2}'.format(a, b, c))
# Output: xyz	12	34.5

print('{2}\t{0}\t{1}'.format(a, b, c))
# Output: 34.5	xyz	12

# --- % formatting ---
print('%d%f%s' % (b, c, a))
# Output: 1234.500000xyz

print('b=%d c=%f a=%s' % (b, c, a))
# Output: b=12 c=34.500000 a=xyz

print('b=%d c=%.2f a=%s' % (b, c, a))
# Output: b=12 c=34.50 a=xyz
