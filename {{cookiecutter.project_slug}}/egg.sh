HIDDEN_ART=".ascii-art"

fetch_ascii_art(){
    touch $(HIDDEN_ART);
    curl \
    'https://ssfy.sh/dev/text-to-ascii-art@d9d0510c/textToAsciiArt?text={{cookiecutter.project_slug}}&font=5 Line Oblique' >> $(HIDDEN_ART)
    echo "" >> $(HIDDEN_ART)
    echo "By: https://github.com/arthurhenrique/cookiecutter-fastapi" >> $(HIDDEN_ART)
}

prolado(){
    cat "$(HIDDEN_ART)"
    echo "[RUNNING] http://localhost:8080/docs"
    echo "[CTRL-C] to exit or wait.."
}

prooutro(){
    cat "$(HIDDEN_ART)"
    echo "[RUNNING] http://localhost:8080/docs"
    echo "[CTRL-C] to exit or wait..."
}


fetch_ascii_art
egg="$(python -c 'print("clear ; prolado ; sleep 1 ; clear ; prooutro; sleep 1;" * (0xDEADBEAF - (0xDEADBEAF - 42)))')"
eval $egg