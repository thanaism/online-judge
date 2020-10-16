# import re;print('NYOE S'[bool(re.match('^(eraser?|dream(er)?)*$',input()))::2])
import re;print('YES'if re.match('^(eraser?|dream(er)?)*$',input())else'NO')
# import re;print('YES'if re.fullmatch('(eraser?|dream(er)?)*',input())else'NO')