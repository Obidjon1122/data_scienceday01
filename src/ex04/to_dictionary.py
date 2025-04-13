list_of_tuples = [
  ('Russia', '25'),
  ('France', '132'),
  ('Germany', '132'),
  ('Spain', '178'),
  ('Italy', '162'),
  ('Portugal', '17'),
  ('Finland', '3'),
  ('Hungary', '2'),
  ('The Netherlands', '28'),
  ('The USA', '610'),
  ('The United Kingdom', '95'),
  ('China', '83'),
  ('Iran', '76'),
  ('Turkey', '65'),
  ('Belgium', '34'),
  ('Canada', '28'),
  ('Switzerland', '26'),
  ('Brazil', '25'),
  ('Austria', '14'),
  ('Israel', '12')
  ]

def to_dictionary():
    resdic={}
    for (country,country_key) in list_of_tuples:
        if country_key not in resdic:
            resdic[country_key]=[]
        resdic[country_key].append(country)
    for country_key in resdic:
        for country in resdic[country_key]:
            print("\'"+country_key+"\' : \'"+country+"\'")

if __name__=='__main__':
    to_dictionary()