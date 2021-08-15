# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	lower_strt=97
	upper_start=65
	num_of_alphabets=26
	str=""
	for x in msg:
		if lower_strt<=ord(x) and ord(x)<=lower_strt+num_of_alphabets:
			str+=chr(((ord(x)+shift-lower_strt)%num_of_alphabets)+lower_strt)
		elif upper_start<=ord(x) and ord(x)<=upper_start+num_of_alphabets:
			str+=chr(((ord(x)+shift-upper_start)%num_of_alphabets)+upper_start)
		else:
			str+=x
	
		
			
	return str




