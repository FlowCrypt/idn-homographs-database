import json
import string

# The simchar data from ShamFinder could be structured
# waaay more efficiently & less redundantly
hgdb_file = open('homographs.json')
hgdb = json.load(hgdb_file)
hgdb_file.close

# Checks whether two individual characters are equivalent
def homoglyphic(letter1, letter2):
  if letter1 == letter2:
    return True

  return letter2 in [entry['char'] for entry in hgdb[letter1]['similar_char']]

def homographic(domain1, domain2):
  """
    Determine whether two domains are homographic (visually equivalent or nearly so)
  """
  domain1 = domain1.lower()
  domain2 = domain2.lower()

  if len(domain1) != len(domain2):
    return False

  for letter1, letter2 in zip(domain1, domain2):

    if not homoglyphic(letter1, letter2):
      return False

  return True

# Get all homoglyphs of a character
def homoglyphs(glyph):
  if glyph not in hgdb:
    return ''

  return (homoglyph['char'] for homoglyph in hgdb[glyph]['similar_char'])

# This uses a recursive backtracking algorithm.
# Since Python lacks tail-call optimization
# for recursive calls, a sufficiently long domain
# will cause throw an exception.
# TODO: replace with iterative equivalent.
def homographs(domain, homograph=''):
  if len(domain) > 253:
    raise NameError('Domain name cannot exceed 253 characters')

  if domain == '':
    yield homograph
    return

  for glyph in homoglyphs(domain[0]):
      yield from homographs(domain[1:], homograph + glyph)

  yield from homographs(domain[1:], homograph + domain[0])
