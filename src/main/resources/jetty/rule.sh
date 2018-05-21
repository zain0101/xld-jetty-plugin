if [[ ${operation} == "CREATE" ]]
then   
  ./install-app.sh
elif [[ ${operation} == "MODIFY" ]]
then
  ./reinstall-app.sh 
elif [[ ${operation} == "DESTROY" ]]
then
  ./uninstall-app.sh
fi
