#!/bin/bash
set -euo pipefail
source ./bash_scripts/colors.sh
create_boilerplate(){
    mkdir -p app/models app/utils app/decorators pre/models pre/utils pre/decorators 
    touch pre/__init__.py
    touch app/__init__.py
    mkdir -p __tests__/pre
    mkdir -p __tests__/app
    touch pylintrc.toml
    
}
git_handler(){
    if [ ! -d ".git" ];then
    git init
    {
        echo -e ".venv/\n"
        echo -e "__pycache__/\n"
    }>>.gitignore
    else
        echo -e "${RED_COLOR} Already a git repo ${NO_COLOR}"
    fi
}
git_handler