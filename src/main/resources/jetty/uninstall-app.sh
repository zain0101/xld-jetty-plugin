echo removing deployment
echo Stop the service...
${deployed.container.serviceStop}
echo Removing artifacts
rm -rf ${deployed.container.targetDirectory}/${deployed.container.artifactsName}
