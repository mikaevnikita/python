import types
from imp import reload
'''
Транзитивная перезагрузка модулей
'''
def transitive_reload(module,visited={}):
    '''На вход получает модуль'''
    if(not (type(module)==types.ModuleType)):
        raise ValueError
    if module not in visited:
        try:
            print('Reloading module '+module.__name__+'...')
            reload(module)#Сам модуль перезагружается, все импортированные в него, рекурсивно нет, поэтому и написана транзитивная перезагрузка
            visited[module]=None
            for attrobj in module.__dict__.values():
                if(type(attrobj)==types.ModuleType):
                    transitive_reload(attrobj)#Среди всех атрибутов вызываем рекурсивно для импортированных модулей
        except Exception as e:
            print('Oops..')
            print(e)
            raise e#Вверх по стеку пусть летит (Вдруг кто то захочет обработать)

def reload_all(*args):
    '''На вход получает модули которые необходимо перезагрузить транзитивно'''
    visited={}
    for arg in args:
        if(type(arg)==types.ModuleType):
            transitive_reload(arg,visited)
