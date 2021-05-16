import re

deep_ocean = '''oCeAn Marlin OcEaN oceAN ocEAN oCEAN OCEAN OCEAn OCEan OCean Ocean ocean oCeAn OcEaN oceAN ocEAN  
                OCEAN OCEAn OCEan OCean Ocean ocean oCeAn OcEaN oceAN ocEAN oCEAN OCEAN OCEAn OCEan OCean Ocean 
                ocean oCeAn OcEaN nemaa ocEAN oCEAN OCEAN OCEAn OCEan OCean ocean oCeAn OcEaN oceAN ocEAN 
                oCEAN OCEAN OCEAn OCEan OCean Ocean ocean oNeMa OcEaN oceAN ocEAN oCEAN OCEAN OCEAn OCEan OCean 
                Ocean ocean oCeAn OcEaN oceAN nenemo oCEAN OCEAN OCEAn OCEan OCean Ocean Nemo ocean oCeAn OcEaN 
                oceAN ocEAN oCEAN OCEAN OCEAn OCEan OCean Ocean ocean oCeAn OcEaN oceAN ocEAN oCEAN OCEAN OCEAn 
                OCEan OCean Ocean ocean  '''

nemo_pattern = r'[Nn]em\w{,2}'

# search() же производит поиск по всему тексту, но только до первого совпадения
matched = re.search(nemo_pattern, deep_ocean)
print(f'Возвращается объект {matched} внутри которого содержится информация о совпадении')  # re.Match object

# Эту информацию можно извлечь следующими методами:
print(f'Подстрока, совпавшая с паттерном поиска {matched.group()}')  # type 'str'
print(f'Индекс начала этой подстроки {matched.start()}')  # 'int'
print(f'И индекс её окончания {matched.end()}')  # 'int'