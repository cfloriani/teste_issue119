from github import Github
import sys, os

# connet in repository
g = Github(sys.argv[1])
repo = g.get_repo(os.getenv('repository'))

# pega o nome da issue
name_issue = os.getenv('ref')[11:]

#pega o numero da issue
for cont in range(0,len(name_issue)):
    if name_issue[cont] == '-':
        num_issue = name_issue[:cont]
        break

# cria o nome do pr
title_pr = 'WIP: ' + name_issue

# cria o pr
# verificar se existe o pr
existe = False
for pull_request in repo.get_pulls(state='open'):
    if pull_request.title == title_pr:
        existe = True

# caso não exista ele cria
if existe is False:
    try:
        repo.create_pull(title=title_pr, body='#' + num_issue, head=name_issue, base='master')
    except:
        print('Branch sem alterações')
    # pesquisa o número do pr para atribuir a label
    for pull_request in repo.get_pulls(state='open'):
        if pull_request.title == title_pr:
            pr = repo.get_pull(pull_request.number)
            pr.add_to_labels('pr: em andamento')
            break
