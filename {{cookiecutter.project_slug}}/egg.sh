#!/bin/bash

fetch_ascii_art(){
    touch .ascii-art
    curl \
    'https://ssfy.sh/dev/text-to-ascii-art@d9d0510c/textToAsciiArt?text={{cookiecutter.project_name}}&font=5%20Line%20Oblique' >> .ascii-art
    echo "" >> .ascii-art
    echo "By: https://github.com/arthurhenrique/cookiecutter-fastapi" >> .ascii-art
}

prolado(){
    cat .ascii-art
    echo "[RUNNING] http://localhost:8080/docs"
    echo "[CTRL-C] to exit or wait.."
}

prooutro(){
    cat .ascii-art
    echo "[RUNNING] http://localhost:8080/docs"
    echo "[CTRL-C] to exit or wait..."
}

if [[ ! -e .ascii-art ]]; then
    fetch_ascii_art
fi

egg="$(python -c 'print("clear ; prolado ; sleep 1 ; clear ; prooutro; sleep 1;" * (0xDEADBEAF - (0xDEADBEAF - 42)))')"
eval $egg