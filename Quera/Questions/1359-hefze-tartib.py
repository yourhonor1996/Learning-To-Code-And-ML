''' حفظ ترتیب

فرض کنید به شما دو دنباله داده شده است و شما مسئول آن هستید که ببینید آیا ترتیب کاراکترها در دنباله دوم، همان ترتیب در دنباله اول است یا خیر؟ کافیست از راست یا از چپ ترتیب حفظ شود.

مثلاً اگر دنباله اول abcdefghi و دنباله دوم bfhi باشد، ترتیب از چپ به راست در اولی حفظ شده است. مثالی دیگر که ترتیب را از راست به چپ حفظ کند، دنباله اول abcdefghi و دنباله دوم gfdb است که ترتیب آمدن اعضای دنباله دوم در اولی از راست به چپ است و ترتیب را حفظ کرده است.

مثالی بزنیم که ترتیب را نه از راست به چپ و نه از چپ به راست، حفظ نکرده باشد. دنباله اولی ‫‪abcdefghi‬‬ و دنباله دومی ‫‪bgic‬‬.

برنامه‌ای بنویسید که با گرفتن دنباله‌ها، مشخص کند آیا ترتیب (چه از راست و چه از چپ) حفظ شده است یا خیر.

توجه: ممکن است در دنباله دوم کاراکتری بیاید که در اولی نیست. روشن است که در این صورت پاسخ منفی است و ترتیب حفظ نشده است.

توجه: ممکن است از هر کاراکتر به هر تعداد موجود باشد. کافی‌ست در یکی از حالات ترتیب حفظ شده باشد تا پاسخ مثبت باشد. برای مثال اگر دنباله اول ‫‪abacdfeag‬‬ و دنباله دوم bca باشد ترتیب حفظ شده است (با در نظر گرفتن آخرین a).

ورودی
در خط اول به شما عدد 1\leq n \leq 101≤n≤10 داده می‌شود که nn بیان‌گر تعداد زوج‌های دنباله‌هاست. سپس به ازای هر زوج دنباله، در یک خط دنباله اول و در خط بعدی دنباله دوم می‌آید.

خروجی
به ازای هر زوج دنباله اگر ترتیب حفظ شده است، YES وگرنه NO را چاپ کنید.

ورودی نمونه
5
abcdefghi
dfge
abcdefghi
hcba
qwer
asdf
qwkedlrfid
kelid
abacdfeag
bca
Copy
خروجی نمونه
NO
YES
NO
YES
YES'''
from copy import deepcopy as dc
data = []
n = int(input())
for i in range(n):
    temp = []
    temp.append(input())
    temp.append(input())
    data.append(temp)
    
# for item in data:
#     ifound = 0
#     lastfound = -1
#     lef_to_right = 2
#     answer = 'Yes'
#     for j, find in enumerate(item[1]):
#         if answer == 'No':
#             break
        
#         for i, found in enumerate(item[0]):
#             if(i == len(item[0])-1 and found != find):
#                 answer = 'No'
#                 break
#             if found == find:
#                 ifound = dc(i)
#                 if j == 1:
#                     if (ifound > lastfound):
#                         lef_to_right = 1
#                     else:
#                         lef_to_right = 0
#                 if (lef_to_right == 1 and ifound < lastfound) or (lef_to_right == 0 and ifound > lastfound):
#                     answer = 'No'
                
#                 lastfound = dc(i)
#                 break
#     print(answer)
    
for idata in data:
    for letter in idata[1]:
        index = idata[0].find(letter)
        
    
    