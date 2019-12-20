def sw1(value):
    return {
        'mme': 'Vous etes une femme',
        'mlle': 'Vous est une femme non marie',
        'm.': 'Vous est un homme',
    }[value]


present = sw1(str.lower(input('Civil :')))
print('Bonjour, {}'.format(present))

