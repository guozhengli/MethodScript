#!/bin/sh

INSTPREFIX="/opt/cisco/anyconnect"
BINDIR="${INSTPREFIX}/bin"
PLUGINSDIR="${BINDIR}/plugins"
LIBDIR="${INSTPREFIX}/lib"
PROFILESDIR="${INSTPREFIX}/nvm"
ACMANIFESTDAT="${INSTPREFIX}/VPNManifest.dat"
NVMMANIFEST="ACManifestNVM.xml"
UNINSTALLLOG="/tmp/nvm-uninstall.log"

ANYCONNECT_NVM_PACKAGE_ID=com.cisco.pkg.anyconnect.nvm_v2

# Array of files to remove
FILELIST=("${INSTPREFIX}/${NVMMANIFEST}" \
          "${INSTPREFIX}/libacnvmctrl.dylib" \
          "${BINDIR}/acnvmagent" \
          "${BINDIR}/nvm_uninstall.sh" )

echo "Uninstalling Cisco AnyConnect Network Visibility Module..."
echo "Uninstalling Cisco AnyConnect Network Visibility Module..." > ${UNINSTALLLOG}
echo `whoami` "invoked $0 from " `pwd` " at " `date` >> ${UNINSTALLLOG}

# Check for root privileges
if [ `whoami` != "root" ]; then
  echo "Sorry, you need super user privileges to run this script."
  echo "Sorry, you need super user privileges to run this script." >> ${UNINSTALLLOG}
  exit 1
fi

# update the VPNManifest.dat; if no entries remain in the .dat file then
# this tool will delete the file - DO NOT blindly delete VPNManifest.dat by
# adding it to the FILELIST above - allow this tool to delete the file if needed
if [ -f "${BINDIR}/manifesttool" ]; then
  echo "${BINDIR}/manifesttool -x ${INSTPREFIX} ${INSTPREFIX}/${NVMMANIFEST}" >> ${UNINSTALLLOG}
  ${BINDIR}/manifesttool -x ${INSTPREFIX} ${INSTPREFIX}/${NVMMANIFEST}
fi

# check the existence of the manifest file - if it does not exist, remove the manifesttool
if [ ! -f ${ACMANIFESTDAT} ] && [ -f ${BINDIR}/manifesttool ]; then
  echo "Removing ${BINDIR}/manifesttool" >> ${UNINSTALLLOG}
  rm -f ${BINDIR}/manifesttool
fi

# move the plugins to a different folder to stop the NVM agent and then remove
# these plugins once NVM agent is stopped. 
mv -f ${PLUGINSDIR}/libacnvmctrl.dylib ${INSTPREFIX} 2>&1 >/dev/null
echo "mv -f ${PLUGINSDIR}/libacnvmctrl.dylib ${INSTPREFIX}" >> ${UNINSTALLLOG}

# wait for 2 seconds for the NVM agent to exit
sleep 2

# ensure that the NVM agent is not running
NVMPROC=`ps -A -o pid,command | grep '(${BINDIR}/acnvmagent)' | egrep -v 'grep|nvm_uninstall' | awk '{print $1}'`
if [ ! "x${NVMPROC}" = "x" ] ; then
    echo Killing `ps -A -o pid,command -p ${NVMPROC} | grep ${NVMPROC} | egrep -v 'ps|grep'` >> ${UNINSTALLLOG}
    kill -TERM ${NVMPROC} >> ${UNINSTALLLOG} 2>&1
fi

# Remove only those files that we know we installed
INDEX=0
while [ $INDEX -lt ${#FILELIST[@]} ]; do
  echo "rm -rf "${FILELIST[${INDEX}]}"" >> ${UNINSTALLLOG}
  rm -rf "${FILELIST[${INDEX}]}"
  let "INDEX = $INDEX + 1"
done

# Remove the plugins directory if it is empty
if [ -d ${PLUGINSDIR} ]; then
  if [ ! -z `find "${PLUGINSDIR}" -prune -empty` ] ; then
    echo "rm -df "${PLUGINSDIR}"" >> ${UNINSTALLLOG}
    rm -df "${PLUGINSDIR}" >> ${UNINSTALLLOG} 2>&1
  fi	
fi

# Remove the bin directory if it is empty
if [ -d ${BINDIR} ]; then
  if [ ! -z `find "${BINDIR}" -prune -empty` ] ; then
    echo "rm -df "${BINDIR}"" >> ${UNINSTALLLOG}
    rm -df "${BINDIR}" >> ${UNINSTALLLOG} 2>&1
  fi	
fi

# Remove the lib directory if it is empty
if [ -d ${LIBDIR} ]; then
  if [ ! -z `find "${LIBDIR}" -prune -empty` ] ; then
    echo "rm -df "${LIBDIR}"" >> ${UNINSTALLLOG}
    rm -df "${LIBDIR}" >> ${UNINSTALLLOG} 2>&1
  fi
fi

# Remove the profiles directory
# During an upgrade, the profiles will be moved and restored by
# preupgrade and postupgrade scripts.

if [ -d ${PROFILESDIR} ]; then
    echo "rm -rf "${PROFILESDIR}"" >> ${UNINSTALLLOG}
    rm -rf "${PROFILESDIR}" >> ${UNINSTALLLOG} 2>&1
fi

# remove installer receipt
pkgutil --forget ${ANYCONNECT_NVM_PACKAGE_ID} >> ${UNINSTALLLOG} 2>&1

echo "Successfully removed Cisco AnyConnect Network Visibility Module from the system." >> ${UNINSTALLLOG}
echo "Successfully removed Cisco AnyConnect Network Visibility Module from the system."

exit 0
