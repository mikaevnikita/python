def print_ierarhy(some_class,deep_tab=''):
    print(deep_tab,some_class.__name__)
    parents=some_class.__bases__
    if(len(parents)==0):
        deep_tab=''
    else:
        deep_tab+='\t'
    for parent in parents:
        print_ierarhy(parent,deep_tab)