from curso import Curso
from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def get_curso():
    t=open('post.txt','r')
    d=t.readlines()

    return d

@app.get('/busca_id')
def get_curso_id(id):
    c=''
    t=open('post.txt','r')
    d=t.readlines()

    for x in d:
        x=x.rstrip('\n')
        x=eval(x)
        if int(x['id'])==int(id):
            c=str(x)
            break
        else:
            c='curso inexistente'

    return c

@app.get('/cadastra_curso')
def post_curso(id:int,titulo:str,aulas:str,horas:int,dia:str):
    c=Curso(id,titulo,aulas,horas,dia)
    t=open('post.txt','r+')
    d=t.readlines()

    t.writelines(str({
        'id':c.id,
        'titulo':c.titulo,
        'aulas':c.aulas,
        'horas':c.horas,
        'dia':c.dia
        })+'\n')
    t.close()

    return 'curso '+str(c.titulo)+' foi postado com sucesso acesse e pode ser observado na pagina inicial ou no arquivo post'

@app.get('/altera')
def put_curso(id,titulo,aulas,horas,dia):
    c=''
    t=open('post.txt','r')
    d=t.readlines()

    for x in d:
        x=x.rstrip('\n')
        x=eval(x)

        if int(x['id'])==int(id):
            if str(titulo)!='':x['titulo']=titulo
            if str(aulas)!='':x['aulas']=aulas
            if horas!=None:x['horas']=horas
            if str(dia)!='':x['dia']=dia
            c+=str(x)+'\n'
        else:
            c+=str(x)+'\n'
    t.close()

    t=open('post.txt','w')
    t.writelines(c)
    t.close()
    return 'dados alterados'

@app.get('/delete')
def delete_curso(id):
    c=''
    t=open('post.txt','r')
    d=t.readlines()

    for x in d:
        x=x.rstrip('\n')
        x=eval(x)

        if int(x['id'])==int(id):
            pass
        else:
            c=str(x)+'\n'
        t.close()

    t=open('post.txt','w')
    t.writelines(c)
    t.close()

    return 'curso deletado'