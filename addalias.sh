#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "# To permentally add arsenal as the command 'a' add this to your ~/.bashrc, ~/.zshrc, ~/.bash_aliases depending on your shell configuration :"
echo "alias a='${DIR}/run'"

echo "Examples :"
echo "echo \"alias a='${DIR}/run'\" >> ~/.bash_aliases && source ~/.bashrc"
echo "echo \"alias a='${DIR}/run'\" >> ~/.zshrc && source ~/.zshrc"
echo "echo \"alias a='${DIR}/run'\" >> ~/.bashrc && source ~/.bashrc"
