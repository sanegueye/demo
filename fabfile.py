from fabric.api import run

def host_type():
    run('uname -s && pwd && ls')
    put(localpath,remotepath,mode=int(mod, 8))
