months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
month_30 = ['April', 'June', 'September', 'November']
month_31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']


def is_sentence(sentence):
    # checks if it is a valid sentence 
    m, d, n = 0, 0, 0 # counters for months, dm date and numbers 
    for word in sentence:
        if word in months:
            m += 1
        elif not word.isalpha():
            if dm_date(word):
                d += 1
            elif '.' not in word:
                n += 1
    if (m == 1 and d == 0 and n >= 1) or (m == 0 and d == 1):
        return True
    else:
        return False


def dm_date(date):
    # checks if the dm date is valid 
    if ',' not in date:
        # this condition is neseccary because if you look at line 13, i call this function only if 
        # is.alpha is false, and 45.7 is also not alpha and 45,7 is also not alpha 
        if '.' in date:
            # further making sure that it is in the format of a dm date 
            date = date.replace('.', ' ')
            date = date.strip()
            date = date.split()
            # manipulating the string to make it useable 
            if len(date) == 2:
                # 1.2.3 will also satisfy the above conditions and thus another condition to filter out 
                # the unwanted stuff
                day, month = date
                # now itll check if the date is valid or not 
                return is_valid(day, month)
            else:
                return False
        else:
            return False
    else:
        return False


def is_valid(day, month):
    # checks if the date is valid 
    day = int(day)
    if month.isdigit():
        if int(month) <= 12:
            month = months[int(month) - 1]
        else:
            return False
    if month == 'February':
        if day > 28:
            # print('false becasue feb has 28 days')
            return False
        else:
            return True
    elif month in month_30:
        if day > 30:
            # print('fasle cause 30 day month')
            return False
        else:
            return True
    elif month in month_31:
        if day > 31:
            # print('false cause 31 day month')
            return False
        else:
            return True


def date_type(sentence):
    # gives the type of sentence 
    if len(list(set(months) & set(sentence))) == 0:
        return 'dm'
    else:
        return 'm'


def solver(fpath):
    # main code 
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.readlines()
        content = list(map(str.strip, content))
        content = list(map(lambda s: s.replace(',', ''), content))
        sentences = list(map(str.split, content[1:]))
        if len(sentences[-1]) == 0:
            sentences.pop(-1)
        output = []
        for sentence in sentences:
            # iterating through each sentence 
            re = sentence[-1].replace('.', '')
            if not dm_date(sentence[-1]):
                # sometimes in a sentece the end is like this 31.4. or 456., so i first replace . with a
                # space and store it in a variable and then i check if it is a dm date, if yes then i 
                # replace the end of the sentence with the modified version 
                sentence[-1] = re
            if is_sentence(sentence):
                if date_type(sentence) == 'm':
                    # if the sentece has a month name 
                    nums = [s for s in sentence if s.isdigit()]
                    # stores all the numbers present in the sentence 
                    month = list(set(sentence).intersection(set(months)))
                    # gives you the month name 
                    month = str(month[0])
                    diff = 100000
                    for num in nums:
                        # iterate through the list of dates 
                        if is_valid(num, month):
                            # checking if the date is valid for the given month 
                            if sentence.index(num) - sentence.index(month) < diff:
                                # this part checks the number which closest to the month 
                                date = num
                                diff = abs(sentence.index(num) -
                                           sentence.index(month))
                    if diff != 100000:
                        i = sentences.index(sentence) + 1
                        # getting the sentence number 
                        output.append([str(i)+'.', month, date])
                        # appending the date 
                else:
                    for word in sentence:
                        if dm_date(word):
                            # this is simpler, im just calling function i made earlier after manipulating the 
                            # words a bit 
                            i = sentences.index(sentence) + 1
                            word = word.replace('.', ' ')
                            day, month = word.split()
                            output.append(
                                [str(i)+'.', months[int(month) - 1], day])

    output = list(map(' '.join, output))
    output = '\n'.join(output)
    return output

# just to automate checking 
for i in range(1, 10):
    input_file = '/Users/tejas/Desktop/semester 2/dates data/pub' + \
        '0' + str(i) + '.in'
    my_ans = solver(input_file)
    ouput_file = '/Users/tejas/Desktop/semester 2/dates data/pub' + \
        '0' + str(i) + '.out'
    with open(ouput_file, 'r', encoding='utf-8') as out:
        ans = out.readlines()
        ans = list(map(str.strip, ans))
    print(my_ans == ans)
my_ans = solver('/Users/tejas/Desktop/semester 2/dates data/pub10.in')
with open('/Users/tejas/Desktop/semester 2/dates data/pub10.out', 'r', encoding='utf-8') as f:
    ans = f.readlines()
    ans = list(map(str.strip, ans))
    print(my_ans == ans)
