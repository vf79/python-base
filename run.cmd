@echo off

chcp 65001
set name="python-base"

if "%1"=="--clean" goto clean
if "%1"=="--env" goto env
if "%1"=="--execute" goto execute
if "%1"=="--formate" goto formate
if "%1"=="--install" goto install
if "%1"=="--install-dev" goto install-dev
if "%1"=="--install-test" goto install-test
if "%1"=="--test" goto test
if "%1"=="--test-debug" goto test-debug
if "%1"=="--test-run" goto test-run
goto help

:clean
    echo "Excluindo arquivos e diretorios desnecessários..."
    for /d /r . %%d in (__pycache__, *.egg-info, .pytest_cache) do @if exist "%%d" rd /s /q "%%d"
    for /r . %%f in (*.pyc) do @if exist "%%f" del "%%f"
    :: rd /s /q build
    :: rd /s /q htmlcov
    :: del .coverage
goto end

:env
    echo "Para setar variáveis de ambiente em powershell use:"
    echo "[System.Environment]::SetEnvironmentVariable('<variavel>','<valor>')"
    echo "Para exibir as variaveis de ambiente em powershell use:"
    echo "dir env:<variavel> ou dir env: para exibir todas as variaveis"
goto end

:execute
    echo "Para executar o script digite:"
    echo "python script.py"
    echo "Para executar debug digite:"
    echo "python -m pdb script.py"
    echo "determinando linha de breakpoint"
    echo "python -m pdb -c ""until 31"" script.py"

goto end

:formate
    echo "Formatando o codigo..."
    isort .
    black -l 79 .
    flake8 .
goto end

:install
    echo "Instalando dependências..."
    pip install -e .
goto end

:install-dev
    echo "Instalando dependências de desenvolvimento..."
    pip install -e .[dev]
goto end

:install-test
    echo "Instalando dependências de testes..."
    pip install -e .[test]
goto end

:test
    echo "Executando testes..."
    pytest tests\ -vv --cov=%name%
    coverage html
goto end

:test-debug
    echo "Executando testes com debug..."
    pytest tests\ -vv --pdb --pdbcls=IPython.terminal.debugger:Pdb -s
goto end

:test-run
    echo "Executando testes selecionado..."
    pytest tests\ -m run -vv --cov=%name%
    coverage html
goto end

:help
    echo "Utilize .\run.cmd --<parametro>"
    echo "Parâmetros:"
    echo "clean - Limpa o codigo"
    echo "env - Exibe informações para configurar environment"
    echo "execute - Exibe o comando para executar o app"
    echo "formate - Formata o codigo em 80 colunas"
    echo "install - Instala dependências"
    echo "install-dev - Instala dependências de desenvolvimento"
    echo "install-test - Instalac dependências de testes"
    echo "test - Executa testes"
    echo "test-debug - Executa testes com debug ipdb"
    echo "test-run - Executa teste selecionado com marker run"

:end
    echo "Script finalizado."