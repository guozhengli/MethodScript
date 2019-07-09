#!/bin/sh

INSTPREFIX="/opt/cisco/anyconnect"
BINDIR="${INSTPREFIX}/bin"
LEGACY_BINDIR="/opt/cisco/vpn/bin"
DARTDIR="${INSTPREFIX}/dart"
CONFIGXMLDIR="${DARTDIR}/xml/config"
REQUESTXMLDIR="${DARTDIR}/xml/request"
APPDIR="/Applications/Cisco"
DARTAPP="Cisco AnyConnect DART.app"
ACMANIFESTDAT="${INSTPREFIX}/VPNManifest.dat"
DARTMANIFEST="ACManifestDART.xml"
LOG="/tmp/dart-uninstall.log"
UNINSTALLER="Uninstall AnyConnect DART.app"

ANYCONNECT_DART_PACKAGE_ID=com.cisco.pkg.anyconnect.dart

# List of files to remove
FILELIST=("${APPDIR}/${DARTAPP}" \
          "${INSTPREFIX}/${DARTMANIFEST}" \
          "${BINDIR}/dart_uninstall.sh" \
          "${LEGACY_BINDIR}/dart_uninstall.sh" \
          "${DARTDIR}" \
          "${APPDIR}/${UNINSTALLER}")
		  
echo "Uninstalling Cisco AnyConnect Diagnostics and Reporting Tool..."
echo "Uninstalling Cisco AnyConnect Diagnostics and Reporting Tool..." > "${LOG}"
echo `whoami` "invoked $0 from " `pwd` " at " `date` >> "${LOG}"

# Check for root privileges
if [ `id | sed -e 's/(.*//'` != "uid=0" ]; then
  echo "Sorry, you need super user privileges to run this script."
  echo "Sorry, you need super user privileges to run this script." >> "${LOG}"
  exit 1
fi

# update the VPNManifest.dat; if no entries remain in the .dat file then
# this tool will delete the file - DO NOT blindly delete VPNManifest.dat by
# adding it to the FILELIST above - allow this tool to delete the file if needed
if [ -f "${BINDIR}/manifesttool" ]; then
  echo "${BINDIR}/manifesttool -x ${INSTPREFIX} ${INSTPREFIX}/${DARTMANIFEST}" >> "${LOG}"
  ${BINDIR}/manifesttool -x ${INSTPREFIX} ${INSTPREFIX}/${DARTMANIFEST}
fi

# check the existence of the manifest file - if it does not exist, remove the manifesttool, setuidtool
if [ ! -f ${ACMANIFESTDAT} ]; then
  if [ -f ${BINDIR}/manifesttool ]; then
    echo "Removing ${BINDIR}/manifesttool" >> "${LOG}"
    rm -f ${BINDIR}/manifesttool
  fi
  if [ -f ${BINDIR}/SetUIDTool ]; then
    echo "Removing ${BINDIR}/SetUIDTool" >> "${LOG}"
    rm -f ${BINDIR}/SetUIDTool
  fi
fi

# ensure that DART is not running
OURPROCS=`ps -A -o pid,command | egrep '(Cisco AnyConnect DART)' | egrep -v 'grep|dart_uninstall' | awk '{print $1}'`
if [ -n "${OURPROCS}" ] ; then
    for DOOMED in ${OURPROCS}; do
        echo Killing `ps -A -o pid,command -p ${DOOMED} | grep ${DOOMED} | egrep -v 'ps|grep'` >> "${LOG}"
        kill -INT ${DOOMED} >> "${LOG}" 2>&1
    done
fi

# Remove only those files that we know we installed
INDEX=0
while [ $INDEX -lt ${#FILELIST[@]} ] ; do
    echo "rm -rf "${FILELIST[${INDEX}]}"" >> "${LOG}"
    rm -rf "${FILELIST[${INDEX}]}"
    let  "INDEX = $INDEX + 1"
done

# Remove the bin directory if it is empty
if [ -e ${BINDIR} ] ; then
  if [ ! -z `find "${BINDIR}" -prune -empty` ] ; then
    echo "rm -df "${BINDIR}"" >> ${LOG}
    rm -df "${BINDIR}" >> ${LOG} 2>&1
  fi	
fi

# Remove the legacy bin directory if it is empty
if [ -e ${LEGACY_BINDIR} ] ; then
  if [ ! -z `find "${LEGACY_BINDIR}" -prune -empty` ] ; then
    echo "rm -df "${LEGACY_BINDIR}"" >> ${LOG}
    rm -df "${LEGACY_BINDIR}" >> ${LOG} 2>&1
  fi
fi

# Remove the Cisco directory if it is empty
if [ ! -z `find "${APPDIR}" -prune -empty` ] ; then 
    echo "rm -rf "${APPDIR}"" >> "${LOG}"
    rm -rf "${APPDIR}"
fi

# remove installer receipt
pkgutil --forget ${ANYCONNECT_DART_PACKAGE_ID} >> "${LOG}" 2>&1

echo "Successfully removed Cisco AnyConnect Diagnostics and Reporting Tool from the system." >> "${LOG}"
echo "Successfully removed Cisco AnyConnect Diagnostics and Reporting Tool from the system."

exit 0
