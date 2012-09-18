import re

EMAIL_REGEX = r'[\S.]+@[\S.]+'

class testEmail:
	def test_email_regex(self):
		assert re.match(EMAIL_REGEX, 'test@mail.ru')
		assert not re.match(EMAIL_REGEX, 'test@where')
