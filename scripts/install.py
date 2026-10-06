import argparse, pathlib, shutil
p=argparse.ArgumentParser(description='Instala uma única skill modular, sem sobrescrever arquivos.')
p.add_argument('--target',choices=['codex','claude','both'],default='both')
p.add_argument('--dest',type=pathlib.Path,help='Pasta pai personalizada; exige target individual')
a=p.parse_args()
if a.dest and a.target=='both': p.error('--dest exige --target codex ou claude')
source=pathlib.Path(__file__).resolve().parents[1]
targets=['codex','claude'] if a.target=='both' else [a.target]
destinations=[((a.dest.expanduser() if a.dest else pathlib.Path.home()/('.agents/skills' if t=='codex' else '.claude/skills'))/'universal-skills') for t in targets]
for dest in destinations:
    if dest.exists(): p.error(f'Instalação já existe: {dest}; faça backup antes de substituir.')
for dest in destinations:
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copytree(source,dest,ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc'))
    print(f'Instalado: {dest}')
