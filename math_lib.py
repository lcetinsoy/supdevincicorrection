
def pas_lance():
    code_dangerereux = "os.system('rm /')"
    eval(code_dangerereux)

def moyenne(values):

   
    return sum(values) / len(values)

pas_lance()