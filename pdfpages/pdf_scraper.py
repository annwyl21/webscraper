# Portable Document Format invented by Adobe

# https://pypdf2.readthedocs.io/en/3.0.0/user/extract-text.html
from PyPDF2 import PdfReader
import re

reader = PdfReader("CVEllenHoughton.pdf")
#reader = PdfReader("LSE_BP_2022.pdf")
print(len(reader.pages), 'pages')
page = reader.pages[0]
# prints text word by word for CV

# collect word by word output and use splitlines to put all the words into a long_list of words
p = page.extract_text()
#print(p.splitlines())
long_list = p.splitlines()

# use join method to create 1 long string
full_text = ' '.join(long_list)
#print(full_text)

#print(full_text.split('.'))

# Use Regex to extract my email
text = full_text
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Explain regex...
# \b and \b: Word boundaries. Makes sure the email is a separate word and not part of another string.
# [A-Za-z0-9._%+-]+: Matches the user name part of the email, which can contain letters, digits, dots, underscores, percentages, pluses, and hyphens.
# @: The at symbol, a required character in email addresses.
# [A-Za-z0-9.-]+: Matches the domain part of the email, which can contain letters, digits, dots, and hyphens.
# \.: Escapes the dot character.
# [A-Z|a-z]{2,}: Matches the top-level domain part (like com, org, net) which contains at least two alphabetic characters.

my_email_address = re.findall(email_pattern, text)

for match in my_email_address:
	print('My email:', match)



# Use regex to extract any links
urls_pattern = r'\b(?:https?://)?(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+(?:/[^\s]*)?\b'

# Explain regex...
# \b: This is a word boundary. It ensures that what comes after is a distinct word and is not part of another word. It matches the position between a word character and a non-word character.
# (?:https?://)?: This part matches either http or https followed by ://. The s? means the "s" is optional. The entire part is enclosed in a non-capturing group (?: ... ) and followed by a ?, making it optional.
# (?:www\.)?: This part is for the optional "www." that some URLs have. Again, this is a non-capturing group made optional by the ?.
# [a-zA-Z0-9-]+: This part matches the domain name (or subdomain) consisting of one or more alphanumeric characters and hyphens.
# \.: This part matches a literal dot .. It's escaped because a plain . is a special character in regex that matches any character.
# [a-zA-Z0-9-.]+: This part matches the top-level domain like .com, .org, .io, etc. It can also match additional subdomains or domain name parts. The + indicates one or more of the preceding characters are required.
# (?:/[^\s]*)?: This part is optional and would match the rest of the URL after the domain name. It starts with a / and continues with any characters that are not whitespace ([^\s]*).
# \b: This is another word boundary, similar to the one at the beginning. It ensures that what comes before is a distinct word and is not part of another word.

my_links = re.findall(urls_pattern, text)

for match in my_links:
	print('Possible URL located:', match)
	
#Isolating My Skills
skills_tuple = full_text.partition('SKILLS')
list_skills = list(skills_tuple[2].split())
my_skills = []
for skill in list_skills:
	my_skills.append(skill.replace(',', ''))
my_skills = ', '.join(my_skills)
my_skills = my_skills.replace(':,', ':')

print(my_skills)
