echo reinstalling archive ${deployed.deployable.file} in ${deployed.container.home}
echo Stop the service...
${deployed.container.serviceStop}
echo Removing old artifacts
sleep 15s
rm -rf ${deployed.container.targetDirectory}/${deployed.container.artifactsName}
echo Deploying new artifact
cp ${deployed.deployable.file} ${deployed.container.targetDirectory}/${deployed.container.artifactsName}
echo Start the service...
${deployed.container.serviceStart}
