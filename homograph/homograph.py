import json
import string
import pathlib

libdir = pathlib.Path(__file__).parent.absolute()
hgdb_file = open(str(libdir) + '/homographs.json', encoding='utf-8')
hgdb = json.load(hgdb_file)
hgdb_file.close

# Checks whether two individual characters are equivalent
def is_char_homoglyphic(letter1, letter2):
  if letter1 == letter2:
    return True

  return letter2 in [entry['char'] for entry in hgdb[letter1]['similar_char']]

def looks_similar(domain1, domain2):
  """
    Determine whether two domains are homographic (visually equivalent or nearly so)
  """
  domain1 = domain1.lower()
  domain2 = domain2.lower()

  if len(domain1) != len(domain2):
    return False

  for letter1, letter2 in zip(domain1, domain2):

    if not is_char_homoglyphic(letter1, letter2):
      return False

  return True

# Get all homoglyphs of a character
def generate_similar_chars(glyph):
  if glyph not in hgdb:
    return ''

  return (homoglyph['char'] for homoglyph in hgdb[glyph]['similar_char'])

# This uses a recursive backtracking algorithm.
# Since Python lacks tail-call optimization
# for recursive calls, a sufficiently long domain
# will cause throw an exception.
# TODO: replace with iterative equivalent.
def generate_similar_strings(domain, homograph=''):
  if len(domain) > 253:
    raise NameError('Domain name cannot exceed 253 characters')

  if domain == '':
    yield homograph
    return

  for glyph in generate_similar_chars(domain[0]):
      yield from generate_similar_strings(domain[1:], homograph + glyph)

  yield from generate_similar_strings(domain[1:], homograph + domain[0])
