#!/bin/sh

POSTUREDIR="/opt/cisco/hostscan"
LOG="/tmp/posture-uninstall.log"

LAUNCHD_DIR="/Library/LaunchDaemons"
LAUNCHD_FILE="com.cisco.anyconnect.ciscod.plist"
LAUNCHD64_FILE="com.cisco.anyconnect.ciscod64.plist"

ANYCONNECT_POSTURE_PACKAGE_ID=com.cisco.pkg.anyconnect.posture

echo "Uninstalling Cisco AnyConnect Posture Module..."
echo "Uninstalling Cisco AnyConnect Posture Module..." > "${LOG}"
echo `whoami` "invoked $0 from " `pwd` " at " `date` >> "${LOG}"

# Check for root privileges
if [ `id | sed -e 's/(.*//'` != "uid=0" ]; then
  echo "Sorry, you need super user privileges to run this script."
  echo "Sorry, you need super user privileges to run this script." >> "${LOG}"
  exit 1
fi

# stop ciscod and remove launchd
if [ -e ${LAUNCHD_DIR}/${LAUNCHD_FILE} ] ; then
    echo "ciscod 32bit..." >> "${LOG}"
    echo "/bin/launchctl unload ${LAUNCHD_DIR}/${LAUNCHD_FILE}" >> "${LOG}"
    /bin/launchctl unload ${LAUNCHD_DIR}/${LAUNCHD_FILE} >> "${LOG}" 2>&1
	rm -f "${LAUNCHD_DIR}/${LAUNCHD_FILE}"
fi

# stop ciscod64 and remove launchd
if [ -e ${LAUNCHD_DIR}/${LAUNCHD64_FILE} ] ; then
    echo "ciscod 64bit..." >> "${LOG}"
    echo "/bin/launchctl unload ${LAUNCHD_DIR}/${LAUNCHD64_FILE}" >> "${LOG}"
    /bin/launchctl unload ${LAUNCHD_DIR}/${LAUNCHD64_FILE} >> "${LOG}" 2>&1
	rm -f "${LAUNCHD_DIR}/${LAUNCHD64_FILE}"
fi

# Remove those pre-deploy files that we may have installed

if [ -e ${POSTUREDIR} ]; then
  echo "rm -rf ${POSTUREDIR}" >> "${LOG}"
  rm -rf ${POSTUREDIR} >> "${LOG}" 2>&1
fi

# update manifest
ANYCONNECT_INSTPREFIX="/opt/cisco/anyconnect"
ANYCONNECT_BINDIR="/opt/cisco/anyconnect/bin"
ACMANIFESTDAT="${ANYCONNECT_INSTPREFIX}/VPNManifest.dat"
POSTUREMANIFEST="ACManifestPOS.xml"

# update the VPNManifest.dat; if no entries remain in the .dat file then
# this tool will delete the file - DO NOT blindly delete VPNManifest.dat by
# adding it to the FILELIST above - allow this tool to delete the file if needed
if [ -f "${ANYCONNECT_BINDIR}/manifesttool" ]; then
  echo "${ANYCONNECT_BINDIR}/manifesttool -x ${ANYCONNECT_INSTPREFIX} ${ANYCONNECT_INSTPREFIX}/${POSTUREMANIFEST}" >> "${LOG}"
  ${ANYCONNECT_BINDIR}/manifesttool -x ${ANYCONNECT_INSTPREFIX} ${ANYCONNECT_INSTPREFIX}/${POSTUREMANIFEST}
fi

# check the existence of the manifest file - if it does not exist, remove the manifesttool
if [ ! -f ${ACMANIFESTDAT} ] && [ -f ${ANYCONNECT_BINDIR}/manifesttool ]; then
  echo "Removing ${ANYCONNECT_BINDIR}/manifesttool" >> "${LOG}"
  rm -f ${ANYCONNECT_BINDIR}/manifesttool
fi

rm -f ${ANYCONNECT_INSTPREFIX}/${POSTUREMANIFEST}

# remove installer receipt
pkgutil --forget ${ANYCONNECT_POSTURE_PACKAGE_ID} >> "${LOG}" 2>&1

echo "Successfully removed Cisco AnyConnect Posture Module from the system." >> "${LOG}"
echo "Successfully removed Cisco AnyConnect Posture Module from the system."

exit 0
