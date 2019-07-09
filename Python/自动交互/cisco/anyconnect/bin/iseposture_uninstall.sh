#!/bin/sh

ANYCONNECT_INSTPREFIX="/opt/cisco/anyconnect"
ANYCONNECT_BINDIR="${ANYCONNECT_INSTPREFIX}/bin"
ANYCONNECT_LIBDIR="${ANYCONNECT_INSTPREFIX}/lib"
ANYCONNECT_PLUGINDIR="${ANYCONNECT_BINDIR}/plugins"
ISEPOSTURE_PROFILEDIR="${ANYCONNECT_INSTPREFIX}/iseposture"

LAUNCHD_DIR="/Library/LaunchDaemons"
LAUNCHD_FILE="com.cisco.anyconnect.aciseagentd.plist"

LOG="/tmp/iseposture-uninstall.log"

ANYCONNECT_ISE_POSTURE_PACKAGE_ID=com.cisco.pkg.anyconnect.iseposture

ISEBINFILES="acise aciseposture aciseagentd iseposture_uninstall.sh"
ISELIBFILES="libacise.dylib"
ISEPLUGINFILES="libaciseapi.dylib libaciseshim.dylib libacisectrl.dylib"


echo "Uninstalling Cisco AnyConnect ISE Posture Module..."
echo "Uninstalling Cisco AnyConnect ISE Posture Module..." > "${LOG}"
echo `whoami` "invoked $0 from " `pwd` " at " `date` >> "${LOG}"

# Check for root privileges
if [ `id | sed -e 's/(.*//'` != "uid=0" ]; then
  echo "Sorry, you need super user privileges to run this script."
  echo "Sorry, you need super user privileges to run this script." >> "${LOG}"
  exit 1
fi


# Remove those pre-deploy files that we may have installed

for f in ${ISEBINFILES}; do
    if [ -e ${ANYCONNECT_BINDIR}/$f ]; then
       echo "rm -rf ${ANYCONNECT_BINDIR}/$f" >> "${LOG}"
       rm -rf ${ANYCONNECT_BINDIR}/$f >> "${LOG}" 2>&1
    fi
done

for f in ${ISELIBFILES}; do
    if [ -e ${ANYCONNECT_LIBDIR}/$f ]; then
       echo "rm -rf ${ANYCONNECT_LIBDIR}/$f" >> "${LOG}"
       rm -rf ${ANYCONNECT_LIBDIR}/$f >> "${LOG}" 2>&1
    fi
done

for f in ${ISEPLUGINFILES}; do
    if [ -e ${ANYCONNECT_PLUGINDIR}/$f ]; then
       echo "rm -rf ${ANYCONNECT_PLUGINDIR}/$f" >> "${LOG}"
       rm -rf ${ANYCONNECT_PLUGINDIR}/$f >> "${LOG}" 2>&1
    fi
done

# Remove ISE Posture profile directory
# TODO AKK 3.2 FCS - Do this only for non-upgrade uninstall: rm -rf ${ISEPOSTURE_PROFILEDIR} >> "${LOG}" 2>&1

# update manifest
ACMANIFESTDAT="${ANYCONNECT_INSTPREFIX}/VPNManifest.dat"
ISEPOSTUREMANIFEST="ACManifestISEPosture.xml"

# update the VPNManifest.dat; if no entries remain in the .dat file then
# this tool will delete the file - DO NOT blindly delete VPNManifest.dat by
# adding it to the FILELIST above - allow this tool to delete the file if needed
if [ -f "${ANYCONNECT_BINDIR}/manifesttool" ]; then
  echo "${ANYCONNECT_BINDIR}/manifesttool -x ${ANYCONNECT_INSTPREFIX} ${ANYCONNECT_INSTPREFIX}/${ISEPOSTUREMANIFEST}" >> "${LOG}"
  ${ANYCONNECT_BINDIR}/manifesttool -x ${ANYCONNECT_INSTPREFIX} ${ANYCONNECT_INSTPREFIX}/${ISEPOSTUREMANIFEST}
fi

# check the existence of the manifest file - if it does not exist, remove the manifesttool
if [ ! -f ${ACMANIFESTDAT} ] && [ -f ${ANYCONNECT_BINDIR}/manifesttool ]; then
  echo "Removing ${ANYCONNECT_BINDIR}/manifesttool" >> "${LOG}"
  rm -f ${ANYCONNECT_BINDIR}/manifesttool
fi

rm -f ${ANYCONNECT_INSTPREFIX}/${ISEPOSTUREMANIFEST}

# stop agent and remove launchd
if [ -e ${LAUNCHD_DIR}/${LAUNCHD_FILE} ] ; then
    echo "Stopping ISE posture agent..." >> "${LOG}"
    echo "sudo launchctl unload ${LAUNCHD_DIR}/${LAUNCHD_FILE}" >> "${LOG}"
    logger "Stopping the ISE Posture agent..."
    sudo launchctl unload ${LAUNCHD_DIR}/${LAUNCHD_FILE} >> "${LOG}" 2>&1
	rm -f "${LAUNCHD_DIR}/${LAUNCHD_FILE}"
fi

# remove installer receipt
pkgutil --forget ${ANYCONNECT_ISE_POSTURE_PACKAGE_ID} >> "${LOG}" 2>&1

echo "Successfully removed Cisco AnyConnect ISE Posture Module from the system." >> "${LOG}"
echo "Successfully removed Cisco AnyConnect ISE Posture Module from the system."

exit 0
