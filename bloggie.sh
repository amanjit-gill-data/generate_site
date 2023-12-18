#!/usr/bin/bash

PROJECT_ROOT="$HOME/projects/personal/website"
GENERATE_REPO="$PROJECT_ROOT/generate_site"
PUBLISH_REPO="$PROJECT_ROOT/amanjit-gill-data.github.io"
CONFIG_PATH="$GENERATE_REPO/pelicanconf.py"

# $1 = expected no. arguments 
# $2 = actual no. arguments
check_argcount () {

  if [ $1 -ne $2 ]; then 
    echo "Incorrect number of arguments."
    exit 1
  fi 
}

# $1 = analysis|mathematics|programming|computing|opinion|pages|extra
get_path() {

  case $1 in 

    analysis|mathematics|programming|computing|opinion)
      path="$GENERATE_REPO/content/category/$1"
      ;;

    pages|extra)
      path="$GENERATE_REPO/content/$1"
      ;;

    *)
      echo "Invalid post path."
      exit 1
      ;;

  esac
}

# $1 = repo_path
# $2 = commit_message
git_acp() {

  echo "*** `basename "$1"` ***"
  
  cd "$1"
  git add . && git commit -m "$2" && git push
}

# $1 = edit|delete|generate|publish|config
# $2 = (for edit/delete) analysis|mathematics|programming|computing|opinion|pages|extra
# $2 = (for publish) "commit message"
# $3 = (for edit/delete) filename.md
case $1 in 

  edit)
    check_argcount 3 $#
    get_path $2 
    nvim "$path/$3"
    ;;

  delete)
    check_argcount 3 $#
    get_path $2
    rm -i "$path/$3"
    ;;

  generate)
    check_argcount 1 $#
    cd "$GENERATE_REPO"
    pelican content
    ;;

  publish)
    check_argcount 2 $#
    git_acp "$GENERATE_REPO" "$2" 
    git_acp "$PUBLISH_REPO" "$2"
    ;;

  config)
    check_argcount 1 $#
    nvim "$CONFIG_PATH"
    ;;

  *)
    echo "Invalid argument."

esac 


