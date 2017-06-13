#!/usr/bin/env bash
# First thing, detect macOS or Linux.
PYQTINSTALL=false

function testPyQt4 {
    # Detecting whether PyQt is already installed.
    python -c "import PyQt4"
    EXITCODE=$?
    if [[ ${EXITCODE} -eq 0 ]]; then
        PYQTINSTALL=true
    else
        PYQTINSTALL=false
    fi
}

testPyQt4

SYSTEM=`uname`

if [[ ${SYSTEM} == *"Darwin"* ]]; then
    echo "Detected macOS..."
    # now attempt to install PyQt
    if [[ ${PYQTINSTALL} == false ]]; then
        echo "Attempting to install PyQt4"
        if ! hash brew 2>/dev/null; then
            echo "Looks like brew isn't installed"
            echo "Installing brew..."
            /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        fi
        brew install cartr/qt4/pyqt
        EXITCODE=$?
        if [[ ${EXITCODE} -ne 0 ]]; then
            echo "There was a problem install PyQt using brew!"
            BREWINSTALL=false
        elif [[ ${EXITCODE} -eq 0 ]]; then
            BREWINSTALL=true
        fi
        if [[ ${BREWINSTALL} == false ]]; then
            echo "Try installing brew and typing 'brew install PyQt'"
            echo "Alternatively, check out these precompiled Mac binaries:"
            echo "https://sourceforge.net/projects/pyqtx/files/"
        elif [[ ${BREWINSTALL} == true ]]; then
            echo "Testing PyQt4 install"
            echo "Adding brew site-packages to PYTHONPATH -- make sure to source ~/.bash_profile"
            echo "Following lines added by install.sh" >> ~/.bash_profile
            echo "PYTHONPATH=\"${PYTHONPATH}:$(brew --prefix)/lib/python2.7/site-packages\"" >> ~/.bash_profile
            source ~/.bash_profile
            # testPyQt4
            # echo "PyQt4 successfully installed? ${PYQTINSTALL}"
        fi
    fi
elif [[ ${SYSTEM} == *"Linux"* ]]; then
    echo "Detected Linux OS..."
   # PYQTINSTALL=false
    # install PyQt under Linux
    if [[ ${PYQTINSTALL} == false ]]; then
        echo "Attempting to install PyQt4"
        if hash apt 2>/dev/null; then
            echo "Installing on Debian based system"
            sudo apt-get install python-qt4
        else if hash dfn 2>/dev/null; then
            echo "Installing on Fedora based system"
            sudo dfn install python-qt4
        else
            echo "Trying to install with yum..."
            sudo yum install python-qt4
        fi
    fi
else
    echo "Couldn't detect the current OS. Exiting"
    exit 0
fi

testPyQt4
