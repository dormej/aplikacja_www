>>> from app.models import Person
>>> from app.serializers import PersonModelSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser

>>> person = Person(first_name='Adam', last_name='Kozak', month_of_birth=1)
>>> person.save()
>>> serializer = PersonModelSerializer(person)
>>> serializer.data
{'id': 6, 'first_name': 'Adam', 'last_name': 'Kozak', 'month_of_birth': 1, 'team': None}

>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"id":6,"first_name":"Adam","last_name":"Kozak","month_of_birth":1,"team":null}'

>>> import io
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> deserializer = PersonModelSerializer(data=data)
>>> deserializer.is_valid()
True

>>> from app.serializers import TeamSerializer
>>> team_serializer = TeamSerializer(team)
>>> team_serializer.data
{'id': 4, 'name': 'team4', 'country': 'UK'}

>>> team_content = JSONRenderer().render(team_serializer.data)
>>> team_content
b'{"id":4,"name":"team4","country":"UK"}'

>>> import io
>>> team_stream = io.BytesIO(team_content)
>>> team_data = JSONParser().parse(team_stream)
>>> deserializer = TeamSerializer(data=team_data)
>>> deserializer.is_valid()
True
> 