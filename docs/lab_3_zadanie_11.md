
>>> Person.objects.all()
<QuerySet [<Person: Natalia Alak>, <Person: Karolina Kowalska>, <Person: Aleksandra Nowak>, <Person: Jan Wolny>]>

>>> Person.objects.filter(id=3)
<QuerySet [<Person: Jan Wolny>]>

>>> Person.objects.filter(first_name__startswith='N')
<QuerySet [<Person: Natalia Alak>]>

>>> list_team = []
>>> for p in Person.objects.all():
>>>    list_team.append(p.team.name)
    
>>> print(list_team)
['team3', 'team1', 'team2', 'team3']
 
>>> unique_team = list(set(list_team))
 
>>> print(unique_team)
['team2', 'team3', 'team1']

>>> Team.objects.all().order_by('name')
<QuerySet [<Team: Team object (1)>, <Team: Team object (2)>, <Team: Team object (3)>]>

>>> p = Person(first_name='Wojciech', last_name='Sokol', month_of_birth='11')
>>> p.save()
>>> Person.objects.all()
<QuerySet [<Person: Natalia Alak>, <Person: Karolina Kowalska>, <Person: Aleksandra Nowak>, <Person: Wojciech Sokol>, <Person: Jan Wolny>]>
